import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FfOptions
import os  # Import the os module for interacting with the operating system


# 1. this section of code is a fixture that will set up the webdriver
@pytest.fixture(scope="class")  # Define a fixture called 'init_driver' with scope set to 'class'
def init_driver(request):  # Define a function named 'init_driver' to set up the WebDriver
    global driver  # Declare that we're using the global variable 'driver' within this function
    pass  # Placeholder statement, does nothing

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']  # Define a list of supported browsers

    browser = os.environ.get('BROWSER', 'Chrome')  # Get the value of the 'BROWSER' environment variable
    if not browser:  # Check if 'BROWSER' environment variable is not set
        raise Exception('The environment variable "BROWSER" must be set.')  # Raise an exception if 'BROWSER' is not set

    browser = browser.lower()  # Convert the browser name to lowercase
    if browser not in supported_browsers:  # Check if the chosen browser is not in the list of supported browsers
        raise Exception(f"Provided '{browser}' is not one of the supported."  # Raise an exception if the browser is not supported
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):  # Check if the chosen browser is Chrome or 'ch' (assuming it's a typo)
        driver = webdriver.Chrome()  # Create a Chrome WebDriver instance
    elif browser in ('firefox', 'ff'):  # Check if the chosen browser is Firefox or 'ff' (assuming it's a typo)
        driver = webdriver.Firefox()  # Create a Firefox WebDriver instance

#### this whole thing basically checks if the browser is headless or not. meaning if the browser is headless then it will not open the browser window and run the test in the background
    elif browser == 'headlesschrome':  # Check if the chosen browser is headless Chrome
        chrome_options = ChOptions() # Create a ChromeOptions instance
        chrome_options.add_argument("--disable-gpu")  # Add the '--disable-gpu' argument to the Chrome options
        chrome_options.add_argument("--no-sandbox")  # Add the '--headless' argument to the Chrome options
        chrome_options.add_argument("--headless")  # Add the '--headless' argument to the Chrome options
        driver = webdriver.Chrome(options=chrome_options) #
#### if you want to see if tests are acctually running, input in cmd pytest -m tcid12 -s --log-cli-level=DEBUG

# do the same thing for firefox browser
    elif browser == 'headlessfirefox': # Check if the chosen browser is headless Firefox
        firefox_options = FfOptions() # Create a FirefoxOptions instance
        firefox_options.add_argument("--headless") # Add the '--headless' argument to the Firefox options
        firefox_options.add_argument("--disable-gpu") # Add the '--disable-gpu' argument to the Firefox options
        firefox_options.add_argument("--no-sandbox") # Add the '--no-sandbox' argument to the Firefox options
        driver = webdriver.Firefox(options=firefox_options)  # Create a Firefox WebDriver instance
#### if you want to see if tests are acctually running, input in cmd pytest -m tcid12 -s --log-cli-level=DEBUG

    else:  # If the chosen browser is not recognized, raise an exception
        raise Exception(f"Provided '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    request.cls.driver = driver  # Attach the WebDriver instance to the test class. Any test methods within the test class can use self.driver
    yield  # Indicates the end of setup and the beginning of the test execution. 

### our test exicution

    driver.quit()  # Quit/close the WebDriver instance after the test execution










# 2. this section of code generates a url, image or any other file that can be attached to the report
import pytest
import pytest_html


@pytest.hookimpl(hookwrapper=True) # this is a hook that will add a url to the report and additional html on failure
def pytest_runtest_makereport(item, call): # this is a function that will make a report of the test
    outcome = yield #  yield is a keyword that is used like return, except the function will return a generator
    report = outcome.get_result() # get the result of the outcome
    extras = getattr(report, "extra", []) # get the extra attribute of the report

    if report.when == "call": # if the report is called
        extras.append(pytest_html.extras.url("http://www.example.com/")) # append the url to the report
        xfail = hasattr(report, "wasxfail") # if the report was expected to fail
       
        if (report.skipped and xfail) or (report.failed and not xfail): # if the report was skipped and expected to fail or if the report failed and was not expected to fail
            is_frontend = True if 'init_driver' in item.fixturenames else False # if the fixture name is init_driver then it is a frontend test
            
            if is_frontend: # if it is a frontend test do this
                # change the results_dir to set a defalt directory as 
                
                results_dir = os.environ.get('RESULTS_DIR', r'C:\Users\srutz\OneDrive - Centuri Group, Inc\Documents\GitHub\QAAutomationCourse\Pytest\results') # The .get() method is used to retrieve the value of an environmental variable.
                                                            # In this case, it looks for an environmental variable named 'RESULTS_DIR'.
                                                            # If the variable exists, it returns its value; otherwise, it returns None.
                if not results_dir:
                    raise Exception('The environment variable "RESULTS_DIR" must be set.') # raise an exception if the results directory is not set
                
                screenshot_path = os.path.join(results_dir, item.name + '.png') # if you put pdb after it, it will show the name of the test you are running (item.name) and the .png extension
                                                                                # results_dir is the directory where the results are stored
                driver_fixture = item.funcargs['request'] # on line 50 we attached the driver to the test class, and we access it here. from item we are accessing the request object and setting it to driver_fixture
                driver_fixture.cls.driver.save_screenshot(screenshot_path) # save the screenshot to the results directory. save_screenshot is a selenium method and screenshot_name is PNG 

                # extras.append(pytest_html.extras.html('<div>Additional HTML</div>') # append additional html to the report
                extras.append(pytest_html.extras.image(screenshot_path)) # append additional html to the report
        report.extras = extras # add the extras to the report
        
    



