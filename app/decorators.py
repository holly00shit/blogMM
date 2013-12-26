#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from threading import Thread

def async(func):
    def wrap(*args, **kwargs):
        thr = Thread(target = func, args = args, kwargs = kwargs)
        thr.start()
    return wrap