# GitHub URL: https://example.com

# Code snippet in `web_steps.py` for verifying specific text presence:
from behave import then

@then('I should see "{text}" on the page')
def step_impl(context, text):
    body = context.driver.find_element_by_tag_name('body')
    assert text in body.text
