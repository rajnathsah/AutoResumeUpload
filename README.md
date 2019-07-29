# Automate resume update on Naukri.com using python

### Requirements

1. [Python 3.x](https://www.python.org/)
2. [Selenium](https://www.seleniumhq.org/)
3. [Chrome Webdriver](https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_win32.zip)
4. [Chrome browser](https://www.google.com/chrome/)

Selenium can be installed using 
```
pip install selenium
```
or using requirement file to install all dependencies
```
pip install -r requirements.txt
```
Chrome webdriver can be download from here or from above given link.

#### Update python script for auto upload resume

1. Open config.ini file using any text editor and update Naukri.com login id, password and resume file name and save it.
2. Run the update_naukri_resume.py from command prompt using 
```
python update_naukri_resume.py
```
3. One can also run using resumeupdate.bat file by double click.
4. It will generate log file and screen shot for verification and debugging purpose.
5. You can schedule it on any server or computer to update profile daily.
6. Happy job hunting
