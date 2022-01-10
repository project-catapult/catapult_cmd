from .git_validate import *

all_validators = {
    'git_user_validator' : USER_VALIDATOR,
    'git_repo_validator' : REPO_VALIDATOR
}


class VALIDATOR:
    def __init__(self, validators=[]):
        self.validators = {}
        for validator in validators:
            self.validators[validator] = all_validators[validator]
            
    def validate(self, config, validator=''):
        if validator == 'all':
            for i, validator in enumerate(self.validators.keys()):
                self.validators[validator](config[i])
        else:
            if validator in self.validators.keys():
                self.validators[validator](config)
            else:
                print(f'Validator {validator} Not Found.')
                exit(0)