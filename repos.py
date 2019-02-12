#This will loop over all the repos and pass back what is needed 
#Loop over each repo in the config
import json
from pprint import pprint

file = 'repos.json'

def parse_repos():
    with open(file) as f:
        data = json.load(f)
        repo = []
    for repos in data["repos"]:
        repo.append([repos["url"], repos["repo"]])
    return(repo)
