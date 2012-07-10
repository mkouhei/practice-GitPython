#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
from git import Git
import git.repo.fun
from git import Repo

prs = argparse.ArgumentParser(description='usage')
prs.add_argument('-b', action='store_true', help='git init --bare')
prs.add_argument('git_dir', action='store', help='To make and git init directory')
args = prs.parse_args()

try:
    # Check argument
    gdir = os.path.abspath(args.git_dir)

    # If not exist directory, make it.
    if args.__dict__.get('b'):
        if gdir.endswith('.git'):
            dirpath = gdir
        else:
            dirpath = gdir + '.git'
    else:
        dirpath = gdir

    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

    g = Git(dirpath)
    # If is not Git repository, git init
    if not git.repo.fun.is_git_dir(dirpath):

        # bare repository
        if args.__dict__.get('b'):
            repo = Repo.init(dirpath, bare=True)
        else:
            # local repository
            g.init()
            
            repo = Repo(dirpath)

            # Make .gitignore
            if not os.path.isfile(dirpath + '/.gitignore'):
                f = open(dirpath + '/.gitignore', 'w')
                f.write('')
                f.close()

            # git add .gitignore and first commit
            if repo.untracked_files or repo.is_dirty():
                # git add
                g.add('.gitignore')
                # git commit
                g.commit(m='First commit')

except RuntimeError as e:
    sys.stderr.write("ERROR: %s\n" % e)
