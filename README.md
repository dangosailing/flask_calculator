Scaled down version of a calculator app from the presentation. 
No login/register functions since I wanted to make sure the basic functionality of the app was intact before adding register/login functionality.
Must add config file with the following (example) structure:
----------------------------------------------------------------
import os

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY", "your_key")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///calculator.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
----------------------------------------------------------------