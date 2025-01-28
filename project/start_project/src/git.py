import os
from typing import Optional

from .github import GithubDetails, create_repo

def setup_git(github_details: Optional[GithubDetails] = None):
    # create README.md
    with open('README.md', 'w') as f:
        pass
    
    # git init
    os.system('git init')

    # git add README.md
    os.system('git add README.md')
    
    # git commit -m 'Initial commit'
    os.system('git commit -m "Initial commit"')
    
    # git branch -M main
    os.system('git branch -M main')
    
    if github_details:
        # create a new repository on GitHub
        create_repo(github_details)
    
        # git remote add origin <repo_url>
        repo_url = f'https://github.com/{github_details["username"]}/{github_details["repo_name"]}.git'
        os.system(f'git remote add origin {repo_url}')
        
        # git push -u origin main
        os.system('git push -u origin main')