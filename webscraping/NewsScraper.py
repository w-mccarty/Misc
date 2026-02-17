#!/usr/bin/python3

# SETUP #####################################################################################################
#(sudo apt-get install selenium)
from selenium import webdriver
#(sudo apt-get install chromium-chromedriver)
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
import sys
import time
import random
#import for RSS specifically
import feedparser
from unidecode import unidecode
#import eventlet
import re
#import for file operations
import csv
import os
#ignore thrown warnings that can stop the script
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
total = []

# CUSTOM VARIABLES ##########################################################################################

old_csv = "old.csv"
new_csv = "new.csv"
dif_txt = "dif.txt"

enableNonRssScrape = "1" #1 enable scrape of Selenium based sites, 0 to skip
enableRssScrape = "1" #1 enable scrape of RSS feeds, 0 to skip
enableYoutube = "1" #1 enable youtube feed scrape, 0 to skip

enableWriteOut = "1" #if enableWriteOut = 1 writeout, if 0 print to terminal (for testing)

# NON-RSS SCRAPE ############################################################################################
#FUNCTIONS, CUSTOM MUST BE CREATED FOR EACH SITE.  PLEASE EXAMINE THE FORMAT REQUIRED: '"' must be replaced with "#" so that urls won't be broken once list is compiled.  Symbols ,'" MUST be removed.  See example below:
def FUNCTION_URL(soup):
	bc2 = []
	for bc1 in soup.findAll("a"):
		if bc1.parent.name == "h5":
			bc2.append(bc1)
	for i in bc2:
		i1 = str(i) #<a href="https://SAMPLE_SITE.HTML">SAMPLE_TITLE</a>
		i2 = i1.replace('<a href="','<a class=#<SAMPLE_SITE_NAME># href=#')
		i3 = i2.replace('">','#>')
		i4 = i3.replace(',','').replace('"','').replace("'","")
		total.append(i4)

url = [
#["1" (enabled)/"0"(disabled), "URL"]
["1","https://<URL>"]
]

#FOR EACH FUNCTION CREATED ABOVE, LIST THIS OUT UNDER THE functions=[] ARRAY
functions = [
FUNCTION_URL
]

if enableNonRssScrape == "1":
	for h in url:
		try:
			user_agents = [
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
			]
			user_agent = random.choice(user_agents)
			service = Service('/usr/bin/chromedriver')
			options = webdriver.ChromeOptions()
			options.add_argument('--incognito')
			options.add_argument('--headless')
			options.add_argument(f'user-agent={user_agent}')
			options.add_argument("--enable-javascript")
			options.add_argument("--disable-blink-features=AutomationControlled") 
			options.add_experimental_option("excludeSwitches", ["enable-automation"])
			options.add_experimental_option("useAutomationExtension", False)
			driver = webdriver.Chrome(service=service, options=options)
			index = url.index(h)
			if url[index][0] == "1":
				driver.get(url[index][1])
				time.sleep(3)
				soup = BeautifulSoup(driver.page_source, 'html.parser')
				time.sleep(1)
				functions[index](soup)
			driver.quit()
		except WebDriverException as e:
			print("An error occured:", str(e))

# RSS FEED SCRAPE ###########################################################################################
rss_urls = [
#["1" (enabled)/"0"(disabled), "SITE NAME", "URL"]
["1",'<SITE_NAME>','https://<SITE_URL>']
]
if enableRssScrape == "1":
	rss_urlrange = range(0,len(rss_urls))
	for vR in rss_urlrange:
		if rss_urls[vR][0] == "1":
			try:
				response = requests.get(rss_urls[vR][2], timeout=10)
				rss_parseurl = str(rss_urls[vR][2])
				rss_d = feedparser.parse(rss_parseurl)
				rss_dl = []
				for index, rss_post in enumerate(rss_d.entries, start = 0):
					rss_link = str(rss_post.link)
					rss_link = rss_link.replace('"','').replace("'","")
					rss_title = str(unidecode(rss_post.title))
					rss_title = rss_title.replace('"','').replace("'","").replace(",","")
					rss_stringout = ('<a class=#' + rss_urls[vR][1] + '# href=#' + rss_link + '#>' + rss_title + '</a>')
					rss_dl.append(rss_stringout)
				for rss_y in range(0,len(rss_dl)):
					total.append(rss_dl[rss_y])
			except requests.exceptions.ReadTimeout:
				print("READ TIMED OUT -" + rss_urls[vR][2])
			except requests.exceptions.ConnectionError:
				print("CONNECT ERROR -" + rss_urls[vR][2])
			except requests.exceptions.RequestException:
				print("OTHER REQUESTS EXCEPTION -" + rss_urls[vR][2] + "error")

# YOUTUBE FEEDS #############################################################################################
#to find YOUTUBE channel ID RSS url
#	1. Open channel, right click view source
#	2. Ctrl + F "https://www.youtube.com/channel/" to find channel ID
#	3. Add ID to end of "https://www.youtube.com/feeds/videos.xml?channel_id="
YT_urls = [
#["1" (enabled)/"0" (disabled), "CHANNEL_NAME", "URL"]
["1","<CHANNEL_NAME>","https://www.youtube.com/feeds/videos.xml?channel_id=<CHANNEL_ID>"],
]
if enableYoutube == "1":
	YT_urlrange = range(0,len(YT_urls))
	for vY in YT_urlrange:
		if YT_urls[vY][0] == "1":
			try:
				response = requests.get(YT_urls[vY][2], timeout=10)
				YTrss_parseurl = str(YT_urls[vY][2])
				YTrss_d = feedparser.parse(YTrss_parseurl)
				YTrss_dl = []
				for index, YTrss_post in enumerate(YTrss_d.entries, start = 0):
					YTrss_link = str(YTrss_post.link)
					YTrss_link = YTrss_link.replace('"','').replace("'","")
					YTrss_title = str(unidecode(YTrss_post.title))
					YTrss_title = YTrss_title.replace('"','').replace("'","").replace(",","")
					YTrss_stringout = ('<a class=#' + YT_urls[vY][1] + '# href=#' + YTrss_link + '#> &#x1F4FA; ' + YTrss_title + '</a>')
					YTrss_dl.append(YTrss_stringout)
				for YTrss_y in range(0,len(YTrss_dl)):
					total.append(YTrss_dl[YTrss_y])
			except requests.exceptions.ReadTimeout:
				print("READ TIMED OUT -" + YT_urls[vY][2])
			except requests.exceptions.ConnectionError:
				print("CONNECT ERROR -" + YT_urls[vY][2])
			except requests.exceptions.RequestException:
				print("OTHER REQUESTS EXCEPTION -" + YT_urls[vY][2] + "error")

# WRITE OUT #################################################################################################
if enableWriteOut == "1":
	with open(new_csv, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows((item,) for item in total)
	#COMPARE WITH OLD
	arrDiff = [] #array of items not found in old_csv
	with open(old_csv, 'r') as old_csvFile, open(new_csv, 'r') as new_csvFile:
		old_csvArr = old_csvFile.readlines()
		new_csvArr = new_csvFile.readlines()
	fullString = '<br><ul>'
	for line in new_csvArr:
		if line not in old_csvArr:
			old_csvArr.append(line) #old_csv
			arrDiff.append(line) #difference items
			line = line.replace('<a class=#','<a class="').replace('# href=#','" href="').replace('#>','">').replace('\n','')
			line = "<li>" + line + "<br></li>"
			fullString = fullString + line
	fullString = fullString + "</ul>"
	with open(old_csv, 'a', newline='') as Td: #writeout arrDiff
		for line in arrDiff:
			Td.write(line)
	#writeout dif_txt to be used with webhook
	if (len(fullString) <= 20): #if no new articles found
		if os.path.exists(dif_txt):
			os.remove(dif_txt)
	else:
		with open(dif_txt, "w") as f:
			f.write(fullString)
			print(fullString)
	#CLEANUP
	if len(old_csvArr) > 5000: #old_csv if more than X items
		n = 500 #to remove from front
		with open(old_csv, 'r', newline='') as fileCl:
			fileClean = fileCl.readlines()
			fileClean = fileClean[n:]
		with open(old_csv, 'w', newline='') as file:
			for line in fileClean:
				file.write(line)
	os.remove(new_csv)
else: #printout instead of writeout
	for item in total:
		print(item)
#############################################################################################################
