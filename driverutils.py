from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import getpass

def go4ever():
    """Solution to make usage of CTRL + C for pausing execution"""
    try:
        while(True):
            print('running')
            sleep(10)
    except:
        a=input('stop? (yes/no)')
        if a!='yes':
            go4ever()

def get_element(driver, xpath, attempts=5, _count=0):
    try:
        element = driver.find_element_by_xpath(xpath)
        return element
    except Exception as e:
        if _count<attempts:
            print("Attempt {}".format(_count))
            print("Error: {}".format(e))
            sleep(1)
            get_element(driver, xpath, attempts=attempts, _count=_count+1)
        else:
            print("Raising error after {} attempts".format(attempts))
            return driver.find_element_by_xpath(xpath)

def click(driver, xpath, attempts=5, _count=0):
    try:
        driver.find_element_by_xpath(xpath).click()
    except Exception as e:
        if _count<attempts:
            print("Attempt {}".format(_count))
            print("Error: {}".format(e))
            sleep(1)
            click(driver, xpath, attempts=attempts, _count=_count+1)
        else:
            print("Raising error after {} attempts".format(attempts))
            driver.find_element_by_xpath(xpath).click()


def wait_until(driver, keywords=None, timeout_count=10):
    count = 0
    if keywords is None:
        sleep(timeout_count)
        return
    while not all(word in driver.page_source for word in keywords):
        print("Waiting until the keywords {} are found in the source page".format(keywords))
        sleep(2)
        count+=1
        if count>timeout_count:
            print("!!!! Exceeded timeout")
            break

def wait_until_beta(driver, keywords, negative_keywords=[], timeout_count=2500):
    count = 0
    page_source = driver.page_source
    print("Waiting until the keywords {} are found in the source page and {} disappear".format(keywords, negative_keywords))
    sleep(1)
    while not all(word.lower() in page_source.lower() for word in keywords) or any(nword in driver.page_source for nword in negative_keywords):   
        count+=1
        sleep(1)
        if count>timeout_count:
            print("Exceeded timeout")
            break
    print("Found it!")

def _login(driver, auth_link, username, password, xpaths, page_kws=None):
    driver.get(auth_link)
    wait_until(driver)
    email = driver.find_element_by_xpath(xpaths[0])
    email.send_keys(username)
    passw = driver.find_element_by_xpath(xpaths[1])
    passw.send_keys(password)
    signin = driver.find_element_by_xpath(xpaths[2])
    signin.click()
    wait_until(driver)
    print('Done!')

def _setup_driver(chrome_options=None):
    print('Loading...')
    if chrome_options is None:
        chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def authenticated_driver(link, username=None, password=None, user_xpath=None, pass_xpath=None, confirm_xpath=None, wait_kws=None, chrome_options=None):
    print("Check username and passwords are inputed")
    if username is None:
        username = raw_input("Username: ")

    if password is None:
        password = getpass.getpass('\nPassword: ')

    print("Setup driver")
    driver = _setup_driver(chrome_options)

    xpaths = [user_xpath, pass_xpath, confirm_xpath]
    _login(driver, link, username, password, xpaths, page_kws=wait_kws)

    return driver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class ChromeBot:
    def __init__(self):
        self.driver = self._setup_driver()

    @staticmethod
    def _setup_driver():
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        '''Safe get_element method with multiple attempts'''
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            if _count<attempts:
                sleep(1)
                print(f'Attempt {_count}')
                self._get_element(xpath, attempts=attempts, _count=_count+1)
            else:
                print("Element not found, raising error")

    def click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.click()
        el.send_keys(message)



def main():
    pass

if __name__ == '__main__':
    main()
