import git
import utils.colors as colors
import os

def	upload_to_github():
	repo: git.Repo
	origin: git.Remote

	print(f"{colors.GREEN}\n\n-> Uploading the changes to github.", end="")
	try:
		repo = git.Repo(".")
		origin = repo.remote("origin")
		repo.git.add(".")
		repo.index.commit("uploading to github from python scriptAAAAAAAAA...")
		family = os.fork()
		state: bool = False

		if (family == 0):
			origin.push()
			return ()
		else:
			while (os.waitpid(family, os.WNOHANG)[0] == 0):
				print(".",end="")
				os.system("usleep 1000")
			print(f"{colors.STD}")
	except:
		print(f"{colors.RED}Something went wrong while uploading the changes to github.{colors.STD}")
