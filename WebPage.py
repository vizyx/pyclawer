#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   5up3rc
# datetime: 2015-02-07 01:51
#**********************************


import urllib2
from bs4 import BeautifulSoup
from splinter import Browser
import chardet
import re
import logging
import traceback


log = logging.getLogger('claw.GetPage')

class GetPage():
    '''
    读取到url的htmlsource，解析出该htmlsource中所有href
    '''
    def __init__(self, urltuples):
        self.urltuples = urltuples


    def get_html(self):
        url = self.urltuples[1]
        try:
            #html = urllib2.urlopen(url, timeout=15).read()
            browser = Browser('phantomjs')
            browser.visit(url)
            html = browser.html.encode('UTF-8')
            browser.quit()
        except Exception, e:
            print "error: %s'\n url: %s'" % (e, url)
            log.debug("URL: %s" % url + traceback.format_exc())
 
        else:
            return html