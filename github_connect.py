import os
import json
from github import Github
from download_url import parse_download_url

with open('config.json', 'r') as f:
    config = json.load(f)

access_token = os.getenv('GITHUB_PUBLIC_ACCESS_TOKEN', config['DEFAULT']['GITHUB_PUBLIC_ACCESS_TOKEN'])
base_url = config['DEFAULT']['GITHUB_BASE_URL']

if not access_token:
    raise ValueError('You must have "GITHUB_PUBLIC_ACCESS_TOKEN" variable')

if not base_url:
    raise ValueError('You must have "GITHUB_BASE_URL" variable')

g = Github(base_url=base_url, login_or_token=access_token)

def get_repo_contents(target_list):
    # Then play with your Github objects:
    target_url = target_list.split('/')
    del target_url[-1]
    repo_striped = target_url[-1]
    repo_path = target_url[3]+'/'+repo_striped
    repo = g.get_repo(repo_path)
    contents = repo.get_contents("")
    while len(contents) > 1:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            parse_download_url(repo_striped, file_content.name, file_content.download_url)

def get_repo_tags(repos):
    #here we will want to bring back the tags from the repo
    response = []
    if ".git" in repos:
        repo = repos[:-4]
        repo = g.get_repo(repo)
        release = repo.get_latest_release()
        # response.append(repo.full_name)
        response.append(release.title)
    else:
        repo = g.get_repo(repos)
        release = repo.get_latest_release()
        # response.append(repo.full_name)
        response.append(release.title)
    return response
