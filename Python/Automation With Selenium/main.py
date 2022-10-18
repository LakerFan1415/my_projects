""""
Automation with selenium web driver
"""
import automate_class


###Can also use sys class to pass city as argument on command line###
#city = sys.argv[1]
city = input("Enter A City: ")


if __name__ == "__main__":
    find_weather = automate_class.AutomateWeatherServices(city)
    find_weather.start_chromedriver()
    find_weather.navigate_to_weather_app()
    find_weather.screenshot_weather()
    find_weather.close_window()