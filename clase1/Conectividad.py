#!/usr/bin/env python
import urllib2

try:
    f = urllib2.urlopen("http://yoelfme.github.io/")
    print f.read()
    f.close()
except HTTPError, e:
    print "Error!!"
    print e.code
except URLError, e:
    print "Error!!"
    print e.code
