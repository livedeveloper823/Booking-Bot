import openpyxl.workbook
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui
import func
import openpyxl
import json
import re
import os



def submit(accounts:list):
    password = "Book123456"
    for account in accounts:
        pyautogui.hotkey("alt", "tab")
        

        remote_debugging_address = "127.0.0.1:9024"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", remote_debugging_address)
        driver = webdriver.Chrome(options=chrome_options)

        sleep(1)
        pyautogui.write("https://account.booking.com/register")
        func.pressEnter()
        func.wait_url(driver, "https://account.booking.com/register")
        sleep(2)
        try:
            accept_btn = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            accept_btn.click()
        except Exception as e:
            # Add your desired action if the element is not found
            print("Accept button not found. Performing alternative action...", e)
            pass
        sleep(1)

        if account["registered"] == False:
            account["registered"] = True
            with open('accounts.json', 'w') as file:
                json.dump(accounts, file)
            sleep(2)
            func.find_element(driver, By.ID, "username").click()
            func.write(account["email"])
            func.pressTab(1)
            func.pressEnter()
            sleep(1)
            func.write(password)
            sleep(0.5)
            func.pressTab(2)
            func.write(password)
            sleep(0.5)
            func.pressTab(2)
            sleep(0.5)
            func.pressEnter()
            print("Successfully Registered! and Logined!")
            sleep(10)
            pyautogui.hotkey("F6")
            func.pressTab(1)
            func.pressEnter()
            sleep(1)
            pyautogui.hotkey("F6")
            sleep(0.5)
            func.write("https://www.booking.com/hotel/al/arc-tirana.en-gb.html?label=gog235jc-1FCAEoggI46AdIM1gDaAaIAQGYAQm4ARjIAQzYAQHoAQH4AQyIAgGoAgS4AqXWg7EGwAIB0gIkNjY5ZDZjMjUtZmI5NS00NmJmLTkwZTEtZmE5ODZhYmIzNjkz2AIG4AIB&sid=51ac83365fbfd6e0947989086e643ab8&aid=397594&ucfs=1&arphpl=1&checkin=2024-04-19&checkout=2024-04-21&dest_id=-108649&dest_type=city&group_adults=4&req_adults=4&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&nflt=fc%3D2&srpvid=033644eca83b00b2&srepoch=1713433776&all_sr_blocks=229704905_100215859_4_2_0&highlighted_blocks=229704905_100215859_4_2_0&matching_block_id=229704905_100215859_4_2_0&sr_pri_blocks=229704905_100215859_4_2_0__10643&from_sustainable_property_sr=1&from=searchresults#hotelTmpl")
            func.pressEnter()
            sleep(10)
            if func.find_element(driver, By.CSS_SELECTOR, "#no_availability_msg > div.bui-alert.bui-alert--error.bui-alert--large"):
                func.find_element(driver, By.CSS_SELECTOR, "#no_availability_msg > div.change_dates > div.c-next-available-dates--pp.c-next-available-dates--pp--www.c-next-available-dates--pp--www-distant > div.bui-carousel.bui-u-bleed\@small.c-next-available-dates__carousel-wrap > ul > li:nth-child(2) > a").click()
                sleep(5)
                btn_element = func.find_element(driver, By.CSS_SELECTOR, "#bodyconstraint-inner > div:nth-child(8) > div > div.af5895d4b2 > div.df7e6ba27d > div.bcbf33c5c3 > div.dcf496a7b9.bb2746aad9 > div.d4924c9e74 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4.bbefc5a07c > div.c066246e13 > div.c1edfbabcb > div > div.b1037148f8 > div.a4b53081e1 > div > div.da8b337763 > a")
                link = btn_element.get_attribute("href")
                sleep(2)
                pyautogui.hotkey("F6")
                sleep(0.5)
                func.pressTab(1)
                func.pressEnter()
                sleep(1)
                pyautogui.hotkey("F6")
                sleep(0.3)
                func.write(link)
                func.pressEnter()
                func.find_element(driver, By.CSS_SELECTOR, "#group_recommendation > table > tbody > tr > td.totalPrice-container > table > tbody > tr:nth-child(2) > td > a").click()
                sleep(2)
                func.find_element(driver, By.CLASS_NAME, "hprt-reservation-cta").click()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#firstname").click()
                sleep(0.5)
                func.write(account["first_name"])
                func.pressTab(1)
                func.write(account["last_name"])
                sleep(1)
                func.find_element(driver, By.CSS_SELECTOR, "#cc1").click()
                func.write("Albania")
                func.pressEnter()
                func.pressTab(1)
                func.write("237431834")
                sleep(2)
                time = func.find_element(driver, By.CSS_SELECTOR, "#bookForm > section.bui-card.bp-card--arrival-time.bui-u-bleed\@small.bui-spacer--large > div > div > div > div:nth-child(1) > ul > li > div > div").text
                match_time = re.search(r'\d+:\d+', time)
                if match_time:
                    # Extract the matched numbers
                    booking_time = match_time.group()
                    print(booking_time)  # Output: 14:00
                else:
                    print("No numbers found")
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#checkin_eta_hour").click()
                sleep(0.5)
                func.write(booking_time)
                func.pressEnter()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div.bui-group__item > button").click()
                sleep(5)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div:nth-child(3) > button").click()
                sleep(10)
                # logout
                func.find_element(driver, By.CSS_SELECTOR, "#b2searchresultsPage > div:nth-child(6) > div > div > header > nav.c20fd9b542 > div.c624d7469d.f034cf5568.dab7c5c6fa.c62ffa0b45.a3214e5942 > div > span > button > span > div").click()
                func.pressTab(6)
                sleep(0.5)
                func.pressEnter()
            else:
                func.find_element(driver, By.CSS_SELECTOR, "#group_recommendation > table > tbody > tr > td.totalPrice-container > table > tbody > tr:nth-child(2) > td > a").click()
                sleep(2)
                func.find_element(driver, By.CLASS_NAME, "hprt-reservation-cta").click()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#firstname").click()
                sleep(0.5)
                func.write(account["first_name"])
                func.pressTab(1)
                func.write(account["last_name"])
                sleep(1)
                func.find_element(driver, By.CSS_SELECTOR, "#cc1").click()
                func.write("Albania")
                func.pressEnter()
                func.pressTab(1)
                func.write("237431834")
                sleep(2)
                time = func.find_element(driver, By.CSS_SELECTOR, "#bookForm > section.bui-card.bp-card--arrival-time.bui-u-bleed\@small.bui-spacer--large > div > div > div > div:nth-child(1) > ul > li > div > div").text
                match_time = re.search(r'\d+:\d+', time)
                if match_time:
                    # Extract the matched numbers
                    booking_time = match_time.group()
                    print(booking_time)  # Output: 14:00
                else:
                    print("No numbers found")
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#checkin_eta_hour").click()
                sleep(0.5)
                func.write(booking_time)
                func.pressEnter()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div.bui-group__item > button").click()
                sleep(5)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div:nth-child(3) > button").click()
                sleep(10)
                # logout
                func.find_element(driver, By.CSS_SELECTOR, "#b2searchresultsPage > div:nth-child(6) > div > div > header > nav.c20fd9b542 > div.c624d7469d.f034cf5568.dab7c5c6fa.c62ffa0b45.a3214e5942 > div > span > button > span > div").click()
                func.pressTab(6)
                sleep(0.5)
                func.pressEnter()
        if account["registered"] == True:
            sleep(2)
            func.find_element(driver, By.ID, "username").click()
            func.write(account["email"])
            func.pressTab(1)
            func.pressEnter()
            sleep(1)
            func.write(password)
            sleep(0.5)
            func.pressTab(2)
            sleep(0.5)
            func.pressEnter()
            print("Successfully Logined!")
            sleep(10)
            pyautogui.hotkey("F6")
            func.pressTab(1)
            func.pressEnter()
            sleep(1)
            pyautogui.hotkey("F6")
            sleep(0.5)
            func.write("https://www.booking.com/hotel/al/enjoy-sunset-at-this-spacious-apartment.en-gb.html?aid=397594&label=gog235jc-1FCAEoggI46AdIM1gDaAaIAQGYAQm4ARjIAQzYAQHoAQH4AQyIAgGoAgS4AqXWg7EGwAIB0gIkNjY5ZDZjMjUtZmI5NS00NmJmLTkwZTEtZmE5ODZhYmIzNjkz2AIG4AIB&sid=51ac83365fbfd6e0947989086e643ab8&all_sr_blocks=1039762901_385657704_0_0_0;checkin=2024-04-19;checkout=2024-04-21;dest_id=-108649;dest_type=city;dist=0;group_adults=4;group_children=0;hapos=1;highlighted_blocks=1039762901_385657704_0_0_0;hpos=1;matching_block_id=1039762901_385657704_0_0_0;nflt=fc%3D2;no_rooms=1;req_adults=4;req_children=0;room1=A%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=1039762901_385657704_0_0_0__8190;srepoch=1713433701;srpvid=033644eca83b00b2;type=total;ucfs=1&#hotelTmpl")
            func.pressEnter()
            sleep(10)
            if func.find_element(driver, By.CSS_SELECTOR, "#no_availability_msg > div.bui-alert.bui-alert--error.bui-alert--large"):
                func.find_element(driver, By.CSS_SELECTOR, "#no_availability_msg > div.change_dates > div.c-next-available-dates--pp.c-next-available-dates--pp--www.c-next-available-dates--pp--www-distant > div.bui-carousel.bui-u-bleed\@small.c-next-available-dates__carousel-wrap > ul > li:nth-child(2) > a").click()
                sleep(5)
                btn_element = func.find_element(driver, By.CSS_SELECTOR, "#bodyconstraint-inner > div:nth-child(8) > div > div.af5895d4b2 > div.df7e6ba27d > div.bcbf33c5c3 > div.dcf496a7b9.bb2746aad9 > div.d4924c9e74 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4.bbefc5a07c > div.c066246e13 > div.c1edfbabcb > div > div.b1037148f8 > div.a4b53081e1 > div > div.da8b337763 > a")
                link = btn_element.get_attribute("href")
                sleep(2)
                pyautogui.hotkey("F6")
                sleep(0.5)
                func.pressTab(1)
                func.pressEnter()
                sleep(1)
                pyautogui.hotkey("F6")
                sleep(0.3)
                func.write(link)
                func.pressEnter()
                func.find_element(driver, By.CSS_SELECTOR, "#group_recommendation > table > tbody > tr > td.totalPrice-container > table > tbody > tr:nth-child(2) > td > a").click()
                sleep(2)
                func.find_element(driver, By.CLASS_NAME, "hprt-reservation-cta").click()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#firstname").click()
                sleep(0.5)
                func.write(account["first_name"])
                func.pressTab(1)
                func.write(account["last_name"])
                sleep(1)
                func.find_element(driver, By.CSS_SELECTOR, "#cc1").click()
                func.write("Albania")
                func.pressEnter()
                func.pressTab(1)
                func.write("237431834")
                sleep(2)
                time = func.find_element(driver, By.CSS_SELECTOR, "#bookForm > section.bui-card.bp-card--arrival-time.bui-u-bleed\@small.bui-spacer--large > div > div > div > div:nth-child(1) > ul > li > div > div").text
                match_time = re.search(r'\d+:\d+', time)
                if match_time:
                    # Extract the matched numbers
                    booking_time = match_time.group()
                    print(booking_time)  # Output: 14:00
                else:
                    print("No numbers found")
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#checkin_eta_hour").click()
                sleep(0.5)
                func.write(booking_time)
                func.pressEnter()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div.bui-group__item > button").click()
                sleep(5)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div:nth-child(3) > button").click()
                sleep(10)
                # logout
                func.find_element(driver, By.CSS_SELECTOR, "#b2searchresultsPage > div:nth-child(6) > div > div > header > nav.c20fd9b542 > div.c624d7469d.f034cf5568.dab7c5c6fa.c62ffa0b45.a3214e5942 > div > span > button > span > div").click()
                func.pressTab(6)
                sleep(0.5)
                func.pressEnter()
            else:
                func.find_element(driver, By.CSS_SELECTOR, "#group_recommendation > table > tbody > tr > td.totalPrice-container > table > tbody > tr:nth-child(2) > td > a").click()
                sleep(2)
                func.find_element(driver, By.CLASS_NAME, "hprt-reservation-cta").click()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#firstname").click()
                sleep(0.5)
                func.write(account["first_name"])
                func.pressTab(1)
                func.write(account["last_name"])
                sleep(1)
                func.find_element(driver, By.CSS_SELECTOR, "#cc1").click()
                func.write("Albania")
                func.pressEnter()
                func.pressTab(1)
                func.write("237431834")
                sleep(2)
                time = func.find_element(driver, By.CSS_SELECTOR, "#bookForm > section.bui-card.bp-card--arrival-time.bui-u-bleed\@small.bui-spacer--large > div > div > div > div:nth-child(1) > ul > li > div > div").text
                match_time = re.search(r'\d+:\d+', time)
                if match_time:
                    # Extract the matched numbers
                    booking_time = match_time.group()
                    print(booking_time)  # Output: 14:00
                else:
                    print("No numbers found")
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#checkin_eta_hour").click()
                sleep(0.5)
                func.write(booking_time)
                func.pressEnter()
                sleep(2)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div.bui-group__item > button").click()
                sleep(5)
                func.find_element(driver, By.CSS_SELECTOR, "#bookForm > div.bui-group.bui-spacer--large > div > div:nth-child(3) > button").click()
                sleep(10)
                # logout
                func.find_element(driver, By.CSS_SELECTOR, "#b2searchresultsPage > div:nth-child(6) > div > div > header > nav.c20fd9b542 > div.c624d7469d.f034cf5568.dab7c5c6fa.c62ffa0b45.a3214e5942 > div > span > button > span > div").click()
                func.pressTab(6)
                sleep(0.5)
                func.pressEnter()
        func.wait_url(driver, "https://account.booking.com/signup")
        print("Successfully Registered!")

if __name__ == "__main__":
    response = input("Do you want to register new account?(y/n)")

    accounts = []
    if response == "y":
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
            print(accounts)
    submit(accounts)
