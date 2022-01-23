from .config import CONFIG


class CATAPULT(CONFIG):
    def __init__(self):
        self.users = []
    
        super(CATAPULT, self).__init__(from_config=False)

class USER(CONFIG):
    def __init__(self):
        self.user_id = ''
        self.user_name = ''
        self.user_email = ''
        self.git = {
            'platform' : '',
            'username' : '',
            'access_token' : ''
        }
        
        self.projects = []
        
        super(USER, self).__init__(from_config=False)
        
class PROJECT:
    def __init__(self):
        self.project_name = ''
        self.project_id = ''
        self.project_description = ''
        self.project_repo = ''
        self.last_commit = ''
        self.docker_image = ''
        self.version = ''
        self.contributors = []
        
        super(PROJECT, self).__init__(from_config=False)