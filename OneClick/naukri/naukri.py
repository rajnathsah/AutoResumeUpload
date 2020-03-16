from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import logging

# Generate log file name
updateimage = r'naukri_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logger = logging.getLogger(__name__)

logger.info('Naukri Start')

opts=Options()
opts.headless=False

def loginUpload(username, password, path_to_resume):
    # open browser, login and upload resume
    try:
        browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
        browser.get('https://www.naukri.com/nlogin/login?URL=http://www.naukri.com/mnjuser/profile?id=&altresid')
        browser.maximize_window()
        
        logger.info('Open url in chrome')
        time.sleep(5)    
        
        usernameField = browser.find_element_by_id("usernameField")#('usernameField')    
        usernameField.send_keys(username)
        logger.info('Entered username')
        
        passwordField=browser.find_element_by_id('passwordField')
        passwordField.send_keys(password)
        logger.info('Entered password')
        
        browser.find_element_by_xpath("//*[@id='loginForm']/div[3]/div[3]/div/button[1]").click()
        time.sleep(5)
        logger.info('Click on login and wait for 5 sec')
        
        try:
            browser.find_element_by_id('attachCV').send_keys(path_to_resume)
            time.sleep(5)
            browser.save_screenshot(updateimage)
            logger.info('Uploaded')            
        except Exception as ex:
            logger.error('Error in login and cv upload: {}'.format(ex))
            raise
                
    except Exception as ex:            
        logger.error('Error in cv upload- {}'.format(ex))
    finally:
        browser.quit()
        logger.info('Naukri End')