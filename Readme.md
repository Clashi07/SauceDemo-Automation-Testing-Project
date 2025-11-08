# SauceDemo Automation Testing Project

This project contains automated test scripts for the [SauceDemo](https://www.saucedemo.com/) website using Python, Selenium, and Pytest with Allure reporting.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Test Scenarios](#test-scenarios)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Execution Instructions](#execution-instructions)
- [Allure Report Generation](#allure-report-generation)
- [Technologies Used](#technologies-used)

---

## 🎯 Project Overview

This automation framework tests the complete e-commerce functionality of the SauceDemo application, including authentication, product selection, cart management, and checkout process.

---

## 📝 Test Scenarios

### Q1: Locked Out User Test (20 Marks)
- **User**: `locked_out_user`
- **Steps**:
  1. Attempt login with locked user credentials
  2. Verify error message is displayed
  3. Validate error message text: "Epic sadface: Sorry, this user has been locked out."

### Q2: Standard User Purchase Journey (50 Marks)
- **User**: `standard_user`
- **Steps**:
  1. Login successfully
  2. Reset application state from hamburger menu
  3. Add three products to cart:
     - Sauce Labs Backpack
     - Sauce Labs Bike Light
     - Sauce Labs Bolt T-Shirt
  4. Navigate to cart
  5. Proceed to checkout
  6. Fill checkout information
  7. Verify product names and total price on final checkout page
  8. Complete purchase
  9. Verify success message
  10. Reset app state again
  11. Logout

### Q3: Performance User with Sorting (30 Marks)
- **User**: `performance_glitch_user`
- **Steps**:
  1. Login successfully
  2. Reset application state
  3. Sort products by name (Z to A)
  4. Verify first product is "Test.allTheThings() T-Shirt (Red)"
  5. Add first product to cart
  6. Navigate to checkout
  7. Verify product name and total price
  8. Complete purchase
  9. Verify success message
  10. Reset app state
  11. Logout

---

## 🔧 Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Google Chrome Browser** - [Download Chrome](https://www.google.com/chrome/)
- **Git** - [Download Git](https://git-scm.com/downloads)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Clashi07/SauceDemo-Automation-Testing-Project
cd saucedemo-automation

2. Create Virtual Environment
Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt
requirements.txt should contain:

selenium==4.15.2
pytest==7.4.3
pytest-html==4.1.1
pytest-metadata==3.1.1
allure-pytest==2.13.2
webdriver-manager==4.0.1

📁 Project Structure
saucedemo-automation/
│
├── pages/                          
│   ├── __init__.py
│   ├── base_page.py               # Base page with common methods
│   ├── login_page.py              # Login page objects
│   ├── inventory_page.py          # Product inventory page objects
│   ├── cart_page.py               # Shopping cart page objects
│   └── checkout_page.py           # Checkout page objects
│
├── tests/                          # Test files
│   ├── __init__.py
│   ├── conftest.py                # Pytest configuration and fixtures
│   ├── test_q1_locked_user.py     # Q1 test scenario
│   ├── test_q2_standard_user.py   # Q2 test scenario
│   └── test_q3_performance_user.py # Q3 test scenario
│
├── allure-results/                 # Allure test results (generated)
├── screenshots/                    # Screenshots on failure (generated)
├── venv/                          # Virtual environment (excluded from git)
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
└── README.md                      # This file

▶️ Execution Instructions
Run All Tests
pytest tests/ --alluredir=allure-results -v

Run Individual Test Scenarios
Q1 - Locked User Test:

pytest tests/test_q1_locked_user.py --alluredir=allure-results -v

Q2 - Standard User Test:

pytest tests/test_q2_standard_user.py --alluredir=allure-results -v

Q3 - Performance User Test:

pytest tests/test_q3_performance_user.py --alluredir=allure-results -v

Run Tests with Specific Markers
pytest -m q1 --alluredir=allure-results -v
pytest -m q2 --alluredir=allure-results -v
pytest -m q3 --alluredir=allure-results -v

Run Tests with Console Output
pytest tests/ --alluredir=allure-results -v -s

Run Tests Sequentially (All Three)
pytest tests/test_q1_locked_user.py tests/test_q2_standard_user.py tests/test_q3_performance_user.py --alluredir=allure-results -v

📊 Allure Report Generation
1. Install Allure Commandline
Windows (using Scoop):

scoop install allure

macOS (using Homebrew):

brew install allure

Linux:

sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure

2. Generate and View Report
After running tests, generate the Allure report:
allure serve allure-results
This will automatically open the report in your default browser.

3. Generate Static Report
To generate a static HTML report:

allure generate allure-results --clean -o allure-report

Then open the report:

allure open allure-report

🛠️ Technologies Used
Technology	Version	Purpose
Python	3.13.1	Programming Language
Selenium WebDriver	4.15.2	Browser Automation
Pytest	7.4.3	Testing Framework
Allure	2.13.2	Test Reporting
WebDriver Manager	4.0.1	Automatic Driver Management
Page Object Model	-	Design Pattern
🐛 Troubleshooting
ChromeDriver Issues
If you encounter ChromeDriver errors:

Clear cached drivers:

# Windows
rmdir /s %USERPROFILE%\.wdm\drivers\chromedriver
# macOS/Linux
rm -rf ~/.wdm/drivers/chromedriver

Update Chrome browser to the latest version

Reinstall webdriver-manager:

pip uninstall webdriver-manager
pip install webdriver-manager

Test Failures
Ensure stable internet connection
Check if SauceDemo website is accessible
Increase wait times in conftest.py if using slower system
Run tests in non-headless mode for debugging (comment out --headless in conftest.py)
📝 Test Credentials
Username	Password	Purpose
locked_out_user	secret_sauce	Q1 - Error validation
standard_user	secret_sauce	Q2 - Complete purchase flow
performance_glitch_user	secret_sauce	Q3 - Sorting & performance test
📧 Contact
For any queries or issues, please contact:

Email: your.email@example.com
GitHub: Your GitHub Profile
📄 License
This project is created for educational and assessment purposes.

✅ Checklist Before Submission
 All three test scenarios pass successfully
 Allure report generated without errors
 Code pushed to GitHub public repository
 README.md is complete and accurate
 requirements.txt includes all dependencies
 .gitignore excludes venv and unnecessary files
Last Updated: November 2024
Author: IFTE KHARUL ISLAMNIHAL
Assessment: SauceDemo Automation Testing Project

---
## **Also create a `.gitignore` file:**
```gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Pytest
.pytest_cache/
.tox/
*.log

# Allure
allure-results/
allure-report/
# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
# Screenshots
screenshots/
*.png
*.jpg
# WebDriver
.wdm/
chromedriver.exe
geckodriver.exe
# Coverage
htmlcov/
.coverage
.coverage.*
coverage.xml
*.cover

