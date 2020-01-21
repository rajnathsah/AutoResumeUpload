from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import logging


updateimage = r'naukrigulf_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logger = logging.getLogger(__name__)

logger.info('NaukriGulf Start')

opts=Options()
opts.headless=False

def loginUpload(username, password, path_to_resume):
    '''Open naukrigulf.com, login and upload resume
    '''
    try:    
        browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
        browser.get('https://www.naukrigulf.com/ni/nilogin/user/login')
        browser.maximize_window()
        
        time.sleep(5)
        
        usernameField = browser.find_element_by_id("loginusername")    
        usernameField.send_keys(username)
        
        passwordField=browser.find_element_by_id('loginpassword')
        passwordField.send_keys(password) 
        
        browser.find_element_by_id("gnbLogInSubmit").click()
        time.sleep(5)
        
        browser.find_element_by_xpath('//*[@id="myHome"]/div[2]/div[2]/div[2]/div[1]/div[2]/div/a').click()
        time.sleep(5)
        
        browser.find_element_by_xpath('//*[@id="qLinks"]/ul/li[8]/a').click()
        time.sleep(2)
        
        try:
            browser.find_element_by_xpath('//*[@id="cvUploadForm"]/div/resman-uploader/div/div/div[1]/div/div/div/span/input').send_keys(path_to_resume)
            time.sleep(5)
            browser.save_screenshot(updateimage)
            logger.info('Uploaded')        
            browser.quit()
        except Exception as ex:
            logger.error('Error in cv upload: {}'.format(ex))
            raise
    
    except Exception as ex:
        logger.error('Error in resume upload : {}'.format(ex))    
    finally:
        browser.quit()
        logger.info('NaukriGulf End')