import time
import logging
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Generate log file name
updateimage = r'monsterindia_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logger = logging.getLogger(__name__)

logger.info('MonsterIndia Start')

opts=Options()
opts.headless=False


def loginUpload(username, password, path_to_resume):
    '''open browser, login and upload resume
    '''
    try:
        browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
        browser.get('https://www.monsterindia.com/rio/login')
        browser.maximize_window()
        
        logger.info('Open url in chrome')
        time.sleep(5)    
        
        usernameField = browser.find_element_by_id("signInName")#('usernameField')    
        usernameField.send_keys(username)
        logger.info('Entered username')
        
        passwordField=browser.find_element_by_id('password')
        passwordField.send_keys(password)
        logger.info('Entered password')
        
        browser.find_element_by_xpath("//*[@id='SignInForm']/div[2]").click()
        time.sleep(10)
        logger.info('Click login and wait for 5 sec')
        
        browser.find_element_by_xpath('//*[@id="stickySidebar"]/div[1]/div/a').click()
        time.sleep(5)
        
        browser.find_element_by_xpath('//*[@id="user-profile-right"]/div/div[2]/div[1]/div/a/i').click()
        time.sleep(5)    
        try:
            browser.find_element_by_xpath('//*[@id="resume"]').send_keys(path_to_resume)                
            time.sleep(5)                
            browser.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3) .pt10").click()                
            time.sleep(5)
            browser.save_screenshot(updateimage)
            logger.info('Uploaded')        
        except Exception as ex:        
            logger.error('Error in login and cv upload: {}'.format(ex))
            raise
                
    except Exception as ex:    
        logger.error('Error in monsterindia cv upload- {}'.format(ex))
    finally:
        browser.quit()
        logger.info('MonsterIndia End')
        logger.info('MonsterIndia End')    