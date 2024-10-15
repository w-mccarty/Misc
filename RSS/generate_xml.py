#SIMPLE XML RSS GENERATOR
#from csv with the following format: 
#  page.html, title, MM-DD-YY

import csv
import datetime

#VARIABLES
x_title = "" #BLOG NAME
x_title = "" #BLOG URL
x_description = "" #BLOG DESCRIPTION
x_script = '<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel><title>' + x_title + '</title><link>' + x_title + '</link><description>' + x_description + '</description>'
x_file = 'feed.xml' #OUTPUT FILE

#CONVERT DATE FROM MM-DD-YY to TO RSS FORMAT.  WARNING: SCRIPT IGNORES POSTING TIME, USES 00:00:00 GMT FOR SIMPLICITY.
def dateformat(pubDate):
        d_wkday = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][pubDate.weekday()]
        d_day = str(pubDate.day)
        d_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][pubDate.month - 1]
        d_year = str(pubDate.year)
        dtotal = d_wkday + ', ' + d_day + ' ' + d_month + ' ' + d_year + ' 00:00:00 GMT'
        return(dtotal)

with open('test.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                arr.append(row)
arrlength = len(arr)

#GENERATE RSS ENTRIES & COMBINE
if arrlength > 10:
        rval0 = arrlength - 10
xrange = range(rval0, arrlength)
for x in xrange:
        j_articlenumber = str(x)
        j_name = arr[x][1].strip()
        j_date = arr[x][2].strip()
        d_year = int("20" + j_date[6:8])
        d_month = j_date[:2]
        if d_month[:1] == 0:
                d_month = int(d_month[1:2])
        else:
                d_month = int(d_month)
        d_day = j_date[3:5]
        if d_day[:1] == 0:
                d_day = int(d_day[1:2])
        else:
                d_day = int(d_day)
        rssdate = dateformat(datetime.datetime(d_year, d_month, d_day, 00, 00))
        rsslink = x_title + j_name
        x_script = x_script + '<item><title>' + j_name + '</title><link>' + rsslink + '</link><guid>' + rsslink + '</guid><pubDate>' + rssdate + '</pubDate><description>' + j_name + '</desc>

#CLOSE TAGS & WRITE OUT
x_script = x_script + '</channel></rss>'
with open(x_file, mode="wt", encoding="utf-8") as x_filew:
        x_filew.write(x_script)
