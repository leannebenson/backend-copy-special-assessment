#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "LeanneBenson"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    list_files = []
    files = os.listdir(dirname)
    for file in files:
        match = re.search(r'__(\w+)__', file)
        if match:
            list_files.append(os.path.abspath(os.path.join(dirname, file)))
    return list_files


def copy_to(path, files):

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("This path exists")

    for file in files:
        shutil.copy(file, path)


def zip_to(path, dest_zip):
    paths = list(path)
    command = "zip -j {} {}".format(dest_zip, ' '.join(paths))
    print("Command I am going to do: ")
    print(command)
    os.system(command)


def zip_to_two(paths, zip_path):
    command = ["zip", "-j", zip_path]
    command.extend(paths)
    print("command I am going to do: {}".format(' '.join(command)))
    subprocess.check_output(command)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='src dir to look for local files')
    ns = parser.parse_args(args)
    all_paths = get_special_paths(ns.fromdir)

    if ns.todir:
        copy_to(ns.todir, all_paths)

    if ns.tozip:
        zip_to(all_paths, ns.tozip)

    if not ns.todir and not ns.tozip:
        print('\n'.join(all_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
