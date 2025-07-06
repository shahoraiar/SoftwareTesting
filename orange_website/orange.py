from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    username = "Admin"
    password = "admin123"

    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(3)

    try:
        message = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    except:
        message = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
    
    print('message ✅ : ', message)

    if "Dashboard" in message:
        print('Welcome to Dashboard ✅')
    elif "Invalid credentials" in message:
        print("Login Failed ✅")
        driver.quit()

    time.sleep(2)

    my_info_element = driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
    print('---------------------my info clicked end ---------------------------')
    time.sleep(5)
    qualification = driver.find_element(By.XPATH, "//a[normalize-space()='Qualifications']").click()
    time.sleep(2)

    work_experience_add_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button').click()
    time.sleep(3)

    company = "CodeForces"
    job_title = "JR. Software Developer"
    from_date = "2022-31-12"
    to_date = "2023-31-12"
    commnet = "Nice Work Place"

    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input""").send_keys(company)
    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input""").send_keys(job_title)
    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input""").send_keys(from_date)
    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input""").send_keys(to_date)
    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[3]/div/div/div/div[2]/textarea""").send_keys(commnet)
    time.sleep(1)

    work_experience_save = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/button[2]').click()
    print('------------------- work_experience_save ----------------- ')

    # education_add_button 
    driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button""").click()
    time.sleep(3)

    # education level dropdown click 
    print('-------------------education level dropdown click start ----------------- ')
    dropdown_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    driver.find_element(By.XPATH, dropdown_xpath).click()
    print('-----------education level dropdown click end -------------------- ')
    time.sleep(2)

    # Get and print selected text
    selected_value_xpath = dropdown_xpath + '/div[@class="oxd-select-text-input"]'
    selected_value = driver.find_element(By.XPATH, selected_value_xpath).text
    print("education Selected value:", selected_value)

    # Print all visible dropdown options
    options = driver.find_elements(By.XPATH, '//div[contains(@class,"oxd-select-dropdown")]//div')
    print("Dropdown options:")
    for opt in options:
        print("--", opt.text)
    
    # college
    print('----------selelct the college option  start --------------')
    option_xpath = '//div[contains(@class,"oxd-select-dropdown")]//div[@role="option"]/span[text()="College Undergraduate"]'
    driver.find_element(By.XPATH, option_xpath).click()
    print('----------selelct the college option end --------------')
    time.sleep(1)

    # institue
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("NITER")
    # major
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys("CSE")
    # year
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[4]/div/div[2]/input').send_keys("2025")

    # GPA
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys("3.85")

    # start date
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input').send_keys("2020-25-1")

    # end date
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys("2025-30-6")

    education_save = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[3]/button[2]').click()
    print('--------------------------education save success ------------------------')
    time.sleep(5)

    # member ship click 
    print('-----------------member ship click for <a> TAG---------------------- ')
    driver.find_element(By.LINK_TEXT, "Memberships").click()
    time.sleep(2)
    assingned_membership_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
    time.sleep(1)

    # membership dropdown click start 
    print('membership dropdown click -------------------- start')
    member_ship_dropdown_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    driver.find_element(By.XPATH, member_ship_dropdown_xpath).click()
    print('membership dropdown click -------------------- end')
    time.sleep(1)

    # Get and print selected text 
    member_ship_selected_value_xpath = member_ship_dropdown_xpath + '/div[@class="oxd-select-text-input"]'
    member_ship_selected_value = driver.find_element(By.XPATH, member_ship_selected_value_xpath).text
    print("Selected value:", member_ship_selected_value)

    # Print all visible dropdown options
    options = driver.find_elements(By.XPATH, '//div[contains(@class,"oxd-select-dropdown")]//div')
    print("Dropdown options:")
    for opt in options:
        print("--", opt.text)
    
    # college
    print('selelct the membeship option --------------start')
    option_xpath = '//div[contains(@class,"oxd-select-dropdown")]//div[@role="option"]/span[text()="British Computer Society (BCS)"]'
    driver.find_element(By.XPATH, option_xpath).click()
    print('selelct the membeship option --------------end')
    time.sleep(1)

    # membership dropdown click end

    # subscription dropdown click start 
    print('subscription dropdown click -------------------- start')
    subscription_dropdown_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    driver.find_element(By.XPATH, subscription_dropdown_xpath).click()
    print('dropdown click -------------------- end')
    time.sleep(2)

    # Get and print selected text 
    subscription_selected_value_xpath = subscription_dropdown_xpath + '/div[@class="oxd-select-text-input"]'
    subscription_selected_value = driver.find_element(By.XPATH, subscription_selected_value_xpath).text
    print("Selected value:", subscription_selected_value)

    # Print all visible dropdown options
    options = driver.find_elements(By.XPATH, '//div[contains(@class,"oxd-select-dropdown")]//div')
    print("Dropdown options:")
    for opt in options:
        print("--", opt.text)
    
    # college
    print('selelct the subscription option --------------start')
    option_xpath = '//div[contains(@class,"oxd-select-dropdown")]//div[@role="option"]/span[text()="Company"]'
    driver.find_element(By.XPATH, option_xpath).click()
    print('selelct the subscription option --------------end')
    time.sleep(1)

    # subscription dropdown click end

    # subscription amount 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys("100")

     # currency dropdown click start 
    print('currency dropdown click -------------------- start')
    currency_dropdown_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    driver.find_element(By.XPATH, currency_dropdown_xpath).click()
    print('dropdown click -------------------- end')
    time.sleep(1)

    # Get and print selected text 
    currency_selected_value_xpath = currency_dropdown_xpath + '/div[@class="oxd-select-text-input"]'
    currency_selected_value = driver.find_element(By.XPATH, currency_selected_value_xpath).text
    print("Selected value:", currency_selected_value)

    # Print all visible dropdown options
    options = driver.find_elements(By.XPATH, '//div[contains(@class,"oxd-select-dropdown")]//div')
    # print("Dropdown options:")
    # for opt in options:
    #     print("--", opt.text)
    
    # college
    print('selelct the currency option --------------start')
    option_xpath = '//div[contains(@class,"oxd-select-dropdown")]//div[@role="option"]/span[text()="Bangladeshi Taka"]'
    driver.find_element(By.XPATH, option_xpath).click()
    print('selelct the currency option --------------end')
    time.sleep(1)

    # currency dropdown click end

    subscription_commence_date = "2025-31-07"
    subscription_renewal_date = "2025-31-08"

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/input').send_keys(subscription_commence_date)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/input').send_keys(subscription_renewal_date)


    # memrship add button click 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/button[2]').click()

    # attachment start 
    attachment_add_btn = driver.find_element(By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='button'][normalize-space()='Add']").click()
    print('attachment button clicked')
    time.sleep(1)

    # Upload PDF file
    print('uploading PDF file -------------------- start')
    pdf_file_path = "C:\\Users\\User\\Downloads\\ss.pdf"  # Replace with your PDF file path
    if not os.path.exists(pdf_file_path):
        raise Exception(f"PDF file not found at: {pdf_file_path}")
    file_input = driver.find_element(By.XPATH, '//input[@type="file" and @class="oxd-file-input"]')
    file_input.send_keys(pdf_file_path)
    print('uploading PDF file -------------------- end')
    time.sleep(1)  # Wait for upload to process

    driver.find_element(By.XPATH, "//textarea[@placeholder='Type comment here']").send_keys('add our sub')
    # save
    driver.find_element(By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']").click()
    time.sleep(5)

    # logout start
    driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    time.sleep(1)

    login_text = driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").text

    print('loign text : ', login_text)

    if 'Login' in login_text:
        print('logout success ----------------------- ')


    time.sleep(10)
except Exception as e:
    print(f"Test Failed ❌ : {e}")

