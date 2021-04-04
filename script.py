import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Purchasable url
# url='https://www.amazon.in/dp/B07GBZ4Q68/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07GBZ4Q68&pd_rd_w=KOxJe&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=kFOWO&pf_rd_r=APARXRJRV46QBRH7PDVQ&pd_rd_r=e3926f42-52d0-4a39-b028-04db5a629459&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRkRCV1FSMEZMWEFBJmVuY3J5cHRlZElkPUEwNzA4MTA2N0c2UllFTDZWU1FQJmVuY3J5cHRlZEFkSWQ9QTA3Nzc1MTMzUTEwNEs0TTNJWTI4JndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

#Not available url
url='https://www.amazon.in/dp/B0895DY6F5/ref=cm_sw_r_wa_apa_glc_fabc_K2YB7HA56B9NXBX5BYQZ'

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/Users/gb/Desktop/prac/automated-buying/chromedriver'
browser = webdriver.Chrome(options = options, executable_path = driver_path)

browser.get(url)


buybutton=False

while not buybutton:

	try:
		addToCartBtn = addButton = browser.find_element_by_id('availability')
		print("Item not available")
		time.sleep(15)
		browser.refresh()
	except:
		addToCartBtn = addButton = browser.find_element_by_id('add-to-cart-button')
		print("Item Available")
		addToCartBtn.click()
		buybutton=True


	



