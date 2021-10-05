import random
import time
from selenium import webdriver


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$#'
numbers = '0123456789'

random_length = random.randint(7, 15)
# replace this with your username
user_name = 'INSERT_USERNAME'

# creates a new password


def make_password(length):
    password = ''
    half = round(length / 2)
    for i in range(1, half):
        password += chars[random.randint(0, len(chars) - 1)]

    for i in range(1, half + 1):
        password += numbers[random.randint(0, len(numbers) - 1)]

    shuffled = list(password)
    random.shuffle(shuffled)
    return ''.join(shuffled)


# runs to make a new password and stores to variable
made_password = make_password(random_length)
# opens or creates txt file to hold password locally
# reads and stores the last made password in a variable for next reset
txt_file = open('hello.txt', 'r+')
last_password = txt_file.read()
# truncate deletes file contents to store new password
txt_file.truncate(0)
txt_file.close()
# stores the new password we created.
reopen = open('hello.txt', 'w')
reopen.write(made_password)
reopen.close()


# function with all webdriver commands
def change_insta(user_name, last_password, made_password):
    driver = webdriver.Chrome(
        executable_path='/usr/lib/chromium-browser/chromedriver')
    driver.get('https://instagram.com')
    time.sleep(75)
    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user_name)

    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(last_password)
    time.sleep(75)
    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(75)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    time.sleep(60)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[3]/div').click()
    time.sleep(75)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()
    time.sleep(75)
    driver.find_element_by_xpath(
        '//*[@id="cppOldPassword"]').send_keys(last_password)
    driver.find_element_by_xpath(
        '//*[@id="cppNewPassword"]').send_keys(made_password)
    driver.find_element_by_xpath(
        '//*[@id="cppConfirmPassword"]').send_keys(made_password)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/form/div[4]/div/div/button').click()
    time.sleep(10)
    driver.quit()


# run the code with all the needed contents
change_insta(user_name, last_password, made_password)
