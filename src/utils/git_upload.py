import git
import utils.colors as colors
import os

def	upload_to_github():
	repo: git.Repo
	origin: git.Remote

	print(f"{colors.GREEN}\n\n-> Uploading the changes to github...{colors.STD}")
	try:
		repo = git.Repo(".")
		origin = repo.remote("origin")
		repo.git.add(".")
		repo.index.commit("uploading to github from python script...")
		origin.push()
	except:
		print(f"{colors.RED}Something went wrong while uploading the changes to github.{colors.STD}")
