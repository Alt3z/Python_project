from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def get_price(html_code):
    span = html_code.split('<span class="">')[1].split('</span>')[0]
    return span.replace('&nbsp;', '').replace('<!-- -->', '')

def parse(driver):
    container = driver.find_element(By.CLASS_NAME, 'items-items-kAJAg')
    elements = container.find_elements(By.CLASS_NAME, 'iva-item-root-_lk9K')

    obyavlen = {}

    for element in elements:
        title_container = element.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
        price_container = element.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')

        title = title_container.text
        price_html = price_container.find_element(By.CLASS_NAME, 'styles-module-root-LIAav').get_attribute('outerHTML')
        price = get_price(price_html)

        obyavlen[title] = price

    return obyavlen

def output(dict):
    if len(dict) != 0:
        keys = dict.keys()
        for key in keys:
            print(f'{key} : {dict.get(key)}')

try:
    driver.get('https://www.avito.ru/')

    search_edittext = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input')
    search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/button')

    search_edittext.send_keys('клавиатуры')
    time.sleep(1)
    search_button.click()

    page1 = parse(driver)
    output(page1)
    print(f'Количество объявлений >> {len(page1)}')

except Exception as e:
    print(f'Exception >> {e}')
finally:
    time.sleep(10)
    driver.close()
    driver.quit()
