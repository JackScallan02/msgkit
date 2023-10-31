from os import getenv
from openai import api_key
from msgkit import errorlog

api_key = getenv("OPENAI_API_KEY")

logger = errorlog.ErrorLog()
