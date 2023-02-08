# Creating necessary imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Below code makes bot undetecable by browser.

#Removes navigator.webdriver flag
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service('/Users/maxwalker/Downloads/chromedriver'), options=option)

# Change browser options
option.add_argument("window-size=1280,800")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

# Add a different proxy. A proxy address can already be flagged so if trying, you may need to use a different free proxy or buy ones.
# option.add_argument('proxy-server=106.122.8.54:3128')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Create a path, driver, and link to tiktok homepage
url = "https://www.tiktok.com/en/"
user_profile = "thatdudeshorty.ttv"
driver.get(url)


def get_to_page():
    # Tiktok has puzzle piece captcha. Setting sleep note to allow for us to manually pass it. Should we not solve it for some reason, "except" code will be ran.
    # sleep(10)

    tiktok_search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    tiktok_search_input.click()

    tiktok_search_input.send_keys(user_profile, Keys.ENTER)
    sleep(2)
    # hamed_page_link = driver.find_element(By.CLASS_NAME, 'tiktok-133zmie-DivLink')

    hamed_page_link = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tiktok-8vmh8u-DivLink"))
    )
    hamed_page_link.click()
    driver.refresh()

def view_video():
    get_to_page()

    video = 1
    while video <= 32:
        sleep(2)
        video_to_view = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[{}]'.format(video))
        video_to_view.click()
        print("Video {} started".format(video))

        time_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tiktok-o2z5xv-DivSeekBarTimeContainer"))
        )
        time_container = time_container.text #00:00/01:05
        time_container = time_container[6:] #01:05
        min_seconds_container = int(float(time_container[1:2])) * 60
        seconds_container = int(time_container[3:])
        total_vid_seconds = min_seconds_container + seconds_container

        sleep(total_vid_seconds)
        print("Video {} finished".format(video))

        driver.back()
        video += 1


    print("All videos viewed :)")




view_video()