import os
from dotenv import load_dotenv


load_dotenv()

settings = {
    'TOKEN': os.getenv('TOKEN'),
    'LOG_FILE': 'logger.log',
    'GOOGLESHEET_URL': os.getenv('GOOGLESHEET_URL'),
    'USER_ID': os.getenv('USER_ID')
}
