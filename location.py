import tkinter as tk
import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import requests, bs4
from datetime import date
import json
import tkinter as tk
from tkinter import simpledialog
from pynput.keyboard import Key, Listener
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains  #
import pandas as pd
from tkinter import *
from pprint import pprint
import openpyxl
from openpyxl import Workbook
import xlsxwriter
import openpyxl
import time



wu = openpyxl.load_workbook('keywordget.xlsx')
sheet = wu['page1']


current_row = 2  #we start the sheet from the second row
for x,y in enumerate(sheet["a"]):
    if x < 1000:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        result = sheet[f"b{1+x}"].value.replace(" ","-")#####
        print(2, result)
        if result is not None:
            location = result
            url_from = f"https://www.distance.to/{location}/Cancun"   #change city name her
            driver.get(url_from)
            time.sleep(1)
            try:
                login = driver.find_element(By.CLASS_NAME, "flight")
            except:
                continue
            flight_data = login.text
            fuck_you = flight_data.split(" ")

            print(fuck_you[2],"fuck",fuck_you[6]+fuck_you[7])


            time.sleep(0)
            sheet[f"c{1+x}"] = fuck_you[2]
            sheet[f"d{1+x}"] = fuck_you[6]+fuck_you[7]
            
            driver.close()
            wu.save('keywordget.xlsx')




'''

location = "london"
url_from = f"https://www.distance.to/{location}/Mexico-city"

driver.get(url_from)
time.sleep(5)
login = driver.find_element(By.CLASS_NAME, "flight")

flight_data = login.text


fuck_you = flight_data.split(" ")

print(fuck_you[2],"fuck",fuck_you[6]+fuck_you[7])
    '''

