"""
-----------------------------------------------------------
## Description  : 
## Author       : 
## Project      : 
## Main Project : 
-----------------------------------------------------------
"""

from PyInquirer import Validator, ValidationError


"""
    REPO_VALIDATOR : Validates If Existing Repository Exists 
                    Or If It Can Be Created Given The Info
"""
class REPO_VALIDATOR(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

"""
    USER_VALIDATOR : Validates If The Provided User Name Or Organization Name
                    Exists On The Given Platform
"""
class USER_VALIDATOR(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
            