from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys


s_no=input().split(' ')

driver = webdriver.Chrome()

'''
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
'''

driver.get('https://landrecords.karnataka.gov.in/service2/RTC.aspx')

district = Select(driver.find_element_by_id('ctl00_MainContent_ddlCDistrict'))
district.select_by_visible_text('BANGALORE URBAN')

time.sleep(5)
taluk = Select(driver.find_element_by_id('ctl00_MainContent_ddlCTaluk'))
taluk.select_by_visible_text('BANGALORE-SOUTH')

time.sleep(5)
hobli = Select(driver.find_element_by_id('ctl00_MainContent_ddlCHobli'))
hobli.select_by_visible_text('UTTARAHALLI -4')

time.sleep(5)
village = Select(driver.find_element_by_id('ctl00_MainContent_ddlCVillage'))
village.select_by_visible_text('HOSAKEREHALLI')

time.sleep(2)
survey = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_txtCSurveyNo"]')
i=1

for surveynum in s_no:
	time.sleep(2)
	if(i!=1):
		survey = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_txtCSurveyNo"]')
		survey.clear()
	else:
		i+=1
	
	time.sleep(2)
	survey = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_txtCSurveyNo"]')			
	surveynum=int(surveynum)
	survey.send_keys(surveynum)
	
	time.sleep(2)
	gobtn = driver.find_element_by_id('ctl00_MainContent_btnCGo')
	gobtn.click()
	gobtn.click()

	time.sleep(13)
	surnoc = Select(driver.find_element_by_id('ctl00_MainContent_ddlCSurnocNo'))
	surnoc.select_by_index(1)

	time.sleep(3)
	hissa = Select(driver.find_element_by_id('ctl00_MainContent_ddlCHissaNo'))
	hissa.select_by_index(1)


	time.sleep(3)
	period = Select(driver.find_element_by_id('ctl00_MainContent_ddlCPeriod'))
	period.select_by_index(1)

	time.sleep(3)
	year = Select(driver.find_element_by_id('ctl00_MainContent_ddlCYear'))
	year.select_by_index(1)

	time.sleep(2)

	fetchbtn = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_btnCFetchDetails"]')
	fetchbtn.click()

	time.sleep(2)
	tabletxt = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_div1"]/div/div[2]')
	text = tabletxt.get_attribute('innerHTML')
	#print(text.strip())
	f = open("ymail.html", "a")
	f2 = open("ymail.txt", "a")
	f2.write(text)
	f.write(text)
	f.close()
	f2.close()
	


	'''st=u'ವಿಜಯ್ ಡಿಸೋಜ'
	print(st)

	if(driver.getPageSource().contains(st))
	{
		f = open("ymail.txt", "w")
		f.write("1")
		f.close()
	}

	else
	{
		f = open("ymail.txt", "w")
		f.write("0")
		f.close()
	}
'''
