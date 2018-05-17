#-*- coding: utf-8 -*-
import sys
import json
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

url = "https://api.github.com/repos/kookmin-sw/2018-cap1-2/issues"
issues = json.load(urllib2.urlopen(url))
issues = json.dumps(issues, indent = 4,ensure_ascii=False).encode('utf8')

print(issues)
