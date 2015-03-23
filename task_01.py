#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

players = ['heidy', 'david', 'lourdes']
tup = ()
temp = []
def get_matches(players):
    for index, item in enumerate(players):
        for index1, item1 in enumerate(players):
            tup = item, item1
        temp.append(tup)
    
    return temp
print get_matches(players)
    
