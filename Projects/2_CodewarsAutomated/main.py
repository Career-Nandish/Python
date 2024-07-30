from GitHub import github as gh
from CodeWars import codewars as cw
from github import Github, GithubIntegration
from github import GithubException, AuthenticatedUser
from github import ContentFile

def main():    
	
	PAT = gh.load_gh_credentials()
	guser = gh.get_github_user(PAT)
	
	# content = gh.check_folder_exists(guser)
	# print(content)

	# check if content is contentfile or str
	# based on that do future things

	# codewars
	creds = cw.load_cw_credentials()

	# If you have different usernames for github and codewars
	# please change it here or hardcode it as default value
	# in the function below
	cw.codewars_login(creds, username = guser.login)

if __name__ == '__main__':
	main()