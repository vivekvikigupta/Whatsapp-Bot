#this code is written by Vivek Gupta // vivekvikigupta@gmail.com

#importing webdriver
from selenium import webdriver

#opening whatsapp web in browser
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

#collecting data to be sended to a user
name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')
#_13mgZ is the div id in which msg box form is present.

#loop for sending the msg
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
	#_3M-N- is the div id in which send button is present.
    button.click()
