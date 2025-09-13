import git

def	upload_to_github():
	repo: git.Repo
	origin: git.Remote

	repo = git.Repo(".")
	origin = repo.remote("origin")
	repo.git.add(".")
	repo.index.commit("uploading to github from python script...")
	origin.push()
