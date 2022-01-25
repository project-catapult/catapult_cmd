"""
-----------------------------------------------------------
## Description  : Catapult Command Line Interface
## Author       : Anubhav Tiwari
## Project      : catcmd
## Main Project : Catapult
-----------------------------------------------------------
"""

# -*- coding: utf-8 -*-
import regex

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from pyfiglet import Figlet


from .base_class import BASE

class CLI(BASE):
    def __init__(self):
        self.banner = Figlet(font='slant')
        self.banner_text = f.renderText('Catapult')
        self.style_dict = style_from_dict({
                        Token.QuestionMark: '#E91E63 bold',
                        Token.Selected: '#673AB7 bold',
                        Token.Instruction: '',  # default
                        Token.Answer: '#2196f3 bold',
                        Token.Question: '',
                    })
        
        self.projectaile_config = CONFIG('./base_config.yaml')
        self.catapult_config = CONFIG('./catapult_config.yaml')
        self.questions = CONFIG('./questions.yaml')
        
        super(CLI, self).__init__()
                
        self.launch()
    
    def launch(self):
        self.log(f'[green]{self.banner_text}[/]')
        answers = prompt(self.questions, style=self.style_dict)
        self.update_config(answers)
        self.init_project()
        
    def update_config(self, answers):
        for k, v in answers.items():
            self.projectaile_config[k] = v
            # Same For catapult config as well, add the project info to the list
            
    def init_project(self):
        self.init_image()
        self.init_repo()


f = Figlet(font='slant')
print(f.renderText('Catapult'))

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


print("Hi, Let's Configure Your Projectaile For Loading On The Catapult.")