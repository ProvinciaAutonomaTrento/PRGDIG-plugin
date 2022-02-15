# -*- coding: utf-8 -*-

class CallBackInfo:
    def __init__(self, objectType, oid, status, progress = None):
        self.objectType = objectType
        self.oid = oid 
        self.status = status
        self.progress = progress
        self.errors = None
        self.error_table = None
        self.fatal = False