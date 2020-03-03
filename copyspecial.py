#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "???"


# +++your code here+++
# Write functions and modify main() to call them
# Given a dirname, returns a list of all its special files
def get_special_paths(dir):
    result = []
    paths = os.listdir(dir)  # list of paths in that dir
    for fname in paths:
        match = re.search(r'__(\w+)__', fname)
        if match:
            result.append(fname)
    return result

# Copy all of the given files to the given dir, creating it if necessary


def copy_to(paths, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, fname))

# Zip up all of the given files into a new zip file with the given name


def zip_to(paths, zipfile):
    command = ['zip', '-j', zipfile]
    command.extend(paths)
    print('\nCommand I\'m going to do {}'.format(' '.join(command)))
    subprocess.call(command)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='dest of "special files" to print')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    return args


def main():
    args = create_parser()
    # +++your code here+++
    # Call your functions
    # Gather all the special files
    paths = []
    for dirname in args.dir:
        paths.extend(get_special_paths(dirname))

    if not args.todir and not args.tozip:
        print('\n'.join(paths))
    if args.todir:
        copy_to(paths, args.todir)
    if args.tozip:
        zip_to(paths, args.tozip)


if __name__ == "__main__":
    main()

# python copyspecial.py --todir tmp .
# python copyspecial.py --tozip tmp.zip .
