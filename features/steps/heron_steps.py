from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

@given('I enter 25 into the element a')
def input_a(context):
    try:
        # Locate the span element using its class name
        a = context.behave_driver.find_element(By.ID, "a")

        # Clear any existing text in the input element
        a.clear()
        
        # Enter the number 2 into the input element
        a.send_keys("25")
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@given('I enter 35 into the element b')
def input_a(context):
    try:
        # Locate the span element using its class name
        b = context.behave_driver.find_element(By.ID, "b")

        # Clear any existing text in the input element
        b.clear()
        
        # Enter the number 2 into the input element
        b.send_keys("35")
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@when('I first click the calculate button')
def click_calculate(context):
    try:
        # Wait for up to 5 seconds for the element to be clickable
        WebDriverWait(context.behave_driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "clcbtn"))
        )
    except Exception as e:
        assert False, f"Failed to wait for the button: {str(e)}"
    
    try:
        # Locate the input element by its ID

        
        calculate = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")
        time.sleep(3)
        
        calculate.click()
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@then('there should be a pop up stating: "{expected_text}"')
def confirm_area(context, expected_text):

    try:
        # Try switching to the alert
        alert = context.behave_driver.switch_to.alert
        assert alert is not None, "Alert is not present."
        alert_text = alert.text
        assert alert_text == expected_text, f"Expected value '{expected_text}', but got '{alert_text}'."
        alert.accept()
        time.sleep(3)
    except NoAlertPresentException:
        assert False, "No alert is present on the page."
    

@given('I enter 2 into the element a')
def input_a(context):
    try:
        # Locate the span element using its class name
        a = context.behave_driver.find_element(By.ID, "a")

        # Clear any existing text in the input element
        a.clear()
        
        # Enter the number 2 into the input element
        a.send_keys("2")
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@given('I enter 3 into the element b')
def input_a(context):
    try:
        # Locate the span element using its class name
        b = context.behave_driver.find_element(By.ID, "b")

        # Clear any existing text in the input element
        b.clear()
        
        # Enter the number 2 into the input element
        b.send_keys("3")
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@given('I enter 4 into the element c')
def input_c(context):
    try:
        # Locate the span element using its class name
        c = context.behave_driver.find_element(By.ID, "c")

        # Clear any existing text in the input element
        c.clear()
        
        # Enter the number 2 into the input element
        c.send_keys("4")
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@when('I click the calculate button')
def click_calculate(context):
    try:
        # Wait for up to 5 seconds for the element to be clickable
        WebDriverWait(context.behave_driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "clcbtn"))
        )
    except Exception as e:
        assert False, f"Failed to wait for the button: {str(e)}"
    
    try:
        # Locate the input element by its ID

        
        calculate = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")
        time.sleep(3)
        
        calculate.click()
    except StopIteration:
        assert False, "No link with href '/wiki/Folklore' was found."
    except NoSuchElementException:
        assert False, "No <a> elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"




@then('the text of the element with id "d" should be "{expected_text}"')
def confirm_area(context, expected_text):
    # try:
    #     # Wait for up to 5 seconds for the element to be clickable
    #     WebDriverWait(context.behave_driver, 10).until(
    #         EC.text_to_be_present_in_element((By.ID, id), expected_text)
    #     )
    # except Exception as e:
    #     assert False, f"Failed to find text '{expected_text}' in element with id '{id}': {str(e)}"
    # try:

    input_element = context.behave_driver.find_element(By.XPATH, "//input[@id='_d' and @disabled]")
    
    # Retrieve the value of the input element
    actual_value = input_element.get_attribute("value")
    assert actual_value == expected_text, f"Expected value '{expected_text}', but got '{actual_value}'."

    #     time.sleep(3)
    #     # Locate the input element by its ID
    #     area = context.behave_driver.find_element(By.ID, id)

    #     # Get the text of the span
    #     actual_text = area.text.strip()
        
    #     # Verify the text matches the expected value
    #     assert actual_text == expected_text, f"Expected text '{expected_text}', but found '{actual_text}'."
    # except StopIteration:
    #     assert False, "No link with href '/wiki/Folklore' was found."
    # except NoSuchElementException:
    #     assert False, "No <a> elements were found on the page."
    # except Exception as e:
    #     assert False, f"An unexpected error occurred: {str(e)}"


        
        