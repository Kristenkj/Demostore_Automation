### 🚀 Custom Hybrid Automation Framework for DEMO E-commerce Site - In progress


## Project Description
Hello, I am Kristen!

For this project, I created a hybrid web automation framework utilizing the page object model (POM) design pattern in Selenium 
In addition, I validated the functionality and user interactions of the e-commerce-based site using automated tests with Selenium Webdriver.

The site that was used: [Demo e-commerce store practice site](http://demostore.supersqa.com/)

## Table of Contents

- [Test Cases](#test-cases)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Test Cases

The automated test cases cover the following functionalities:
* Product Listing and Purchase: Tests the process of browsing products and completing a purchase.
* Form Validations: Checks form validations and error messages.
* Account registration and Login: Creating an account and logging in
* Applying Coupons: Utilizing coupons to test functionality


## Technologies Used

- Python 3.12: Programming Language
- Pytest: Framework for writing and running tests
- Selenium Webdriver: For browser Automation
- Openpyxl: For handling Excel files
- Logger: For logging test execution details
- Jenkins: For CI/CD
- Faker: For generating fake data for testing
- Random: For generating random emails and passwords

## Project Structure

```
demostore/
└── autoFramework/  
    ├── configs                                   # Configuration files
         └── ggeneric_configs
    ├── Logs/                                     # Log files
        ├── logfile.log
    ├── extensions/                 
        ├── SeleniumExtended
    ├── reports/                                  # Test reports
        └── allure-results                        # Allure results directory
    ├── pageObjects/                              # Page Object Models
            └── locators/
                ├── CartPageLocators                
                ├── ChecoutPageLocators
                ├── HomePageLocators
                ├── MyAccountSignedInLocators
                ├── MyAcctSignOutLocators
                ├── OrderReceivedPageLocators
                └── HeaderLocators
        ├── checkOutPage.py
        ├── cartPage.py
        ├── homePage.py
        ├── MyAcctSignInPage.py
        ├── MyAcctSignOutPage.py
        ├── Header.py
        └── orderReceivedPage.py
    ├── screenshots/                               # Screenshots of test execution
        ├── CheckoutPage.py
        ├── ConfirmPage.py
        ├── HomePage.py
        ├── ShopPage.py
    ├── testCases/                                 # Test files
        ├── end_to_end/
            ├── test_end_to_end_checkout_guest_user_story.py
        ├── my_account/
            ├── test_login_negative.py
            └── test_register_new_user.py
        └── test_dummy.py
    ├── testData/                                  # Test data files
        └── test_form_validations.py
    ├── utils/                                     # Utility functions
        ├── helpers.py
            └── generic_helpers.py
        ├── BaseClass.py
        └── excel_utils.py                       # Excel handling functions using openpyxl
    ├── conftest.py                              # Configuration for pytest
    ├── requirements.txt                         # Project dependencies
    └── README.md                                # Project documentation

```

## Contact
For any questions or inquiries, contact me at:

- Subject Line: Proto Commerce - questions/inquiry
- Email: jonesbkristen@gmail.com

- Github: [Kristen's GitHub Profile](https://github.com/Kristenkj)
