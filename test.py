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
    if not os.path.isdir(gdir):
        os.mkdir(gdir)

    # If is not Git repository, git init
    if not git.repo.fun.is_git_dir(gdir) and not git.repo.fun.is_git_dir(gdir + '/.git'):
        # bare repository
        if args.__dict__.get('b'):
            repo = Repo.init(gdir, bare=True)
        # local repository
        else:
            g = Git(gdir)
            g.init()

except RuntimeError as e:
    sys.stderr.write("ERROR: %s\n" % e)
