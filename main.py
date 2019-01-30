import sites
import github_connect
import download_url
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

download_url.find_sources(dir_path+"/cap-aws-lamp/")



# for target_list in sites.parse_sites():
#     print(github_connect.get_repo_contents(target_list))

