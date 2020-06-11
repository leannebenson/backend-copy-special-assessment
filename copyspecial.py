#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    list_files = []
    path = os.listdir(dirname) #could need to be path_list
    for file_name in path:
        match = re.search(r'__(\w+)__', file_name)
        if match:
            list_files.append(os.path.abspath(os.path.join(dirname, file_name)))
    return list_files


def copy_to(path_list, dest_dir):

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for path in path_list:
        file_name = os.path.basename(path)
        shutil.copy(path, os.path.join(dest_dir, file_name))
    # could also error out if path_list doesnt match up with 
    # path variable from get_special_paths


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
