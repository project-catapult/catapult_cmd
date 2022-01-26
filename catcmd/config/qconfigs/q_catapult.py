questions = [
    {
        'question' : {
            'type': 'list',
            'name': 'task',
            'message': 'What do you want to do?',
            'choices': ['Create', 'Fetch', 'Update', 'Delete', 'Exit'],
            'filter': lambda val: val.lower()
        },
        'callback': lambda response: form_question(response)
    }
]

def form_question(response):
    question = {
        'type': 'list',
        'message' : f'What do you want to {response.title()}?',
        'choices': [f'{response.title()} {i}' for i in ['User', 'Projectile', 'Environment', 'Git Profile', 'Cloud Profile']],
        'filter': lambda choice: choice.split(' ')[1].lower()
    }
    
    return question