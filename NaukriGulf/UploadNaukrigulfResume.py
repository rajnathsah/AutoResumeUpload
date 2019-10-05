from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import os
import logging
import configparser


logfile = r'NaukriGulf_{}.log'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))
updateimage = r'NaukriGulf_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.info('Start')

opts=Options()
opts.headless=False

try:
    config=configparser.ConfigParser()
    config.read('gulfconfig.ini')
    username=config['login']['username']
    password=config['login']['password']
    resume=config['resume']['filename']
except Exception as ex:
    logger.error('Error in reading configuration file: {}'.format(ex))
    raise
    
cur_dir_path=os.getcwd()
logger.info('Current working directory - {}'.format(cur_dir_path))
path_to_resume=os.path.join(cur_dir_path,resume)
try:
    if os.path.isfile(path_to_resume):
        pass
    else:
        raise
except Exception as ex:
    logger.error('Error in locating resume file : {} - {}'.format(path_to_resume,ex))
    raise
    
logger.info('Path to cv- {}'.format(path_to_resume))

try:    
    browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
    browser.get('https://www.naukrigulf.com/ni/nilogin/user/login')
    browser.maximize_window()
    
    time.sleep(5)
    
    usernameField = browser.find_element_by_id("loginusername")    
    usernameField.send_keys(username)
    
    passwordField=browser.find_element_by_id('loginpassword')
    passwordField.send_keys(password) 
    
    clickbtn=browser.find_element_by_id("gnbLogInSubmit").click()
    time.sleep(5)
    
    browser.find_element_by_xpath('//*[@id="myHome"]/div[2]/div[2]/div[2]/div[1]/div[2]/div/a').click()
    time.sleep(5)
    
    browser.find_element_by_xpath('//*[@id="qLinks"]/ul/li[8]/a').click()
    time.sleep(2)
    
    browser.find_element_by_xpath('//*[@id="cvUploadForm"]/div/resman-uploader/div/div/div[1]/div/div/div/span/input').send_keys(path_to_resume)
    time.sleep(5)
    browser.save_screenshot(updateimage)
    logger.info('Screen shot of resume upload : {}'.format(updateimage))
    logger.info('Finish')
    browser.quit()
except Exception as ex:
    logger.error('Error in resume upload : {}'.format(ex))
    raise
finally:
    browser.quit()