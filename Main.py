try:
    import os
    import time
    import datetime
    import selenium
    import pandas as pd
    import Config as cfg
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError as err:
    print(f"Import Error.. Need to install {err} Library")
    exit(0)


class ShareMarket():

    def __init__(self):
        """
        Initialize Variables required for application code.
        """
        self.options = webdriver.ChromeOptions()
        self.options.headless = False
        self.WEBDRIVER_EXE_PATH = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe"
        )

    def validate_keys(self, input):
        """
        Validate input string with keywords and return boolean values.

        :param input:
        :return:
        """
        try:
            keywords = [keyword.lower().strip() for keyword in cfg.KEYWORDS]
            flag = False
            for keyword in keywords:
                if keyword in input.lower():
                    flag = True

            return flag
        except Exception as error:
            print(f"Class: ShareMarket, Method: validate_keys(); Error: {error.__str__()}")

    def scrap_stock_details(self, table):
        """
        After getting table tag of each stock, here we are scrapping its all data as per its fields and
        store it in dictionary list to add it in xlsx file.
        Before scrapping data need to check any keyword from list of keywords is present in table text or not.
        :param table:
        :return:
        """
        try:

            flag = self.validate_keys(table.text)

            if flag:
                stock_info = {}
                rows = table.find_elements_by_tag_name('tr')
                #url = table.find_element_by_xpath('//tbody/tr[1]/td[3]/a').get_attribute('href')
                #print("1: ",url)
                cols = rows[0].find_elements_by_tag_name('td')
                stock_info['name'] = cols[0].text.strip()
                stock_info['url'] = cols[2].find_element_by_tag_name('a').get_attribute('href')

                stock_info['content'] = rows[1].text
                return stock_info
            else:
                return False
        except Exception as error:
            print(f"Class: ShareMarket, Method: scrap_stock_details(); Error: {error.__str__()}")
            return False

    def scrap_webpage(self):
        """
        Open webpage url given in config.py file and scrap data from it.
        after that find all expected keywords in text.
        :return:
        """

        try:
            driver = webdriver.Chrome(executable_path=self.WEBDRIVER_EXE_PATH, options=self.options)
            driver.maximize_window()
            driver.get(cfg.URL)
            time.sleep(5)

            home = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div'))).text

            if not "Announcements".lower() in home.lower():
                driver.refresh()

            pages = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div/div[4]/div[1]").text
            page_count = pages.split(" ")[-1]

            stock_name, pdf_url, content = [], [], []
            print(page_count)
            for page in range(int(page_count)):
                data = driver.find_element_by_xpath('//*[@id="lblann"]/table/tbody/tr[4]/td')
                tables = data.find_elements_by_tag_name('table')
                for table in tables:
                    stock_details = self.scrap_stock_details(table)
                    if stock_details:
                        print(stock_details.get('url', 'No PDF'))
                        stock_name.append(stock_details.get('name', 'No Name'))
                        pdf_url.append(stock_details.get('url', 'No PDF'))
                        content.append(stock_details.get('content', 'No Description'))

                next_button = driver.find_elements_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div[4]/div[1]/b[2]/a')

                if len(next_button) < 1:
                    pass
                else:
                    next_button[0].click()
                    time.sleep(10)

            df = pd.DataFrame()
            df['Name'] = stock_name
            df['Attachment'] = pdf_url
            df['Description'] = content
            df.to_excel(f"Stock Updates_{datetime.date.today()}.xlsx", sheet_name="Stocks")

        except Exception as error:
            print("Exception Raised: ", error.__str__())
            exit(1)


if __name__ == '__main__':
    caller = ShareMarket()
    caller.scrap_webpage()
