from selenium import webdriver

#Merit Group

url = "https://www.bseindia.com/corporates/ann.html"

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)

home = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div/span")

table = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table")

tables = table.find_elements_by_tag_name('table')

for t in tables:
    rows = t.find_elements_by_tag_name('tr')
    name = rows[0].find_elements_by_tag_name('td')
    print(name[0].text)
    url = t.find_elements_by_tag_name('a')
    url1 = url[1].get_attribute('href')
    print(url1)




"""    class Employee:
def __init__(self, name, age,salary):

"""

class Employee:

    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)

obj1 = Employee("Name1", "28", "30000")
obj1.display()
obj2 = Employee("Name2", '30', "40000")
obj2.display()