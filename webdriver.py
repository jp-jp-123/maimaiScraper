import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def GetChromeProfilePath():
    if os.name == 'nt':
        return os.path.expandvars(r'C:\Users\Lenovo\AppData\Local\Google\Chrome\User Data')
    else:  # Linux and Mac
        return os.path.expanduser('~/.config/google-chrome/Default')


def OpenChromeDefaultProfile():

    profile_path = GetChromeProfilePath()

    chrome_options = Options()
    chrome_options.add_argument(f'--user-data-dir={profile_path}')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    # driver.get('https://maimaidx-eng.com/maimai-mobile/home/')

    return driver


if __name__ == "__main__":
    OpenChromeDefaultProfile()
