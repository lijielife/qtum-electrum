#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
"""
__author__ = 'CodeFace'
"""
from . import qtum
from .storage import ModelStorage


class SmartContracts(ModelStorage):
    def __init__(self, storage):
        ModelStorage.__init__(self, 'smart_contracts', storage)

    def _validate(self, data):
        for k, v in list(data.items()):
            if k == self.name:
                return self._validate(v)
            if not qtum.is_hash160(k):
                data.pop(k)
        return data
