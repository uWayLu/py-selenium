from pyvirtualdisplay import Display
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from sys import argv
import json
# import os
import time

# from argvs
from_url = argv[1]
save_dir = argv[2]
# service = Service(executable_path = os.getenv('BROWSER'))
# service = Service(executable_path = r'./bin/chromedriver')

chrome_options = webdriver.ChromeOptions()
appState = {
   'recentDestinations': [
      {
           'id': 'Save as PDF',
           'origin': 'local',
           'account': ''
      }
  ],
   'selectedDestinationId': 'Save as PDF',
   'version': 2,
}
prefs = {
   'printing.print_preview_sticky_settings.appState': json.dumps(appState), 
   'savefile.default_directory': save_dir
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--window-size=1280,720')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("detach", True)

# xvfb
display = Display(visible=0, size=(900, 600))
display.start()

# selenium
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

driver.get(from_url)

# try:
#     myElem = WebDriverWait(driver, delay = 3).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
#     print('ready')
# except TimeoutException:
#     print(r'timeout')
# time.sleep(3)

customjs="""
  var timer = setInterval(() => {
    console.log(window.status)
    if (window.status === 'ready') {
      clearInterval(timer)
      window.print();
    }
  }, 1000);
"""
driver.execute_script(customjs)
print(f'savedir path: {save_dir}')

time.sleep(30)
driver.quit()
display.stop()
