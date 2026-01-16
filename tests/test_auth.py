import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ================= CONFIG =================
BASE_URL = "http://localhost/quiz"
SHOT_DIR = "tests/screenshots"
os.makedirs(SHOT_DIR, exist_ok=True)


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def shot(driver, name):
    driver.save_screenshot(os.path.join(SHOT_DIR, name))


# =====================================================
# ================= HALAMAN LOGIN ======================
# =====================================================

# L1 - tanpa memasukkan data
def test_login_empty():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login.php")
    shot(driver, "L1_login_empty_page.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "L1_login_empty_result.png")

    driver.quit()


# L2 - hanya memasukkan username
def test_login_only_username():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login.php")

    driver.find_element(By.NAME, "username").send_keys("ra")
    shot(driver, "L2_only_username_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "L2_only_username_result.png")

    driver.quit()


# L3 - username ra + password sembarang
def test_login_wrong_password():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login.php")

    driver.find_element(By.NAME, "username").send_keys("ra")
    driver.find_element(By.NAME, "password").send_keys("sembarang")
    shot(driver, "L3_wrong_password_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "L3_wrong_password_result.png")

    driver.quit()


# L4 - username ra + password 123
def test_login_short_password():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login.php")

    driver.find_element(By.NAME, "username").send_keys("ra")
    driver.find_element(By.NAME, "password").send_keys("123")
    shot(driver, "L4_short_password_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "L4_short_password_result.png")

    driver.quit()


# L5 - SQL Injection
def test_login_sql_injection():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login.php")

    driver.find_element(By.NAME, "username").send_keys("' OR '1'='1")
    driver.find_element(By.NAME, "password").send_keys("' OR '1'='1")
    shot(driver, "L5_sql_injection_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "L5_sql_injection_result.png")

    driver.quit()


# =====================================================
# ================= HALAMAN REGISTER ===================
# =====================================================

# R1 - tidak mengisi data
def test_register_empty():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/register.php")
    shot(driver, "R1_register_empty_page.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "R1_register_empty_result.png")

    driver.quit()


# R2 - username sudah ada (ra)
def test_register_existing_user():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/register.php")

    driver.find_element(By.NAME, "username").send_keys("ra")
    driver.find_element(By.NAME, "email").send_keys("ra@email.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "repassword").send_keys("123456")
    shot(driver, "R2_existing_user_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "R2_existing_user_result.png")

    driver.quit()


# R3 - email tanpa @
def test_register_invalid_email():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/register.php")

    driver.find_element(By.NAME, "username").send_keys("user_email_salah")
    driver.find_element(By.NAME, "email").send_keys("emailsalah.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "repassword").send_keys("123456")
    shot(driver, "R3_invalid_email_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "R3_invalid_email_result.png")

    driver.quit()


# R4 - password dan repassword tidak sama
def test_register_password_not_match():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/register.php")

    driver.find_element(By.NAME, "username").send_keys("user_pass_beda")
    driver.find_element(By.NAME, "email").send_keys("user@mail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "repassword").send_keys("654321")
    shot(driver, "R4_password_not_match_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "R4_password_not_match_result.png")

    driver.quit()


# R5 - semua data valid
def test_register_success():
    driver = setup_driver()
    driver.get(f"{BASE_URL}/register.php")

    username = "user_" + str(int(time.time()))

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "email").send_keys(f"{username}@mail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "repassword").send_keys("123456")
    shot(driver, "R5_register_success_input.png")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    shot(driver, "R5_register_success_result.png")

    driver.quit()
