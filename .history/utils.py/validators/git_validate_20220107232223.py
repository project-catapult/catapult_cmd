from PyInquirer import Validator, ValidationError

class REPO_VALIDATOR(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
            
class USER_VALIDATOR(Validator):
def validate(self, document):
    try:
        int(document.text)
    except ValueError:
        raise ValidationError(
            message='Please enter a number',
            cursor_position=len(document.text))  # Move cursor to end
        