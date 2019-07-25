from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import os
import logging

logfile = r'update_naukri_profile_{}.log'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))
updateimage = r'update_naukri_profile_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start')

opts=Options()
opts.headless=False

cur_dir_path=os.getcwd()
logger.info('Current working directory - {}'.format(cur_dir_path))
path_to_cv=os.path.join(cur_dir_path,"<resume>")
logger.info('Path to cv- {}'.format(path_to_cv))

#assert opts.headless
try:
    browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
    browser.get('https://www.naukri.com/nlogin/login?URL=http://www.naukri.com/mnjuser/profile?id=&altresid')
    browser.maximize_window()
    
    logger.info('Open url in chrome')
    time.sleep(5)    
    
    username = browser.find_element_by_id('usernameField')
    username.send_keys('<username>')
    logger.info('Enter username')
    
    password=browser.find_element_by_id('passwordField')
    password.send_keys('<password>')
    logger.info('Enter password')
    
    clickbtn=browser.find_element_by_xpath("//*[@id='loginForm']/div[5]/div/button").click()
    time.sleep(5)
    logger.info('Click login and wait for 5 sec')
    
    browser.find_element_by_id('attachCV').send_keys(path_to_cv)
    time.sleep(5)
    browser.save_screenshot(updateimage)
    logger.info('Upload cv and wait for 5 sec')
    
    browser.quit()
except Exception as ex:
    print(ex)
    logger.error('Error in cv upload- {}'.format(ex))
    browser.quit()