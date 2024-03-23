<a name="readme-top"></a>

<p align="center">
  <img src="https://raw.githubusercontent.com/AlexisRodriguezCS/AutoTesterPy/main/images/selenium.png" alt="selenium.png" style="display:block;margin:auto;" height="500">
</p>
<h1 align="center">AutoTesterPy</h1>

<!-- TABLE OF CONTENTS -->
<p align="center">
  <a href="#about">About The Project</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#usage">Usage</a> •
  <a href="#contact">Contact</a>
</p>

<!-- ABOUT THE PROJECT -->

<a name="about"></a>

## About The Project

Welcome to my project, where I showcase my QA skills using Python, pytest, Selenium, and Docker. Through this project, I aim to demonstrate my proficiency in automating testing processes and ensuring software quality.

Using the website [Automation Exercise](https://automationexercise.com/), I've implemented a range of test cases to cover essential functionalities such as registering users, logging in with correct and incorrect credentials, logging out users, and handling scenarios like registering users with existing email addresses.

By leveraging the power of Python for scripting, pytest for test organization and execution, Selenium for web automation, and Docker for containerization, I've created a robust testing framework capable of efficiently validating the functionality and reliability of web applications.

Whether it's ensuring smooth user experiences or identifying and fixing potential issues, this project serves as a testament to my dedication to quality assurance and my ability to deliver reliable software solutions.

### Key Technologies Used

- Python <img align="left" alt="Python" width="30px"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />: A programming language used for backend development and automation tasks.

- Pytest <img align="left" alt="Pytest" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" />: A testing framework for Python, commonly used for unit testing and functional testing.

- Selenium <img align="left" alt="Selenium" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" />: A tool primarily employed for automating web browsers, often used for web application testing.

- Docker <img align="left" alt="Docker" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" />: A containerization platform used for packaging applications and their dependencies into containers for easy deployment and scalability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

<a name="project-structure"></a>

## Project Structure

The testing application is organized into the following directories:

- `\pages` : Pages files provide a set of instructions for navigating and interacting with specific parts of a website, like filling out forms or clicking buttons, making it easier to automate tasks without needing to know the technical details.
- `\tests` : Test files are like a checklist of actions to confirm that a website or application works correctly, ensuring that users can perform tasks like signing up or logging in without any problems.
- `\fixtures` : conftest.py sets up the browser, loads environment variables, navigates to a URL, verifies the home page, and closes the browser after each test.

#### Pages

| File                                   | Description                                        |
| -------------------------------------- | -------------------------------------------------- |
| BasePage.py:                           | Base class for interacting with web elements.      |
| AuthPageLocators.py:                   | Locators and methods for authentication.           |
| AccountCreationPageLocators.py:        | Locators and methods for account creation.         |
| AccountCreationSuccessPageLocators.py: | Locators and methods for account creation success. |
| AccountDeletionPageLocators.py:        | Locators and methods for account deletion.         |
| HeaderLocators.py:                     | Locators and methods for the main page header.     |
| TestCasesPage.py                       | Locators and methods for test case page.           |
| HomePageLocators.py                    | Locators and methods for home page.                |
| ContactUsPageLocators.py               | Locators and methods for contact us page.          |

#### Tests

| File                                                | Description                                                                |
| --------------------------------------------------- | -------------------------------------------------------------------------- |
| test_register_user.py:                              | Testing the registration process, and deleting the account.                |
| test_login_user_correct_credentials.py              | Testing the login process with correct email and password.                 |
| test_login_user_incorrect_credentials.py            | Testing the login process with incorrect email and password.               |
| test_logout_user.py                                 | Testing the logout process.                                                |
| test_register_existing_email.py                     | Testing the registration process with an existing email.                   |
| test_contact_us_form.py                             | Testing the contact us form functionality.                                 |
| test_verify_test_cases_page.py                      | Testing the functionality to verify the test cases page.                   |
| test_verify_all_products_and_product_detail_page.py | Testing the functionality to verify all products and product detail pages. |
| test_search_product.py                              | Testing the functionality to search for a product.                         |
| test_verify_subscription_home_page.py               | Testing the subscription functionality on the home page.                   |
| test_verify_subscription_cart_page.py               | Testing the subscription functionality on the cart page.                   |
| test_add_products_in_cart.py                        | Testing the functionality to add products to the cart.                     |
| test_verify_product_quantity_in_cart.py             | Testing the functionality to verify product quantity in the cart.          |

Other files like .env and data files are utilized within the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

<a name="getting-started"></a>

## Getting Started

To set up a project locally, follow these simple steps.

### Prerequisites

_Software used to run the program._

- [Visusal Studio Code](https://code.visualstudio.com/)<img align="left" alt="Visual Studio Code" width="30px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" />

- [Python](https://www.python.org/downloads/)<img align="left" alt="Python" width="30px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />

- [ChromeDriver](https://chromedriver.chromium.org/)<img align="left" alt="ChromeDriver" width="30px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original.svg" />

- [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing)<img align="left" alt="Chrome for Testing" width="30px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-plain.svg" />

- [Git](https://git-scm.com/)<img align="left" alt="Git" width="30px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" />

### Installation

_Here's how to install and set up the program locally._

From your command line:

```bash
# Clone this repository
$ git clone https://github.com/AlexisRodriguezCS/AutoTesterPy.git

# Go into the repository
$ cd AutoTesterPy

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment
$ venv\Scripts\activate

# Install the Python packages listed in a requirements.txt
$ pip install -r requirements.txt

# Run the tests using pytest
$ pytest
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DOCKER -->

<a name="docker"></a>

## Docker

Docker makes it easy to build and run software by putting everything it needs into small packages, so it works the same way no matter where it's used.

**Method 1**: Using Dockerfile to Build Image and Container.

```bash
# Build Docker Image
docker build -t autotesterpy-image .

# Run Docker Container
docker run -d autotesterpy-image
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

<a name="contact"></a>

## Contact

Alexis Rodriguez

- [LinkedIn](https://www.linkedin.com/in/alexisrodriguezcs/)<img align="left" alt="LinkedIn" width="25px" style="padding-right:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" />

- [alexisrodriguezdev@gmail.com](alexisrodriguezdev@gmail.com)<img align="left" alt="Email" width="25px" style="padding-right:5px;" src="https://img.icons8.com/emoji/48/e-mail.png" />

Project Link: [https://github.com/AlexisRodriguezCS/AutoTesterPy.git](https://github.com/AlexisRodriguezCS/ValentineProposal.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
