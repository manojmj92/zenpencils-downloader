#-------------------------------------------------------------------------------
# Name:        zenpencils downloader
# Purpose:
#
# Author:      hp
#
# Created:
# Copyright:   (c)manojmj.com
# Licence:
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import urllib2
import os
import sys
import time

dir = os.path.dirname(os.path.abspath(__file__))
zendir = os.path.join(dir, "ZenComics")

if not os.path.exists(zendir):
        os.makedirs(zendir)

count = 0;
while(1):
    main_url = "http://zenpencils.com/comic/" + str(count)
    headers = {'User-agent': 'Mozilla/5.0'}

    main_url_opener = urllib2.Request(main_url, None, headers)
    try:
        main_url_response = urllib2.urlopen(main_url_opener).read()

        main_url_soup = BeautifulSoup(main_url_response,'html.parser')
        images = main_url_soup.findAll("div", {"id": "comic"})
        image = images[0].img['src']
        name = image.split('/')[-1]
        with open(os.path.join(zendir, name), 'wb') as f:
            f.write(urllib2.urlopen(image.encode('utf-8')).read())
    except urllib2.HTTPError:
        print "Complete: " + str(count) + " images downloaded."
        break
    count += 1
