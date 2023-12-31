# IKEA Website Test Automation Project

This is a test automation project to perform end-to-end testing on the IKEA website. The project utilizes Python, Selenium, and Allure reporting to ensure the website's functionalities are working correctly.

## Project Structure

The project is organized into the following directories:

1. **assets:** Contains any necessary resources like images, test data, or configuration files.

2. **pages:** Includes page objects that model the different pages of the IKEA website. These page objects encapsulate the elements and actions specific to each page.

3. **tests:** Contains the test scripts that execute the test cases on the IKEA website. The test cases are designed to cover various scenarios to ensure proper functionality.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- Selenium WebDriver
- Allure Framework (for reporting)

## Installation

1. Clone this repository to your local machine.

2. Install the required Python packages using the following command:

   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the appropriate web drivers for the browsers you intend to use (e.g., Chrome, Firefox). Download and place the driver executables in a directory included in your system's PATH.

## Running Tests

To execute the test cases, run the following command from the project root:

```
pytest --alluredir=reports
```

This command will run all the test scripts in the `tests` directory and generate test reports in the `reports` directory using Allure.

## Viewing Test Reports

To view the test reports generated by Allure, run the following command:

```
allure serve reports
```

This will launch a local server displaying the test reports. You can access the reports by navigating to the provided URL in your web browser.

## Test Coverage

The test cases cover various aspects of the IKEA website, including:

- Homepage navigation and content verification.
- Product search and listing functionalities.
- Product details and description verification.
- Shopping cart interactions, such as adding/removing items and verifying cart contents.
- Checkout process, including entering shipping and payment information.
- User registration and login functionality.

## Contributing

We welcome contributions to this test automation project. If you find any issues or have suggestions for improvements, please create a pull request, and we will be happy to review it.



