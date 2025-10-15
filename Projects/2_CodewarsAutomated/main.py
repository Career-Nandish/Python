from GitHub import github as gh
from CodeWars import codewars as cw
from github import ContentFile


def main():    
	
	# Loading credentials
	PAT = gh.load_gh_credentials()
	
	# Authenticating the PAT
	gUser = gh.get_github_user(PAT)
	
	# Check if the folder/file already exists or not
	content = gh.check_folder_exists(gUser)

	#print(content)
	
	# check if content is ContentFile or str
	if isinstance(content, ContentFile.ContentFile):
		pass
	else:
		init_project(guser, content)
	# based on that do future things

	# codewars
	# creds = cw.load_cw_credentials()

	# If you have different usernames for github and codewars
	# please change it here or hardcode it as default value
	# in the function below
	#cw.codewars_login(creds, username = guser.login)

if __name__ == '__main__':
	main()