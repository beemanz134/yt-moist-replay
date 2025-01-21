import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get(input)
        driver.implicitly_wait(4)  # Waits for elements to load
        print(driver.title)

    finally:
        driver.quit()
