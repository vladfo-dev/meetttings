from backend.version import __version__
import os

# FastAPI logging level
DEBUG = True
# FastAPI project name
PROJECT_NAME = "meetttings"
VERSION = __version__
# Path to config file
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Secret Key
SECRET_KEY = os.urandom(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
