# -*- coding: utf-8 -*-
import regex

from rich.console import Console
from rich import inspect as rich_inspect
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
        self.fill_config(answers)
        self.init_project()
        
    def fill_config(self, answers):
        for k, v in answers.items():
            self.projectaile_config[k] = v

f = Figlet(font='slant')
print(f.renderText('Catapult'))

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


print("Hi, Let's Configure Your Projectaile For Loading On The Catapult.")

questions = [
    {
        'type': 'confirm',
        'name': 'toBeDelivered',
        'message': 'Is this for delivery?',
        'default': False
    },
    {
        'type': 'input',
        'name': 'phone',
        'message': 'What\'s your phone number?',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'list',
        'name': 'size',
        'message': 'What size do you need?',
        'choices': ['Large', 'Medium', 'Small'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'quantity',
        'message': 'How many do you need?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'expand',
        'name': 'toppings',
        'message': 'What about the toppings?',
        'choices': [
            {
                'key': 'p',
                'name': 'Pepperoni and cheese',
                'value': 'PepperoniCheese'
            },
            {
                'key': 'a',
                'name': 'All dressed',
                'value': 'alldressed'
            },
            {
                'key': 'w',
                'name': 'Hawaiian',
                'value': 'hawaiian'
            }
        ]
    },
    {
        'type': 'rawlist',
        'name': 'beverage',
        'message': 'You also get a free 2L beverage',
        'choices': ['Pepsi', '7up', 'Coke']
    },
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your purchase experience?',
        'default': 'Nope, all good!'
    },
    {
        'type': 'list',
        'name': 'prize',
        'message': 'For leaving a comment, you get a freebie',
        'choices': ['cake', 'fries'],
        'when': lambda answers: answers['comments'] != 'Nope, all good!'
    }
]

answers = prompt(questions, style=style)
print('Order receipt:')
pprint(answers)