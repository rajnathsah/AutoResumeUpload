import os
from driver import chromedriver
import logging
from time import strftime
import configparser

from encrdecr import decr_passwd
from naukri import naukri
from configgen import GUI

logfile = r'ResumeUploader_{}.log'.format(strftime('%Y_%m_%d_%H.%M.%S'))    
logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG)
logger = logging.getLogger(__name__)
#logging.disable()

if __name__ =='__main__':
    # check if chromedriver exist else download latest version
    cur_dir_path=os.getcwd()
    logger.info('Current working directory - {}'.format(cur_dir_path))
    path_to_driver=os.path.join(cur_dir_path,'chromedriver.exe')

    try:
        if os.path.isfile(path_to_driver):
            pass
        else:
            chrome_release = chromedriver.get_chrome_driver_release()
            chromedriver.download_driver(chrome_release)
    except Exception as ex:
        logger.error('Error in finding/downloading chromedriver : {}-{}'.format(path_to_driver,ex))
        raise    
    
    # check if config file exist else prompt for creating it
    config_file = os.path.join(os.getcwd(), 'config.ini')
    try:
        if os.path.isfile(config_file):
            pass
        else:
            # create config file
            guiFrame = GUI()    
            guiFrame.mainloop()
            
    except Exception as ex:
        logger.error('Error in finding/creating config file : {}-{}'.format(config_file, ex))
    
    # read config file for parameters
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        resume = config['resume']['filename']        
    except Exception as ex:
        logger.error('Error in reading configuration file: {}'.format(ex))
        raise
    
    # validate resume file path
    cur_dir_path=os.getcwd()
    logger.info('Current working directory - {}'.format(cur_dir_path))
    path_to_resume=os.path.join(cur_dir_path,resume)
    try:
        if os.path.isfile(path_to_resume):
            pass
        else:
            raise
    except Exception as ex:
        logger.error('Error in locating resume file : {}'.format(path_to_resume))
        raise
    
    logger.info('Path to cv- {}'.format(path_to_resume))    
    
    '''read naukri.com username and password and account flag
    In case value is not set then set it with default setting account flas as N
    '''
    try:
        naccount = config['naukri']['account']
        nusername = config['naukri']['username']
        npassword = decr_passwd(config['naukri']['password'])   
    except Exception as ex:
        naccount = 'No'
        nusername = None
        npassword = None
         
    if naccount == 'Yes' and nusername is not None and npassword is not None:
        naukri.loginUpload(nusername, npassword, path_to_resume)