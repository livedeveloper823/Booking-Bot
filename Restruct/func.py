import pyautogui as pyg
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

def wait_url(driver : webdriver.Chrome, url : str):
    print(url)
    while True:
        cur_url = driver.current_url
        if cur_url == url:
            break
        sleep(0.1)
        
def find_element(driver : webdriver.Chrome, whichBy, unique : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(whichBy, unique)
            break
        except:
            pass
        sleep(1)
    return element

# def find_element(driver, whichBy, unique, timeout=10):
#     try:
#         element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((whichBy, unique)))
#         return element
#     except TimeoutException as e:
#         print(f"Element not found: {e}")
#         return None

def find_elements(driver : webdriver.Chrome, whichBy, unique : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(whichBy, unique)
            break
        except:
            pass
        sleep(0.1)
    return elements

def get_price(string):
    string = string.replace(",", "")
    return float(string)

def evaluate_similarity(string1, string2):
  arr1 = string1.lower().split(" ")
  string2 = string2.lower()
  for i in range(len(arr1)):
    if arr1[i] == "de":
      continue
    if string2.find(arr1[i]) != -1:
      return True
  return False


def pressTab(num:int):
    for _ in range(num):
      pyg.press("tab")
      sleep(0.3)

def pressEnter():
   pyg.press("enter")
   sleep(0.3)

def write(text:str):
   pyg.write(text)
   sleep(0.3)