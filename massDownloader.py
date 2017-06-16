from selenium import webdriver
import time as tm

email = "your facebook login email"
password = "your facebook login password"
groupURL = "facebook group's file section URL"
# you must be a member of this group if it is a closed group
"""
Example:
email = "abcdef@xyz.com"
password = "asdf123456"
groupURL = "https://www.facebook.com/groups/StudyAbroad/files/"
"""

br = webdriver.Chrome()
tm.sleep(3)
br.get("https://www.facebook.com/")
tm.sleep(5)
userField = br.find_element_by_id("email")
passField = br.find_element_by_id("pass")
loginButton = br.find_element_by_id("loginbutton")
userField.send_keys(email)
passField.send_keys(password)
loginButton.click()
tm.sleep(5)
br.get(groupURL)
flag = True
cnt = 0
clicked = 0
while flag:
	try:
		tm.sleep(6)
		seeMore = br.find_element_by_class_name('uiMorePagerPrimary')
		seeMore.click()
		cnt = 0
		clicked = clicked + 1
		print "clicked: " + str(clicked) + " times"
	except Exception as e:
		cnt = cnt + 1
		print "failed " + str(cnt) + "times in a row"
		if cnt == 4:
			flag = False
print "Done!"