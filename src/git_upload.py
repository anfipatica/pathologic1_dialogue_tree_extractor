import git
import utils.colors as colors
import os

def	upload_to_github():
	repo: git.Repo
	origin: git.Remote

	print(f"{colors.GREEN}\n\n-> Uploading the changes to github.")
	try:
		repo = git.Repo(".")
		origin = repo.remote("origin")
		repo.git.add(".")
		repo.index.commit("uploading to github from python script...")
		family = os.fork()
		state: bool = False

		if (family == 0):
			origin.push()
		else:
			while (os.WIFEXITED(family) == False):
				print("my hijo sigue corriendo...")
			print("y... murió")

	except:
		print(f"{colors.RED}Something went wrong while uploading the changes to github.{colors.STD}")
