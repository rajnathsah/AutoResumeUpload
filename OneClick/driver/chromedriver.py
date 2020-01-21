import requests, zipfile, io
 
def get_chrome_driver_release():
    '''
    Function returns latest chrome driver release number 
    '''
    result = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
    return result.text


def download_driver(version):
    '''
    Download given version of chrome driver and extract the zip file
    '''
    driver_download_url= 'https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip'.format(version)
    chrome_req = requests.get(driver_download_url)
    driver_zipfile = zipfile.ZipFile(io.BytesIO(chrome_req.content))
    driver_zipfile.extractall()
