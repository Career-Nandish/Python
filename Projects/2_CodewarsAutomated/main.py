from GitHub import github as gh
from github import Github, GithubIntegration
from github import GithubException, AuthenticatedUser
from github import ContentFile


def main():    
	PAT = gh.load_credentials()
	guser = gh.get_github_user(PAT)
	content = gh.check_folder_exists(guser)


if __name__ == '__main__':
	main()