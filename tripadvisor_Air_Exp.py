from selenium import webdriver
from bs4 import BeautifulSoup as soup
from datetime import datetime
from dateutil.parser import parse
import time 
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def one_page():
	print(driver.current_url)
	# MORE & SHOW LESS SELUTION
	#more = driver.find_element_by_class_name('_36B4Vw6t')
	more = WebDriverWait(driver,1000).until(EC.element_to_be_clickable((By.CLASS_NAME, '_36B4Vw6t')))
	more.click()
	#time.sleep(5)
	# RATING
	r=driver.find_elements_by_xpath("//div[@class='location-review-review-list-parts-RatingLine__bubbles--GcJvM']/span[1]")
	rate=[]
	for i in r:
		rate.append(int(i.get_attribute("class")[24]))
	labels=[]
	for i in rate:
		if i == 1 or i == 2:
			labels.append('neg')
		elif i == 5 or i == 4: 
			labels.append('pos')
		else:
			labels.append('obj')
			

	# REVIEW
	rev=driver.find_elements_by_xpath("//q[@class='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC']/.//span")	
	print("Reviews")
	print(len(rev))

	for i in range(0,len(rev)): 
		global count
		file2 = open('F:/Dropbox/DS/NewAirlines2019,Dec/AirFrance/text/'+ labels[i]+ str(count) +'.txt','w')# create a folder for the data
		try:
			#text is a property of the WebElement class
			file2.write (re.sub('\s+',' ',rev[i].text).strip())
		except Exception:
			pass
		file2.close()
		count += 1 
		# FOR BERT Training 
		file = open('F:/Dropbox/DS/NewAirlines2019,Dec/AirFrance/training/training.txt','a')# create a folder for the data
		try:
			#text is a property of the WebElement class
			if labels[i]=='neg' or labels[i]=='pos':
				file.write(re.sub('\s+',' ',rev[i].text).strip()+'\t'+labels[i].upper())
				file.write('\n')
		except Exception:
			pass
		file.close()
		
count = 1	
driver = webdriver.Firefox()
reCounter = 5
driver.get('https://www.tripadvisor.com.au/Airline_Review-d8729003-Reviews-Air-France')
n=10470 # n is the number of reviews on the website 
while reCounter <= n: 
	one_page()
	next = WebDriverWait(driver,1000).until(EC.element_to_be_clickable((By.LINK_TEXT , 'Next')))
	next.click();
	#driver.find_element_by_link_text("Next").click();
	reCounter += 5
