import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("user-data-dir=scraper")

        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
        self.data = {}

    def scraper(self, number: int):
        driver = self.driver
        driver.get("https://www.kaggle.com/lava18/google-play-store-apps")
        time.sleep(10)

        for i in range(1, number):
            temp = []
            application_name_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[7]/span[{}]/div/div[1]'.format(
                str(i))
            driver.execute_script(
                '''document.evaluate("{path}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''.format(
                    path=application_name_xpath))
            application_name = driver.find_element_by_xpath(xpath=application_name_xpath).text

            category_the_app_belongs_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[7]/span[{}]/div/div[2]'.format(
                str(i))
            category_the_app_belongs = driver.find_element_by_xpath(xpath=category_the_app_belongs_xpath).text

            overall_user_rating_of_the_app_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[7]/span[{}]/div/div[3]'.format(
                str(i))
            overall_user_rating_of_the_app = driver.find_element_by_xpath(
                xpath=overall_user_rating_of_the_app_xpath).text

            number_of_user_reviews_for_the_app_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[7]/span[{}]/div/div[4]'.format(
                str(i))
            number_of_user_reviews_for_the_app = driver.find_element_by_xpath(
                xpath=number_of_user_reviews_for_the_app_xpath).text

            size_of_the_app_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[' \
                                    '2]/div/div[3]/div[7]/span[{}]/div/div[5]'.format(
                str(i))
            size_of_the_app = driver.find_element_by_xpath(xpath=size_of_the_app_xpath).text

            number_of_user_downloads_installs_for_the_app_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[' \
                                                                  '2]/div[3]/div[2]/div/div[2]/div/div[3]/div[' \
                                                                  '7]/span[{}]/div/div[6]'.format(
                str(i))
            number_of_user_downloads_installs_for_the_app = driver.find_element_by_xpath(
                xpath=number_of_user_downloads_installs_for_the_app_xpath).text

            paid_or_free_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[' \
                                 '3]/div[7]/span[{}]/div/div[7]'.format(
                str(i))
            paid_or_free = driver.find_element_by_xpath(xpath=paid_or_free_xpath).text

            price_of_the_app_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[2]/div/div[' \
                                     '2]/div/div[3]/div[7]/span[{}]/div/div[8]'.format(
                str(i))
            price_of_the_app = driver.find_element_by_xpath(xpath=price_of_the_app_xpath).text

            age_group_the_app_is_targeted_at_children_mature_adult_xpath = '/html/body/main/div[1]/div/div[5]/div[' \
                                                                           '2]/div[2]/div[3]/div[2]/div/div[' \
                                                                           '2]/div/div[3]/div[7]/span[{}]/div/div[' \
                                                                           '9]'.format(
                str(i))
            age_group_the_app_is_targeted_at_children_mature_adult = driver.find_element_by_xpath(
                xpath=age_group_the_app_is_targeted_at_children_mature_adult_xpath).text

            an_app_can_belong_to_multiple_genres_xpath = '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div[3]/div[' \
                                                         '2]/div/div[2]/div/div[3]/div[7]/span[{}]/div/div[10]'.format(
                str(i))
            an_app_can_belong_to_multiple_genres = driver.find_element_by_xpath(
                xpath=an_app_can_belong_to_multiple_genres_xpath).text

            temp.append(category_the_app_belongs)
            temp.append(overall_user_rating_of_the_app)
            temp.append(number_of_user_reviews_for_the_app)
            temp.append(size_of_the_app)
            temp.append(number_of_user_downloads_installs_for_the_app)
            temp.append(paid_or_free)
            temp.append(price_of_the_app)
            temp.append(age_group_the_app_is_targeted_at_children_mature_adult)
            temp.append(an_app_can_belong_to_multiple_genres)

            self.data[application_name] = temp


sc = Scraper()
sc.scraper(number=200)
for key, value in sc.data.items():
    print(key, value)
sc.driver.close()
