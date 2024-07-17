from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Function to initialize the WebDriver (Chrome in this case)
def initDriver():
    driver = webdriver.Chrome()
    return driver

# Function to define user input fields (dummy data for demonstration)
def input_user_fields():
    name = "Dev Patel"
    contact_no = "8734835064"
    email = "pateldev21304@gmail.com"
    full_addr = "Harshad society hansol sardarnagar Ahmedabad, Gujarart, India"
    pin_code = "382475"
    dob = "21-03-2004"  # Date of Birth
    gender = "male"

    return {
        "name": name,
        "contact_no": contact_no,
        "email": email,
        "full_address": full_addr,
        "pin_code": pin_code,
        "DOB": dob,
        "gender": gender
    }

# Function to fill out the form
def fill_form():
    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"  # URL of the Google Form
    driver = initDriver()  # Initialize WebDriver
    driver.get(form_url)  # Open the Google Form URL
    data_fields = input_user_fields()  # Get dummy data for form fields

    # XPath selectors for each input field in the form
    name_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
    contact_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
    email_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
    address_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea"
    pin_code_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input"
    dob_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input"
    gender_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input"
    human_verify_code = "//*[@id='i30']/span[1]/b"
    verify_xpath = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input"

    sleep(2)  # Wait for 2 seconds to ensure the form is fully loaded

    # Locate each form input field by XPath and interact with them
    n_obj = driver.find_element(By.XPATH, name_xpath)
    n_obj.click()  # Click on the input field
    n_obj.send_keys(data_fields.get("name"))  # Enter the name

    cno_obj = driver.find_element(By.XPATH, contact_xpath)
    cno_obj.click()
    cno_obj.send_keys(data_fields.get("contact_no"))  # Enter the contact number

    email_obj = driver.find_element(By.XPATH, email_xpath)
    email_obj.click()
    email_obj.send_keys(data_fields.get("email"))  # Enter the email address

    address_obj = driver.find_element(By.XPATH, address_xpath)
    address_obj.click()
    address_obj.send_keys(data_fields.get("full_address"))  # Enter the full address

    pin_code_obj = driver.find_element(By.XPATH, pin_code_xpath)
    pin_code_obj.click()
    pin_code_obj.send_keys(data_fields.get("pin_code"))  # Enter the PIN code

    dob_obj = driver.find_element(By.XPATH, dob_xpath)
    dob_obj.click()  # Click on the date of birth input field

    # Split the date string into day, month, and year components
    day, month, year = data_fields.get("DOB").split("-")

    # Send keys to input the date of birth in the format day, month, year
    dob_obj.send_keys(Keys.TAB)  # Move focus to the next field (day)
    dob_obj.send_keys(day)  # Enter the day
    dob_obj.send_keys(month)  # Enter the month
    dob_obj.send_keys(year)  # Enter the year

    gender_obj = driver.find_element(By.XPATH, gender_xpath)
    gender_obj.click()
    gender_obj.send_keys(data_fields.get("gender"))  # Enter the gender

    # Fetch and input the verification code (if any) from the form
    human_code_obj = driver.find_element(By.XPATH, human_verify_code)
    verification_code = human_code_obj.text

    verify_code_obj = driver.find_element(By.XPATH, verify_xpath)
    verify_code_obj.click()
    verify_code_obj.send_keys(verification_code)  # Enter the verification code

    sleep(3)  # Wait for 15 seconds before quitting the driver

    submit_xpath = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div"
    submit_btn = driver.find_element(By.XPATH, submit_xpath)
    submit_btn.click()

    sleep(7)
    driver.quit()  # Close the WebDriver session

# Call the function to execute the form filling process
fill_form()
