#!/usr/bin/env python
# -*- coding: utf-8 -*-

# all(iterable)
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# any(iterable)
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

#Return an enumerate object
def enumerate(sequence, start=0):
    n = start
    for element in sequence:
        yield n, element
        n += 1
