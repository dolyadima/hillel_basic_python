import os
from dotenv import load_dotenv
from pprint import pprint

project_folder = os.path.expanduser(r'~/PYCHARM/hillel_basic_python/lesson_15/')
load_dotenv(os.path.join(project_folder, r'.env'))

pprint(os.getenv('API_KEY'))
