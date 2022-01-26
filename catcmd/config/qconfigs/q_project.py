questions = [
    {
        'property': 'project_name',
        'question' : {
            'type': 'input',
            'message': 'Please Enter Project Name: ',
            'default': '',
            # 'validate': CHECK_EMPTY
        }
    },
    {
        'property': 'project_description',
        'question' : {
            'type': 'input',
            'message': 'Brief Project Description',
            'default': ''
        }
    },
    {
        'property': 'version',
        'question' : {
            'type': 'input',
            'message': 'Project Version',
            'default': '1.0'
        }
    }
]