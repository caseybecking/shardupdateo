from github import Github
from download_url import parse_download_url

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", login_or_token="55bf707283a6122c4e275dbf47f63132b5b65837")

def get_repo_contents(target_list):
    # Then play with your Github objects:
    target_url = target_list.split('/')
    del target_url[-1]
    repo_striped = target_url[-1]
    repo_path = "rackerlabs/"+repo_striped
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