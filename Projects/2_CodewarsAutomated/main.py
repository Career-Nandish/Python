from GitHub import github as gh
from CodeWars import codewars as cw
from github import Github, GithubIntegration
from github import GithubException, AuthenticatedUser
from github import ContentFile


def main():    
	
	# PAT = gh.load_gh_credentials()
	# guser = gh.get_github_user(PAT)
	# content = gh.check_folder_exists(guser)

	# check if content is contentfile or str
	# based on that do future things

	# codewars
	driver = cw.get_webdriver()
	creds = cw.load_cw_credentials()
	
	cw.codewars_navigate(driver, creds)

if __name__ == '__main__':
	main()