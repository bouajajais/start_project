from typing import TypedDict
from typing_extensions import Required
import requests

class GithubDetails(TypedDict, total=False):
    token: Required[str]
    username: Required[str]
    repo_name: Required[str]
    description: str
    private: bool
    

def create_repo(github_details: GithubDetails):
    token = github_details["token"]
    repo_name = github_details["repo_name"]
    description = github_details.get("description", "")
    private = github_details.get("private", False)
    
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return response.json()
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(f"Error message: {response.json().get('message', 'Unknown error')}")
        raise Exception("Failed to create repository")