# GitHub URL: https://example.com

# Code snippet in `web_steps.py` for verifying specific text absence:
from behave import then

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    body = context.driver.find_element_by_tag_name('body')
    assert text not in body.text
