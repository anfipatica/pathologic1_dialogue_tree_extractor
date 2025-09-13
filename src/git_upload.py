import git

def	upload_to_github():
	repo = git.Repo(".")
	repo.git.add(".")
	repo.index.commit("probando gitpython")
