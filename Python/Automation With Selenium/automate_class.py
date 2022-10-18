from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import datetime
import os

class AutomateWeatherServices:
    def __init__(self, city):
        self.city = city
        self.driver_location = Service("<Location_Of_ChromeDriver>")
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.driver_location, options=self.options)

    def __str__(self):
        print(f"{self.city}'s weather forecast is located in the screenshots folder")

    def start_chromedriver(self):
        self.driver.get('https://lakerfan1415.github.io/')

    def navigate_to_weather_app(self):
        main_page_btn = self.driver.find_elements(By.TAG_NAME, "a")  # list of attribute elements

        # Clicks weather app button
        main_page_btn[0].click()
        time.sleep(2)

        # Enter information into input field
        self.driver.find_elements(By.ID, "city-input")[0].send_keys(self.city)
        time.sleep(3)

        # Click enter to get weather information
        self.driver.find_elements(By.ID, "city-btn")[0].click()
        time.sleep(2)

    def screenshot_weather(self):
        forecast_types = ["Current", "2-Day Forecast", "7-Day Forecast"]
        cur_date = datetime.datetime.now()
        date = cur_date.strftime("%x").replace("/", ".")
        hour = cur_date.strftime("%I")
        minute = cur_date.strftime("%M")

        folder = ""
        path = ""

        #Create new directory for screenshots
        try:
            folder = f"{self.city.capitalize()}-{date}"
            parent_dir = "<Location_Of_ComputerDrive>\screenshots"

            path = os.path.join(parent_dir, folder)

            os.mkdir(path)
        except:
            folder = f"{self.city.capitalize()}-{date}-Hour.{hour} Minute.{minute}"
            parent_dir = "<Location_Of_ComputerDrive>\screenshots"

            path = os.path.join(parent_dir, folder)

            os.mkdir(path)


        #Grab each screenshot and save to new directory
        for i in range(3):
            forecast_btn = self.driver.find_elements(By.LINK_TEXT, f"{forecast_types[i]}")[0]
            forecast_btn.click()
            time.sleep(4)
            self.driver.save_screenshot(f"{path}/{forecast_types[i]}.png")
            time.sleep(2)


    def close_window(self):
        self.driver.close()