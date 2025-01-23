import os
import re

import cv2
from markdown_it.rules_core import linkify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC


# -check url is a youtube video link
# -browser open and scrape beautifulsoup for confirmation 4 day old video and 50k views
# - add script to display graph
# - pass image of graph along to opencv

def check_url(input):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?'
        r'(youtube\.com/watch\?v=|youtu\.be/)'
        r'([a-zA-Z0-9_-]{11})$'
    )
    if re.match(youtube_regex, input) is not None:
        return True
    else:
        return False

def sel_take(input):
    global view_str
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# ////////////////////////////////////////////////////////////chrome browser simulate
    try:
        driver.get(input)
        driver.implicitly_wait(2)
        print(driver.title + " ///////seleneium browser")
        page_view_element = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-watch-info-text/div/yt-formatted-string/span[1]')
        page_view = page_view_element.text
        page_date_element = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-watch-info-text/div/yt-formatted-string/span[3]')
        page_date = page_date_element.text
        try:
            video_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, 'video'))
            )
        except Exception as e:
            print("Error finding video element:", e)
            video_element = None  # Set to None if not found

        if video_element:
            try:
                driver.execute_script("arguments[0].play();", video_element)
                print("Video is now playing.")
            except Exception as e:
                print("Error trying to play the video:", e)
        else:
            print("Video element not found, cannot play.")
# ///////////////////////////////////////////////////check for minimum upload date, views
        total_duration = driver.execute_script("return arguments[0].duration;", video_element)
        total_duration_hr = int(total_duration // 3600)
        total_duration_min = int((total_duration % 3600) // 60)
        total_duration_sec = int(total_duration % 60)
        print(f"{page_date} + {page_view} + {total_duration_hr:02}:{total_duration_min:02}:{total_duration_sec:02}")

        if "hours" in page_date or "hour" in page_date or "day" in page_date:
            print("upload time needs to be at least 4 days")
            driver.quit()
        if "days" in page_date:
            days = re.findall(r'\d+', page_date)
            day = [int(num) for num in days]
            if any (d < 4 for d in day):
                print("Upload time needs to be at least 4 days")
                driver.quit()
        views_str = page_view.replace('views', '').strip()
        if 'M' in views_str:
            view_str = int(float(views_str.replace('M', '').strip()) * 1_000_000)
        elif 'K' in views_str:
            view_str = int(float(views_str.replace('M', '').strip()) * 1_000)
        if int(view_str) < 50000:
            print("need to be above 50k views")
            driver.quit()

        # //////////////////////////////////////////////////////////////////////// youttube mouseover to show graph
        driver.execute_script("""
            const heatMapContainer = document.querySelector('.ytp-progress-bar');
            const mouseOverEvent = new MouseEvent('mouseover', { bubbles: true, cancelable: true, view: window });
            heatMapContainer.dispatchEvent(mouseOverEvent);
        """)

# //////////////////////////////////////////////////////////////////take a screenshot
        os.makedirs('rsrc', exist_ok=True)
        try:
            driver.save_screenshot('rsrc/screenshot.png')
        except Exception as e:
            print(f"Error saving screenshot: {e}")
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()
# ////////////////////////work on image
#     image = cv2.imread('screenshot.png')
