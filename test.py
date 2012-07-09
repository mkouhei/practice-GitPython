import os
from git import *

# see http://packages.python.org/GitPython/0.3.2/tutorial.html#tutorial-label


repo = Repo(".")


# bare repository check
if repo.bare:
    print(repo + " is bare")

# bare repository init
#repo = Repo.init("~/tmp/moge")
#assert repo.bare == True

# ro
repo.config_reader()

# w
#repo.config_writer()

# True: Changes not staged for commit
if repo.is_dirty():
    print("unstatged: " + str(repo.is_dirty()))

# When untracked file
if repo.untracked_files:
    print("untracked: " + str(repo.untracked_files))
    
# git clone from repo
# unable to use relative path
if os.path.isdir('/tmp/dest-clone'):
    cloned_repo = repo.clone('/tmp/dest-clone')

# git init
if not os.path.isdir('/tmp/dest-init'):
    new_repo = repo.init('/tmp/dest-init')

# archive to tarball
#repo.archive(open('/tmp/test.tar', 'w'))

#repo2 = Repo("/tmp/gitdb-test", odbt=GitDB)

if repo.heads:
    head = repo.head
    master = head.reference
    master.commit
    print(head.name, master, master.commit)
    head_ = repo.heads[0]
    print(head_.name, head_.commit, head_.commit.hexsha)

    log = master.log()
    # first reflog entry
    print(log[0])
    # last reflog entry
    print(log[-1])
