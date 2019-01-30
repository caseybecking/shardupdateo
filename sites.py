#This will loop over all the sites and pass back what is needed 
#Loop over each repo in the config
import json
from pprint import pprint

file = 'sites.json'

def parse_sites():
    with open(file) as f:
        data = json.load(f)
        site = []
    for sites in data["sites"]:
        site.append(sites["url"])
    return(site)


