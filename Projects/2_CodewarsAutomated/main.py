from GitHub import github as gh
from github import Github, Auth, GithubIntegration, GithubException, AuthenticatedUser


def main():    
	PAT = gh.load_credentials()
	guser = gh.get_github_user(PAT)
	for i in guser.get_repos():print(i)

if __name__ == '__main__':
	main()