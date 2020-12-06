import telebot 
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException 
import time


bot = telebot.TeleBot("") 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global check 
    check = 3
    bot.send_message(message.from_user.id, "Привет, я буду говорить тебе когда дик мертв/жив. Сейчас он")
    driver = webdriver.Chrome("chromedriver.exe") 
    driver.get("https://digedu.ru/")
    try:
        elem = driver.find_element_by_class_name('navbar')
        bot.send_message(message.from_user.id, "дик робит")
        check = 1
    except NoSuchElementException:
        bot.send_message(message.from_user.id, "Увы, но дик лежит")
        check = 0
    driver.close()
    while 1:
        time.sleep(1200)
        driver = webdriver.Chrome("chromedriver.exe")
        #bot.send_message(message.from_user.id, "чек")
        driver.get("https://digedu.ru/")
        try:
            anal = driver.find_element_by_class_name('navbar')
            check = 1
        except NoSuchElementException: 
            check = 0 
        if check == 0:
            bot.send_message(message.from_user.id, "Дик лежит") 
        elif check == 1:
            bot.send_message(message.from_user.id, "Дик робит")
        time.sleep(300)
        driver.close()
         

@bot.message_handler(content_types=['text'])
def send_hui(message): 
    bot.send_message(message.from_user.id, "Дружище я работаю по времени, если дик упадет или встанет я тебе об этом сообщю") 



bot.polling()