#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


import authentication
import getpass
STR1 = 'Incorrect username or password. You have '


def login(username, maxattempts=2):
    """long in"""
    i = 1
    var = False
    while i <= maxattempts:
        myval = getpass.getpass()
        if authentication.authenticate(username, myval):
            var = True
        else:
            print STR1 + str((maxattempts - i)) + ' attempts left'
        i += 1
    return var
