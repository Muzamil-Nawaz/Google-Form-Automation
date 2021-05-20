import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from xlrd import open_workbook
import time


book =  open_workbook("us500.xlsx")
sheet = book.sheet_by_index(0)

names = []
emails =[]

for k in range(1,sheet.nrows):
    names.append(str(sheet.row_values(k)[1-1]))
    emails.append(str(sheet.row_values(k)[11-1]))
print(names,emails)


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='G:\Google form automation\chromedriver_win32\chromedriver.exe', options=option)

browser.get("https://forms.gle/48AG4X42zywV89TL8")

for i in range(12,150):
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(names[i])
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(emails[i])
    browser.find_element_by_xpath('//*[@id="i18"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i37"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i50"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i63"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i73"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i86"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i111"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i121"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i137"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i156"]/div[3]/div').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="i5"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i24"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i37"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i50"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i60"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i67"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i83"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i99"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i109"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i125"]/div[3]/div').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="i14"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i30"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i40"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i53"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i75"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i85"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i110"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i120"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i142"]/div[3]/div').click()
    browser.find_element_by_xpath('//*[@id="i152"]/div[3]/div').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()
    time.sleep(2)
    browser.get("https://forms.gle/48AG4X42zywV89TL8")

    
# js = """
# document.querySelector('.quantumWizTextinputPaperinputInput exportInput').value = 'adasd'; """
# browser.execute_script(js)