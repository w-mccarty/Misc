import feedparser
import requests
import sys
import os
import re
import time
import datetime
from datetime import datetime
import pytz
from unidecode import unidecode
import eventlet
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

################################ CUSTOMIZEE THESE AS NEEDED ###############################
#timezone
tzone = 'US/Eastern'
#location of RSS html files
htmlDir = "/var/www/html/rss/"

#this script should be scheduled to run with cron hourly, use the scheduler to set the hours that each url is pulled
#referenced in urls[x][0]  
#ie: scheduler[0] = every day at 6am, scheduler[3] = hourly starting at 6am...
#
scheduler = [
'06',
'06,12',
'06,08,10,12,14,16,18,20,22',
'06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23'
]

#to find YOUTUBE channel ID RSS url
#   1. Open channel, right click view source
#   2. Ctrl + F "https://www.youtube.com/channel/" to find channel ID
#   3. Add ID to end of "https://www.youtube.com/feeds/videos.xml?channel_id="
#
urls = [
[3,'Hacker News Frontpage','https://hnrss.org/frontpage'],
[3,'Reddit Technology','https://www.reddit.com/r/technology/hot.rss']
]
############################################################################################

timezone = pytz.timezone(tzone)
localnow = datetime.now(timezone).strftime('%H')
urllen = len(urls)
urlrange = range(0,urllen)
for x in urlrange:
	if str(localnow) in (scheduler[(urls[x][0])]):
		try:
			fname = urls[x][1].replace(" ","")
			rfile = str(htmlDir) + str(fname) + ".html"
			with eventlet.timeout.Timeout(5):
				response = requests.get(urls[x][2])
			parseurl = str(urls[x][2])
			d = feedparser.parse(parseurl)
			dl = []
			for index, post in enumerate(d.entries, start = 0):
				indexval = index
				v1 = post.link
				v2 = unidecode(post.title)
				v3 = parse(post.published)
				v3a = str(v3)[5:10] #mm-dd
				v3b = str(v3).replace("-","").replace(" ","").replace(":","").replace("+","")
				v4 = datetime.now().astimezone().replace(microsecond=0).isoformat()
				v4 = parse(v4)
				delta = relativedelta(v4 v3)
				if ((delta.years < 0) or (delta.months < 0) or (delta.days < 0) or (delta.hours < 0)):
					pnv = ["dfeed_fut","tfeed_fut"]
				elif ((delta.years == 0) and (delta.months == 0) and (delta.days == 0) and (delta.hours < 2)):
					pnv = ["dfeed_now","tfeed_now"]
				elif ((delta.years == 0) and (delta.months == 0) and (delta.days == 0)):
					pnv = ["dfeed_day","tfeed_day"]
				else:
					pnv = ["dfeed_old","tfeed_old"]
				v5 = ("<div id=\"fdiv_" + str(x) + "_" + v3b + str(indexval) + "\" class=\"" + pnv[0] + " rssdiv\"><div class=\"" + pnv[1] + " rssdate\" id=\"rssdate_" + str(x) + "_" + str(indexval) + "\">" + v3a + "</div><div class=\"" + pnv[1] + " rsslink\" id=\"rsslink_" + str(x) + "_" + str(indexval) + "\"><a href=\"" + v1 + "\" target=\"_blank\">" + v2 + "</a></div><br></div>")
				dl.append(v5)
			dl2 = sorted(dl, reverse=True)
			v6= str(datetime.today().strftime('%H:%M,%m-%d-%Y'))
			with open(rfile, mode="wt", encoding="utf-8") as myfile:
				myfile.write("<div id=\"rssheadlink\">" + str(urls[x][1]) + "</div><div id=\"rssheadupdate\">Last updated: " + v6 + "</div>")
				myfile.write('\n'.join(dl2))
		except requests.exceptions.ReadTimeout:
			print("READ TIMED OUT -" + urls[x][2])
		except requests.exceptions.ConnectionError:
			print("CONNECT ERROR -" + urls[x][2])
		except eventlet.timeout.Timeout:
			print("TOTAL TIMEOUT -" + urls[x][2])
		except requests.exceptions.RequestException:
			print("OTHER REQUESTS EXCEPTION -" + urls[x][2] + "error")
	else:
		print("time scope incorrect - desired time" + str(scheduler[(urls[x][0])]))
