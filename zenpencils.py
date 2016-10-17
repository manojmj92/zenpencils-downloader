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

dir = os.path.dirname(os.path.abspath(__file__))
zendir = dir +"\\ZenComics"

if not os.path.exists(zendir):
        os.makedirs(zendir)

for url_range in range(1,145):

    main_url = "http://zenpencils.com/comic/" + str(url_range)
    headers = {'User-agent': 'Mozilla/5.0'}

    main_url_opener = urllib2.Request(main_url, None, headers)
    main_url_response = urllib2.urlopen(main_url_opener).read()

    main_url_soup = BeautifulSoup(main_url_response,'html.parser')


    for comiclink in main_url_soup.find_all('img'):
        all_links = comiclink.get('src')

        if all_links.split('/')[3] == 'comics':
            filename = all_links.split('/')[4]
            res = urllib2.Request(all_links,None,headers)
            img= urllib2.urlopen(res).read()
            with open(zendir+"\\"+filename,"wb")as image:
                    image.write(img)
            print "Completed Download of  :"+filename
            break

