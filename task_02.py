#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


import authentication
import getpass


def login(username, maxattempts = 2):
    i=1
    var = False
    while i <= maxattempts:
      
        
        myval = getpass.getpass()
        if authentication.authenticate(username, myval):
            var = True
        else:
            print 'Incorrect username or password. You have ' + str((maxattempts - i)) + ' attempts left'
        i+=1
    return var
