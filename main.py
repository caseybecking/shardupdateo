import sites, github_connect, download_url, os, time, sys, itertools, threading

dir_path = os.path.dirname(os.path.realpath(__file__))

print("This will take some time!!")

#long process here
for target_list in sites.parse_sites():
    github_connect.get_repo_contents(target_list[0])
    download_url.find_sources(dir_path+"/"+target_list[1]+"/")