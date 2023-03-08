import base64
import requests
import json
import os
import shutil
import time

# Set the path to the directory containing the captcha images
captcha_dir = 'facebook_captcha'

# Initialize an empty list to store the file names and titles
captcha_files = []

# Iterate over the files in the captcha directory
index = 0
for filename in os.listdir(captcha_dir):
    # Get the full path to the file
    filepath = os.path.join(captcha_dir, filename)
    # Check if the file is an image
    if os.path.isfile(filepath) and filename.endswith('.png'):
        # Add the file name and title to the list
        encoded_string = ""
        
        api_key = '0abb3b319eb64abbae0ea36a9f4b3f45'
        captcha_fp = open('1.png', 'rb')
        client = AnycaptchaClient(api_key)
        task = ImageToTextTask(captcha_fp)
        job = client.createTask(task,typecaptcha="text")
        job.join()
        result = job.get_solution_response()
        if result.find("ERROR") != -1:
            print("error ", result)
        else:
            print("success ", result)

        

def serialize(self, **result):
    return result

class ImageToTextTask(object):
    type = "ImageToTextTask"
    fp = None
    phrase = None
    case = None
    numeric = None
    math = None
    minLength = None
    maxLength = None
    time_sleep = 1
    def __init__(
        self,
        fp,
        phrase=None,
        case=None,
        numeric=None,
        math=None,
        min_length=None,
        max_length=None,
    ):
        self.fp = fp
        self.phrase = phrase
        self.case = case
        self.numeric = numeric
        self.math = math
        self.minLength = min_length
        self.maxLength = max_length

    def serialize(self):
        return {
            "type": self.type,
            "body": base64.b64encode(self.fp.read()).decode("utf-8"),
            "phrase": self.phrase,
            "case": self.case,
            "numeric": self.numeric,
            "math": self.math,
            "minLength": self.minLength,
            "maxLength": self.maxLength,
        }
