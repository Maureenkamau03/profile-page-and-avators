import os

class Config(object):
    """Define app conigurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY')  or 'hard-to-guess'