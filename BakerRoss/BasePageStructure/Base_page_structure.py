from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import logging
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import openpyxl
import datetime
import sys
import os
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from io import StringIO
from  TestsConfiguration.local_env import *


class BasePage(object):

    def __init__(self, autotestenvironment, autotestenvchoice, user_catalogue, driver):
        # Variables
        self.autotestenvironment = autotestenvironment
        self.autotestenvchoice = autotestenvchoice
        self.user_catalogue = user_catalogue
        self.driver = driver
    autotestenvironment = localenv + '\\automatedTests\\BakerRoss\\TestsConfiguration\\BakerRoss_env.xml'
    autotestenvchoice = localenv + '\\automatedTests\\BakerRoss\\TestsConfiguration\\env_choice.csv'
    user_catalogue = localenv + '\\automatedTests\\BakerRoss\\TestsData\\user_catalogue.csv'
    # Load the browser defined in env_choice
    with open(autotestenvchoice, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            browser = line['browser']
            if browser == 'Chrome':
                driver = webdriver.Chrome(chromedriver)
            if browser == 'Firefox':
                binary = FirefoxBinary(firefoxdriver)
                driver = webdriver.Firefox(firefox_binary=binary)
            if browser == 'IE':
                driver = webdriver.Ie(internetexplorerdriver)

    # Methods
    def getcountry(self):
        with open(self.autotestenvchoice, "r") as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                country = line['country']
                return country

    def impwait(self):
        self.driver.implicitly_wait(5)

    def createlogfile(self):
        logfilename = datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S') + '_' + os.path.splitext(os.path.basename(sys.argv[0]))[0] + '_log.xlsx'
        wb = openpyxl.Workbook()
        wb.save(logfilename)
        ws = wb.worksheets[0]
        ws['A1'] = 'Date'
        ws['B1'] = 'Test'
        ws['C1'] = 'Status'
        ws['D1'] = 'Details'
        ws['A2'] = datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
        ws ['B2'] = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        wb.save(logfilename)

    def getdomain(self):
        with open(self.autotestenvchoice,"r") as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                environment = line['env']
                country = line['country']
                soup = BeautifulSoup(open(self.autotestenvironment),'html.parser')
                for a in soup.find_all("env", attrs={"id": environment}):
                    for b in a.find_all("country", attrs={"id": country}):
                            domain = b.text
                            return domain

    def gotourl(self, path):
        #self.getdomain()
        url = self.getdomain() + path
        self.driver.get(url)
        self.driver.maximize_window()
        self.impwait()

    def getloginvalue(self):
        site = self.getcountry()
        with open(self.user_catalogue, "r") as file:
            csv_reader = csv.DictReader(file)
            row = [row for row in csv_reader if row['country'] == site]
            for rows in row:
                emailValue = rows['login']
                return emailValue

    def getpassvalue(self):
        site = self.getcountry()
        with open(self.user_catalogue, "r") as file:
            csv_reader = csv.DictReader(file)
            row = [row for row in csv_reader if row['country'] == site]
            for rows in row:
                passValue = rows['password']
                return passValue