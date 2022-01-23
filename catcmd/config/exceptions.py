import os
from .config import CONFIG


_EXCEPTION_LIST_ = CONFIG(
        config_file=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 
                'exceptions.yaml'
                )
        )   