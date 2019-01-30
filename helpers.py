import re, itertools
from string import Template
from prettytable import PrettyTable

def is_word_in_text(word, text):
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)
    return bool(matches)

def compare_versions(org, repo, current_current, source_version):
    #We will use this to compare if the current_version 
    #is less than or equal to the 
    pass

def remove_duplicates(l):
    return list(set(l))

def parse_output(input):
    t = PrettyTable(['Org', 'Repo', 'File', 'Line', 'Current Version', 'Latest Version'])
    # t = Template('Org: $org - Repo: $repo - File: $file - Line: $line - Current Version: $current_version - Latest Version: $latest_version')
    #we will use this to create the output and push it out
    #from the repsone of compare versions
    input.sort()
    list(input for input,_ in itertools.groupby(input))
    for target_list in input:
        t.add_row([target_list[1], target_list[0], target_list[4], target_list[5], target_list[3], target_list[2]])
    print(t)