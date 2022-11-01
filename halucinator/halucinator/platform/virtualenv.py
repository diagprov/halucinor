#!/usr/bin/env python

import sys

def virtualenv_detect():

    prefix = getattr(sys, 'prefix', None)
    base_prefix = getattr(sys, 'base_prefix', None)
    real_prefix = getattr(sys, 'real_prefix', None)

    if real_prefix != None:
        base_prefix = real_prefix

    if base_prefix == None or prefix == None:
        raise Exception("Sys module has no prefix or base prefix attribute")

    if prefix != base_prefix:
        return prefix
    else:
        return None
