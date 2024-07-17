from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'devpatel1828king@gmail.com'
app.config['MAIL_PASSWORD'] = 'hxzkyawmduixcluh'
mail = Mail(app)


# Define the route for sending the email
@app.route('/send-email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = 'pateldev21304@gmail.com'
        cc_recipient = 'pateldev21304@gmail.com'
        subject = 'Python (Selenium) Assignment - [Dev Patel]'
        form_screenshot = r'documents/formfilled.png'
        github_repo = 'https://github.com/DevPatel1479/AutomateGoogleForm/tree/master/PycharmProjects/GoogleFormAutomation'
        email_sending_code_repo = ''
        documentation = """
        Brief Documentation of the Approach

        The goal of this script is to automate the process of filling out a Google Form using Selenium WebDriver. 
        Below is a brief explanation of the approach taken:

        1. Initialization:
            - WebDriver Initialization: A Chrome WebDriver session is initialized using the `webdriver.Chrome()` function. 
              This sets up a new instance of the Chrome browser which will be used to interact with the Google Form.

        2. User Input Fields Definition:
            - Dummy Data Setup: A function `input_user_fields` is defined to return a dictionary containing sample data for each field in the form. 
                This includes fields such as name, contact number, email, full address, PIN code, date of birth, and gender.

        3. Form Filling:
            - Form URL: The URL of the Google Form to be filled is specified.
            - Field Locators: XPath selectors are used to locate each input field in the form. 
              These selectors correspond to the different form fields (name, contact number, email, etc.).
            - Data Input: Using the Selenium WebDriver, the script locates each form input field by its XPath and inputs the corresponding data from the 
              dictionary. This is done using the `send_keys` method.
            - Special Handling for Date of Birth: The date of birth field is filled by splitting the date string into day, month, and year components and 
              then sending each part separately to the input field.
            - Verification Code: If there is a human verification code, it is fetched and inputted into the appropriate field.
            - Form Submission : After all fields are filled, the form is submitted by clicking the submit button.

        4. Finalization:
            - Waiting Period: The script includes sleep commands to wait for a few seconds to ensure the form is fully loaded and submitted.
            - Driver Quit: Finally, the WebDriver session is closed using the `driver.quit()` command.

        This approach automates the entire process of filling and submitting a Google Form using Selenium, ensuring that each field is correctly filled 
        with the provided dummy data.
        """
        resume = r'documents/DevPatel_InternshalaResume.pdf'
        project_links = 'Links to past projects/work samples'

        msg = Message(subject, sender='devpatel1828king@gmail.com', recipients=[recipient], cc=[cc_recipient])
        msg.body = f"""
        Please find the assignment details below:
    
        1. Screenshot of the form filled via code.
        2. Source code: {github_repo}
           - email sending code : {email_sending_code_repo}
        3. Brief documentation{documentation}.
        4. My resume.
        5. Links to past projects/work samples: {project_links}
        6. Yes, I am available to work . 
        """

        # Attach the screenshot
        with app.open_resource(form_screenshot) as fp:
            msg.attach(form_screenshot, 'image/png', fp.read())

        # Attach the resume
        with app.open_resource(resume) as fp:
            msg.attach('resume.pdf', 'application/pdf', fp.read())

        # Send the email
        mail.send(msg)
        return 'Email sent successfully'
    return render_template('send_email.html')


if __name__ == '__main__':
    app.run(debug=True)
