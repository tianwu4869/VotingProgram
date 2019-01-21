from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

players = ['towns', 'rose', 'wiggins', 'covington']
firstname = "Tian"
zipcode = "55114"
email = "wu000130@umn.edu"

driver = webdriver.Chrome()
driver.get('https://vote.nba.com')

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='toggle-filters__button']"))
)

players.sort()
counter = 0
while True:
    try:
        vote = driver.find_element_by_xpath("//button[contains(@data-id, '" + players[counter] + "')]")
        if (counter + 1) == len(players):
            vote.click()
            break
        else:
            vote.click()
            counter += 1
    except:
        driver.execute_script("window.scrollBy(0, 200)")    

sumbit = driver.find_element_by_xpath("//input[@type='submit']")
sumbit.click()

Firstname = driver.find_element_by_xpath("//input[@name='firstname']")
Firstname.send_keys(firstname)
Zip = driver.find_element_by_xpath("//input[@name='zip']")
Zip.send_keys(zipcode)
Email = driver.find_element_by_xpath("//input[@name='email']")
Email.send_keys(email)

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']"))).click()

