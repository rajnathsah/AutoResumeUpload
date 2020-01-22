# OneClick resume upload

### Requirements

1. [Python 3.x](https://www.python.org/)
2. [Selenium](https://www.seleniumhq.org/)
3. [Chrome Webdriver](https://chromedriver.chromium.org/)
4. [Chrome browser](https://www.google.com/chrome/)

Selenium can be installed using 
```python
pip install selenium
```
or using requirement file to install all dependencies
```python
pip install -r requirements.txt
```
Chrome webdriver can be download from here or from above given link.

#### Python script and executable for resume upload
* [naukri.com](https://www.naukri.com)
* [naukrigulf.com](https://www.naukrigulf.com)

1. Download content of Naukri folder and chrome driver.
2. Open config.ini file using any text editor and update [naukri.com](https://www.naukri.com) login id, password and resume file name and save it.
3. Run the UploadResume.py from command prompt using 
```python
python UploadResume.py
```
4. One can also run using resumeupdate.bat file by double click.
5. It will generate log file and screen shot for verification and debugging purpose.
6. You can schedule it on any server or computer to update profile daily.
7. Added window executable (created using [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/index.html)) for one click run  
8. UploadResume.exe can be used without installing python and other dependent libraries, In this case you should download dependent config file and chromedriver.exe. Update config file and place your resume in same folder and you are ready for one click resume upload.  
