#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   5up3rc
# datetime: 2015-02-10 16:27
#**********************************

from urlparse import urlparse
import hashlib
hash_size = 199999

class UrlSimilar(object):
    """docstring for UrlSimilar"""
    def __init__(self, url):

        self.url = url

    def UrlSimilar(self):
        url = self.url
        tmp = urlparse(url)
        scheme = tmp.scheme
        netloc = tmp.netloc
        path = tmp.path
        query_list = tmp.query.split('&')

        '''计算路径中的文件后缀'''
        if len(path.split('/')[-1].split('.')) > 1:
            tail = path.split('/')[-1].split('.')[-1]
        elif len(path.split('/')) == 1:
            tail = path
        else:
            tail = '1'
        tail = tail.lower()
        path_length = len(path.split('/')) - 1
        path_value = 0
        path_list = path.split('/') + [tail]
        query_length = len(query_list) - 1
        quert_value = 0
        for i in range(query_length + 1):
            if query_length - i == 0:
                quert_value += hash(query_list[query_length - i].split('=')[0])%98765
            else:            
                quert_value += hash(query_list[query_length - i].split('=')[0])*(10 ** (i+1))

        for i in range(path_length + 1):
        	if path_length - i == 0:
        		path_value += hash(path_list[path_length - i])%98765
        	else:            
        		path_value += hash(path_list[path_length - i])*(10 ** (i+1))
        netloc_value = hash(hashlib.new("md5", netloc).hexdigest())%hash_size
        url_value = hash(hashlib.new("md5", str(quert_value + path_value + netloc_value)).hexdigest())%hash_size
        
        return url_value