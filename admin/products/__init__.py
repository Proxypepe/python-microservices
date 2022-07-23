from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'RABBITMQ_URL': os.getenv('RABBITMQ_URL')
}
