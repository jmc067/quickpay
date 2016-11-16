from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re    

# Instantiate Firefox Webdriver instance
driver = webdriver.Firefox()
driver.get("https://top.cbr.nl/top/")

# Get Page Source
src = driver.page_source

# Check IFF System is open
text_found = re.search(r'Het systeem is momenteel gesloten.', src)
if text_found==None:
	print "Text not Found.  System is open"
else:
	print "Text found.  System is closed"

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()