from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('C:/Users/Silent_introder/Downloads/chromedriver_win32/chrome/chromedriver') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"YOUR-TARGET-GROUP"'

# Replace the below string with your own message 
string = "YOUR-TARGET-MESSAGE"


x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 

input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(2): 
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) 
