import os, sys, time, mmap
from pathlib import Path
import urllib.request
import helpers
import github_connect



def parse_download_url(repo_name, name, download_url):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = dir_path+'/'+repo_name
    file_name = directory+'/'+name
    ts = time.time()
    # print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    my_file = Path(file_name)
    if my_file.is_file():
        urllib.request.urlretrieve(download_url, directory+'/'+str(ts)+'_'+name)
    else:
        urllib.request.urlretrieve(download_url, directory+'/'+name)   

def find_sources(repo_name, directory_in_str):
    directory = os.fsencode(directory_in_str)
    response = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".tf"):
            with open(directory_in_str+filename, "r") as f:
                searchfile = open(directory_in_str+filename, "r")
                # for line in searchfile:
                for num, line in enumerate(searchfile, 1):   
                    if "source =" in line: 
                        
                        # print(directory_in_str+filename, num, line)
                        # print(num + ',' + line)
                        #based on what this returns we should be able to do our next check
                        # print(check_source_validity(line))
                        # we will now need to go get the source_version using get_repo_tags(repo)
                        for target_list in check_source_validity(line):
                            response1 = []
                            repo = target_list[0]
                            org = target_list[1]
                            current_version = target_list[2]
                            repo_tags = github_connect.get_repo_tags(repo+'/'+org)
                            response1.append(org)
                            response1.append(repo)
                            response1.append(repo_tags[0])
                            response1.append(current_version)
                            response1.append(filename)
                            response1.append(num)
                            response.append(response1)
                searchfile.close()
    helpers.parse_output(response, repo_name)

def check_source_validity(source_url):
    # splits = source_url.split(separator, maxsplit)
    #the idea of this is to make sure we can make a url out of the source
    #if it's valid we will go through it and find all it's branches - get_repo_tags(repo)
    #we have to parse it apart
    #repo_urls_version = [url,version]
    repo_urls_version = []
    if not helpers.is_word_in_text('github.com', source_url):
        pass
    else:    
        try:
            key, value = source_url.split(":")
        except ValueError:
            #github.com/rackspace-infrastructure-automation/aws-terraform-ec2_asg?ref=v0.0.6
            first_pass = source_url.split('/')
            del first_pass[0]
            org = first_pass[0]
            # repo = []
            for i in first_pass:
                # print(first_pass)
                try:
                    remove_and_store_version(org+'/'+first_pass[1])
                except IndexError:
                    del first_pass[0]
                    pass
                # print(first_pass)
                parse_tags = first_pass[1].split("?")
                version = parse_tags[1][5:][:-2]
                # url = org + '/' + parse_tags[0]
            repo_urls_version.append([org, parse_tags[0], version])
        else:
            #git@github.com:rackspace-infrastructure-automation/aws-terraform-elasticsearch//?ref=v0.0.2
            first_pass = source_url.split(':')
            # print(first_pass) 
            second_pass = first_pass[1].split('/')
            org = second_pass[0]
            repo = second_pass[1]
            # print(repo)
            if not helpers.is_word_in_text('ref=<git tag, branch, or commit hash here>', repo):
                # print(second_pass)
                version = second_pass[3][5:][:-2]
                repo_urls_version.append([org, repo, version])
            else:
                parse_tags = repo.split("?")
                # print(parse_tags)
                for parse_tag in parse_tags:
                    if 'ref=<git tag, branch, or commit hash here>' not in parse_tag :
                        # version = parse_tags[1][5:][:-2]
                        # repo_urls_version.append([org+'/'+parse_tag[:-4]])
                        if ".git" in parse_tag:
                            version = parse_tags[1][5:][:-2]
                        # print(version)
                        # repo_urls_version.append([org+'/'+parse_tag[:-4],version])
    return(repo_urls_version)


def remove_and_store_version(string):
    parse_tags = string.split("?")
    # for parse_tag in parse_tags:
        # print(parse_tags)

