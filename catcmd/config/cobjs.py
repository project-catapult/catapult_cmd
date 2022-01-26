import os
import random
import string
from .config import CONFIG


def get_random_id(id_len=10):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(id_len))


class CATAPULT(CONFIG):
    save_path = os.path.join(os.getcwd(), '.catapult')
    def __init__(self):
        try:
            config_file = CATAPULT.save_path 
            super(CATAPULT, self).__init__(config_file=config_file)
        except Exception as e:
            self.users = []
            super(CATAPULT, self).__init__(from_config=False)
            
        self.save()
        
    def add_user(self, usr):
        self.users.append(usr)
        
    def save(self):
        self.export(CATAPULT.save_path)


class USER(CONFIG):
    def __init__(self, answers={}):
        self.user_id = get_random_id(15)
        self.user_name = ''
        self.user_email = ''
        self.projects = []
        self.git = []
        
        super(USER, self).__init__(from_config=False, config_file='', **answers)

    def add_project(self, proj):
        proj.contributors.append(self.user_id)
        self.projects.append(proj)
        
    def add_git(self, git):
        self.git.append(git)


class GIT(CONFIG):
    def __init__(self, answers={}):
        self.platform = ''
        self.username = ''
        self.access_token = ''
        super(GIT, self).__init__(from_config=False, config_file='', **answers)


class CLOUD(CONFIG):
    def __init__(self, answers={}):
        self.platform = ''
        self.key_file_path = ''
        super(CLOUD, self).__init__(from_config=False, config_file='', **answers)


class ENV(CONFIG):
    def __init__(self, answers={}):
        self.environment = ''
        self.env_name = ''
        self.env_config = {}
        super(ENV, self).__init__(from_config=False, config_file='', **answers)


class PROJECT(CONFIG):
    def __init__(self, answers={}):
        self.project_name: str = ''
        self.project_id: str = get_random_id(10)
        self.project_description: str = ''
        self.project_repo: str = ''
        self.last_commit: str = ''
        self.docker_image = ''
        self.version = ''
        self.contributors = []
        
        super(PROJECT, self).__init__(from_config=False, config_file='', **answers)