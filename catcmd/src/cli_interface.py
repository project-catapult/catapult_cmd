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

from catcmd.src import BASE
from catcmd.config.cobjs import *
from catcmd.config.qconfigs import *

class CLI(BASE):
    def __init__(self):
        self.banner = Figlet(font='slant')
        self.banner_text = self.banner.renderText('Catapult')
        self.style_dict = style_from_dict({
                        Token.QuestionMark: '#E91E63 bold',
                        Token.Selected: '#673AB7 bold',
                        Token.Instruction: '',  # default
                        Token.Answer: '#2196f3 bold',
                        Token.Question: '',
                    })
        
        self._config = CATAPULT()
        
        self.questions = catapult_qs
                
        super(CLI, self).__init__()
        self.asking = True
        self.launch()
    
    
    def launch(self):
        self.log(f'[green]{self.banner_text}[/]')
        self.log("[red]Hi, Let's Configure Your Projectaile For Loading On The Catapult.[/]")
        while self.asking:
            answers = prompt(self.questions)
            print(answers)
        
    def init_project(self):
        self.init_image()
        self.init_repo()