from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 
 
driver = webdriver.Chrome() 
driver.maximize_window()

try: 
    driver.get("https://practicetestautomation.com/practice-test-login/") 
    print("Step 1 - Login page ✅:", driver.current_url)

    username_input = "student"          
    password_input = "Password123" 

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username_input) 
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password_input) 
    driver.find_element(By.XPATH, "//button[@id='submit']").click() 
    time.sleep(2) 

    print("Step 2 - After login ✅:", driver.current_url) 
    after_login_url = driver.current_url
    original_window = driver.current_window_handle
    print('original window : ', original_window)

    try:
        message = driver.find_element(By.XPATH, "//h1[normalize-space()='Logged In Successfully']").text 
    except:
        message = driver.find_element(By.XPATH, "//div[@id='error']").text
    time.sleep(2)

    print("Message ✅ :", message) 

    success_text = "Logged In Successfully" 
    password_failed = "Your password is invalid!"
    username_failed = "Your username is invalid!"

    if success_text in message: 
        print("Test Passed ✅ : Login successful.") 
    elif password_failed in message: 
        print("Test Passed ✅ : password invalide.") 
    elif username_failed in message: 
        print("Test Passed ✅ : usernmae invalide.") 
    else: 
        raise AssertionError(f"Unexpected flash message: {message}") 
    time.sleep(3)

    # courses 
    driver.find_element(By.XPATH, "//a[normalize-space()='Courses']").click()
    time.sleep(3)
    print("Step 3 - Courses page ✅:", driver.current_url)

    # python_buy
    driver.find_element(By.XPATH, "//a[@href='https://practicetestautomation.com/selenium-python-udemy']").click()
    time.sleep(3) 

    # original_window = driver.current_window_handle
    # print("Step 4 - Original window handle:", original_window)
    # time.sleep(3)

    # Switch to new window/tab
    all_windows = driver.window_handles
    for window in all_windows:
        driver.switch_to.window(window)
        print("Switched to window:", driver.current_url)
        if window != original_window:
            break
        
    print("Step 4 - In new tab ✅:", driver.current_url)
    time.sleep(10)

    try:
        # Try to detect if Udemy page loaded (check if a course title exists)
        # //*[@id="udemy"]/div[1]/div[1]/header/div[5]/a/span
        udemy_course_loign = driver.find_element(By.XPATH, "//span[normalize-space()='Log in']").text
        print("Udemy Page Loaded ✅:", udemy_course_loign)
    except:
        # If not loaded, show custom message
        print("Udemy Page ❌: Failed to load course content")
        driver.close()
        
        driver.switch_to.window(original_window)
        time.sleep(2)

        driver.get(after_login_url)
        print("✅ Returned to original tab:", driver.current_url)
        time.sleep(10)

        driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()

        test_loign_text = driver.find_element(By.XPATH, "//h2[normalize-space()='Test login']").text
        if 'Test login' in test_loign_text:
            print('---------------LOG OUT SUCCESS----------------')

        else:
            print('----------------failed to logout------------------')
except AssertionError as e: 
   print(f"Test Failed ❌ : {e}") 
 
finally: 
   driver.quit() 
