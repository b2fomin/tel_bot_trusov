import requests
from bs4 import BeautifulSoup

# Функция для получения курса валюты
def get_currency_rate():
    # Адрес сайта, с которого мы будем получать данные
    url = "https://www.google.com/search?q=курс+доллара+к+рублю"
    
    # Получаем содержимое страницы
    response = requests.get(url)
    
    # Создаем объект BeautifulSoup для парсинга HTML-разметки
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Получаем элемент с курсом валюты
    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    
    # Возвращаем курс валюты как число
    return float(result.replace(",", ".")[:5])