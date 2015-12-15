#!/usr/bin/env python

import json
import os


class Loader(object):
    """"
        this class will handle all functions related to working with a posts.json,
        open, save, create, delete, modify, and what have you,
        version 0.2
    """

    def __init__(self, path):
        self.path = self.path_check(path)
        self.get_vars()

    def path_check(self, path):
        # check to see if file is there, if not, make one.
        file = os.path.isfile(path)
        if file is True:
            return path
        else:
            self.make_new(path)
            return path

    def make_new(self, path):
        with open(path, 'w') as outFile:
            json.dump({"meta": {"version": 0.02, 'author': 'auto gen beta'}, 'posts':[]}, outFile,
                      indent=4, separators=(',', ': '))
        return 0

    def get_vars(self):
        with open(self.path) as inFile:
            in_vars = json.load(inFile)

        self.version = in_vars['meta']['version']
        self.author = in_vars['meta']['author']

        self.posts = in_vars['posts']
        return 0

    def save_file(self):
        with open(self.path, 'w') as outFile:
            json.dump({"meta": {"version": self.version, 'author': self.author}, 'posts': self.posts,
                       }, outFile, indent=4, separators=(',', ': '))
        return 0