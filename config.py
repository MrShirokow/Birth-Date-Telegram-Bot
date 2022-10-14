import os
from dotenv import load_dotenv


load_dotenv()


settings = {
    'TOKEN': os.getenv('TOKEN'),
    'LOG_FILE': 'logger.log'
}
