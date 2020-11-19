from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from logger import get_logger
from time import sleep

logger = get_logger()

DRIVER_PATH = '/Users/alice/PycharmProjects/pythonProject5/chromedriver'
GOOGLE_URL = 'https://google.com'


class Twitter:
    def __init__(self, executable_path: str):
        self.driver = webdriver.Chrome(executable_path=executable_path)

    def parse_account_data(self, person_name: str):
        self._find_necessary_person(username=person_name)
        self._open_twitter_account()
        self._get_information()

    def _find_necessary_person(self, username: str):
        self.driver.get(GOOGLE_URL)
        found_element = self.driver.find_elements_by_xpath('//input[@title="Search"]')
        if found_element:
            found_element[0].send_keys(f'twitter {username}')
            found_element[0].send_keys(Keys.ENTER)

    def _open_twitter_account(self):
        found_page = self.driver.find_elements_by_xpath('//a[contains(@href,"twitter.com")]')
        if found_page:
            found_page[0].send_keys(Keys.ENTER)

    def _get_information(self):
        sleep(5)
        username_block = self.driver.find_elements_by_xpath('//a[contains(@href,"header_photo")]/following-sibling::div/div[2]/descendant-or-self::span')
        name = username_block[1].text
        username = username_block[3].text

        followers_count = self.driver.find_elements_by_xpath('//a[contains(@href,"followers")]')
        followers = followers_count[0].text

        logger.info(f'The account of {name} with user name {username} has {followers}')


if __name__ == '__main__':
    tw = Twitter(executable_path=DRIVER_PATH)
    tw.parse_account_data(person_name='Elon Mask')
    tw.parse_account_data(person_name='Alexey Navalny')
    tw.driver.close()
