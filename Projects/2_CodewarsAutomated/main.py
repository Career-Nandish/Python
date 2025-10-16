from GitHub import github as gh
from CodeWars import codewars as cw
from github import ContentFile


def main():    
	
	# Loading credentials
	#PAT = gh.load_gh_credentials()
	
	# Authenticating the PAT
	#gUser = gh.get_github_user(PAT)
	
	# Check if the folder/file already exists or not
	#gContent, repo_path = gh.check_folder_exists(gUser)

	#print(gContent, repo_path)
	
	# check if content is ContentFile or str
	#if gContent:
	#	pass
	#else:
	#	init_project(gUser, gContent)
	# based on that do future things

	# codewars

	# loading credentials
	cw_email, cw_password = cw.load_cw_credentials()
	
	# Loading session and the CSRF token
	cw_session, cw_token = cw.start_cw_session()

	cw_session, cw_username = cw.login_codewars(
		                          cw_session, cw_email, cw_password, cw_token
		                       )

	print(cw_session, cw_username)

	# If you have different usernames for github and codewars
	# please change it here or hardcode it as default value
	# in the function below

if __name__ == '__main__':
	main()