# Python Web and Backend Framework for Sporty

This is the test automation project for the Sporty challenge.

## Technologies

The automated tests are build in Python, the framework is "PyTest" and it uses also "Selenium" to interact with the Web page.

## Requirements

Before running the automated tests, the user needs to have configured and installed the following requirements according to it's O.S : 

- Python
- Google Chrome

## Structure of the Project

```
.
├── backend => Classes needed to run backend tests
│   ├── clients => Folder that contains the clients
│        ├── base => Base classes
├── config => Classes for configuration of the project
├── pages => Folder that contains the page objects
├── tests => Folder that contains the test cases
├── utils => Folder with util classes and methods
├── requirements.txt ==> TXT file with the dependencies of the project
└── README.md
```

## Running the tests

Once you download this project locally, you have to install all the dependencies (just once).
Follow these steps to install the dependencies in a virtual environment :

To configure dependencies:

- cd tests/integration
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

To run the tests follow these steps : 

1. cd tests/integration
1. Enter to the virtual environment running the commands "source venv/bin/activate" 
1. Run 1 Test
    - pytest --html=pytest_report.html tests/test_twitch.py
    - pytest --html=pytest_report.html tests/test_backend.py
1. Run tests all the tests
    1. Chrome: "pytest --html=pytest_report.html" or "python3 pytest --html=pytest_report.html". 
    1. Mobile emulation: "pytest --browser mobile --html=pytest_report.html" or "python3 pytest --browser mobile --html=pytest_report.html".
    1. Chrome Headless: pytest --browser chrome_headless --html=pytest_report.html
    1. Firefox : pytest --browser firefox --html=pytest_report.html

1. Once the execution is finished you should see an HTML file generated automatically with a report of the execution

## Maintaining the Tests
When a test is executed, two important parts are used to run the scenario : 

- PageObject
- Instructions in the test

There are occasions where an element in the page is changed (a button, a textbox, etc.) so the locator doesn't work anymore and the test fail because 
the element was not found according to the locator that we entered.
To fix this issue you should go to the pageobject class (in pages folder) and change the locator.

In order to find the new locator you should open the console in Chrome, find the element and create an according locator (Simple guide here : https://www.browserstack.com/guide/locators-in-selenium) 

There are other occasions where the steps to perform an action changes, so we have to change the steps in the Test.
To do this just add/remove the steps in the _test.py class.

If a test doesn't apply anymore, you can remove it or skip it adding the marker @pytest.mark.skip above the test method or the class.

