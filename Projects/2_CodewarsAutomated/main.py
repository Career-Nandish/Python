from GitHub import github as gh
from CodeWars import codewars as cw
from github import ContentFile


def main():    

	# First run
	first_run = True

	# Loading credentials
	#gPAT = gh.load_gh_credentials()
	cw_email, cw_password = cw.load_cw_credentials()
	
	# Authenticating the PAT
	#gUser = gh.get_gh_user(gPAT)

	# Loading session and the CSRF token
	cw_session, cw_token = cw.start_cw_session()

	cw_session, cw_username = cw.login_cw(
		                          cw_session, cw_email, cw_password, cw_token
		                       )
	
	# Check if the folder/file already exists or not
	#gContent, gRepo_path = gh.check_gh_folder_exists(gUser)

	#print(gContent, repo_path)
	
	gContent = None

	# check if content is ContentFile or str
	if gContent:
		first_run = False
	else:
		cContent = cw.download_cw_solutions(
			           cw_session, cw_username, cw_token, gContent, first_run
			       )
		#gh.init_gh_project(gUser, cContent)

	# based on that do future things

	# codewars

	# loading credentials
	
	
	

	# print(cw_session, cw_username)

	# If you have different usernames for github and codewars
	# please change it here or hardcode it as default value
	# in the function below

if __name__ == '__main__':
	main()