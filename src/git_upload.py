import git

def	upload_to_github():
	repo = git.Repo(".")
	print(repo)
	repo.git.add(".")
	repo.index.commit("probando gitpython")
