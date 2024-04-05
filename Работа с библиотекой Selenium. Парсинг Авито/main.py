from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() # Настраиваем веб-драйвер Google Chrome
driver = webdriver.Chrome(options=options)

def get_price(html_code): # Функция для извлечения цены из HTML-кода
    span = html_code.split('<span class="">')[1].split('</span>')[0]
    return span.replace('&nbsp;', '').replace('<!-- -->', '')

def parse(driver): # Функция для парсинга страницы и сбора информации об объявлениях
    container = driver.find_element(By.CLASS_NAME, 'items-items-kAJAg')
    elements = container.find_elements(By.CLASS_NAME, 'iva-item-root-_lk9K')

    obyavlen = {}

    
    for element in elements: # Проходим по каждому элементу и извлекаем заголовок и цену
        title_container = element.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
        price_container = element.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')

        title = title_container.text
        price_html = price_container.find_element(By.CLASS_NAME, 'styles-module-root-LIAav').get_attribute('outerHTML')
        price = get_price(price_html)

        obyavlen[title] = price # Добавляем информацию об объявлении в словарь

    return obyavlen

def output(dictionary): # Функция для вывода информации о найденных объявлениях
    if len(dictionary) != 0:
        keys = dictionary.keys()
        for key in keys:
            print(f'{key} : {dictionary.get(key)}')

try:
    driver.get('https://www.avito.ru/') # Загружаем страницу Avito

    # Находим поле для ввода запроса и кнопку поиска
    search_edittext = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input') 
    search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/button')

    search_edittext.send_keys('клавиатуры') # Вводим запрос и выполняем поиск
    time.sleep(1)  # Ждем 1 секунду, чтобы страница успела обновиться, если не ждать, программа может вылететь
    search_button.click()

    page1 = parse(driver)  # Парсим первую страницу с объявлениями
    output(page1)  # Выводим информацию о найденных объявлениях на первой странице
    print(f'Количество объявлений: {len(page1)}')

except Exception as e:
    print(f'Exception: {e}')
finally:
    driver.close()
    driver.quit()
