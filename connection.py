import os
from pony.orm import *
from dotenv import load_dotenv

load_dotenv()

db = Database()
connection = db.bind(provider='mysql', host=os.getenv('APP_HOST'), user=os.getenv('DB_USERNAME'),
                     passwd=os.getenv('DB_PASSWORD'), db=os.getenv('DB_DATABASE'))
