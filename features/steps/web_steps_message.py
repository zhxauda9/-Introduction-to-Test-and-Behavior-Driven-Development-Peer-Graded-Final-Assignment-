# GitHub URL: https://example.com

# Code snippet in `web_steps.py` for verifying a specific message:
from behave import then

@then('I should see the message "{message}"')
def step_impl(context, message):
    alert = context.driver.switch_to.alert
    assert message in alert.text
