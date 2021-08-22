from selenium import webdriver
from time import sleep
import pyfiglet
import colorama
from colorama import *
colorama.init(convert=True)
init()

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("                                                                                                                 YOUTUBE VIEW BOT")


arttext = pyfiglet.figlet_format("YOUTUBE " + " VIEW " + " BOT", font = "slant")


print(Fore.RED + arttext)
print("")
print("")
print("")
print("" + Fore.WHITE)

link = input("Enter Youtube URL: ")
views = 1000


driver1 = webdriver.Chrome(executable_path="D:\chromedriver/chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="D:\chromedriver/chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="D:\chromedriver/chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="D:\chromedriver/chromedriver.exe")
 
driver1.get(link)
driver2.get(link)
driver3.get(link)
driver4.get(link)
 

for i in range(views):
    sleep(4)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
