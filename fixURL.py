import re
from mechanize import Browser
from bs4 import BeautifulSoup

out = file('all-files'+'.html', 'w')

localURL = "path of the saved static html file"
"""
Example:
localURL = "file:///home/rabi/Home_Drive/Scrape/allfiles.html"
or
localURL = "C://\User\Downloads\allfiles.html"
"""
browser = Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]

try:
	browser.open(localURL)
	# print browser.viewing_html()
	soup = BeautifulSoup(browser.response().read(), "lxml")
	token = "/"
	prefix = "https://www.facebook.com"
	# print "total links found:", len(soup.findAll('a'))
	for link in soup.findAll('a'):
		try:
			if link['target']:
				link['target'] = "_blank"
			if link['href'] and len(link['href']) > 0 and token == link['href'][0]:
				link['href'] = prefix + link['href']
				if link['rel']:
					link['rel'] = None
		except Exception as ee:
			print "..", ee
	out.write(soup.prettify().encode('utf-8'))
except Exception as e:
	print "exception:", e
out.close()