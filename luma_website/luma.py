from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.support.ui import Select
 
driver = webdriver.Chrome() 
driver.maximize_window()

try: 
    driver.get("https://magento.softwaretestingboard.com/") 
    print("[URL] Step 1 - Login page ✅:", driver.current_url)
    time.sleep(3)

    first_name = "Sagotam1"
    last_name = 'Kumar'
    email = 'sagotam1@gmail.com'
    password = 'Sagotam4321@'
    confim_password = 'Sagotam4321@'

    # --------------- registration start-----------------------
    # create_an_account = driver.find_element(By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']").click()
    # time.sleep(3)

    # create_an_account_text = driver.find_element(By.XPATH, "//span[@class='base']").text
    # print('[PRINT]create an account text ✅: ', create_an_account_text)

    # if 'Create New Customer Account' in create_an_account_text:
    #    print('[SUCCESS] ✅------------now in the create register page-----------')

    # else:
    #    print('[FAILLED] ❌---------failed to load register page---------')

    # # first name
    # driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys(first_name)
    # time.sleep(2)
    # # last name
    # driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys(last_name)
    # time.sleep(2)
    # # email
    # driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys(email)
    # time.sleep(2)
    # # password
    # driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    # time.sleep(2)
    # # confim_password
    # driver.find_element(By.XPATH, "//input[@id='password-confirmation']").send_keys(confim_password)
    # time.sleep(2)
    
    # # register button click
    # driver.find_element(By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]").click()
    # time.sleep(5)

    # # register success message
    # register_succes_msg = driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']").text

    # print('[PRINT]register success message ✅: ', register_succes_msg)

    # if 'Thank you for registering with Main Website Store.' in create_an_account_text:
    #    print('[SUCCESS] ✅------------now in the register page-----------')

    # else:
    #    print('[FAILLED] ❌---------failed to load register page---------')
    # # --------------- registration end-----------------------

    # --------------- sign in start -------------------------
    sign_in_btn = driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()
    time.sleep(2)
    login_page_text = driver.find_element(By.XPATH, "//span[@class='base']").text
    print('[PRINT]login  page ✅: ', login_page_text)

    if 'Customer Login' in login_page_text:
       print('[SUCCESS] ✅------------now in the login page-----------')

    else:
       print('[FAILLED] ❌---------failed to load login page---------')

    # email fill up
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    # pass fill up
    driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//input[@id='pass']").send_keys(password)

    # sing in button click
    driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
    time.sleep(3)

    welcome_text = driver.find_element(By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, Sagotam1 Kumar!']").text

    if 'Welcome, Sagotam1 Kumar!' in welcome_text:
       print('[SUCCESS] ✅------------now in the home page-----------')
    else:
       print('[FAILLED] ❌---------failed to load home page---------')
    # --------------- sign in end -------------------------

    # go to men 
    driver.find_element(By.XPATH, "//span[normalize-space()='Men']").click()
    time.sleep(2)
    # go to jacket
    driver.find_element(By.XPATH, "//a[contains(text(),'Jackets')]").click()
    time.sleep(2)
    
    #-------------- select mars heattech------- start----------
    driver.find_element(By.XPATH, "//img[@alt='Mars HeatTech™ Pullover']").click()
    time.sleep(2)

    # size click
    driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']").click()
    time.sleep(1)
    # color click
    driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-56']").click()
    time.sleep(1)
    # qty click
    driver.find_element(By.XPATH, "//input[@id='qty']").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='qty']").send_keys('2')
    time.sleep(1)
    # add to cart click
    driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()
    time.sleep(3)
    print('------------cart product succes------------')
    #-------------- select mars heattech------- end----------

    #--------------- cart button click----------------------
    driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
    time.sleep(2)

    # proceed to checkout click
    driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
    time.sleep(3)

    # shipping page 
    street_address = '324234'
    city = 'savar'
    
    # dropdown_element = driver.find_element(By.XPATH, "//select[@id='GJE0RLW']")
    # time.sleep(2)

    # # Use the Select class to select an option
    # select = Select(dropdown_element)
    # select.select_by_visible_text("California")


    # Step 2: Locate the <select> dropdown element
    dropdown = driver.find_element(By.XPATH, "//select[@id='GJE0RLW']")
    
    # Step 3: Click the dropdown (not always needed for <select>, but done here for demo)
    dropdown.click()
    time.sleep(5)
    print("click done -----------------------")

    # Step 4: Wrap it with Select class
    select = Select(dropdown)
    print("select done -----------------------")
    # Step 5: Print the currently selected option
    selected_option = select.first_selected_option
    print("Current selected value:", selected_option.text)

    # Step 6: Print all available options
    print("\nAll dropdown options:")
    for option in select.options:
        print("-", option.text)

    # Step 7: Select a new value (e.g., "Texas")
    select.select_by_visible_text("Texas")
    print("Texas select -----------------------")
    time.sleep(5)

    # Step 8: Print the newly selected option
    new_selected = select.first_selected_option
    print("\nNew selected value:", new_selected.text)

    time.sleep(10)
except AssertionError as e: 
   print(f"Test Failed ❌ : {e}") 
 
finally: 
   driver.quit() 
