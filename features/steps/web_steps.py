# GitHub URL: https://example.com

# Code snippet in `web_steps.py` for the Button Click step definition:
from behave import when
from selenium import webdriver

@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    button = context.driver.find_element_by_name(button_name)
    button.click()
