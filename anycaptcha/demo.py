from anycaptcha import AnycaptchaClient, ImageToTextTask
import os
import shutil

captcha_dir = 'facebook_captcha'

def demo_imagetotext():
    api_key = '0abb3b319eb64abbae0ea36a9f4b3f45'
    for filename in os.listdir(captcha_dir):
        filepath = os.path.join(captcha_dir, filename)
        captcha_fp = open(captcha_dir + "\\" + filename, 'rb')
        client = AnycaptchaClient(api_key)
        task = ImageToTextTask(captcha_fp)
        job = client.createTask(task,typecaptcha="text")
        job.join()
        result = job.get_solution_response()
        if result.find("ERROR") != -1:
            print("error ", result)
        else:
            value = result
            fileName = value + ".png"
            destinationFilePath = "facebook_captcha_labels\\" + fileName
            shutil.copy(filepath, destinationFilePath)
            print("success ", result)

def demo_getblance():
    api_key = api_key = "0abb3b319eb64abbae0ea36a9f4b3f45"
    client = AnycaptchaClient(api_key)
    print(client.getBalance())


if __name__=="__main__":
    demo_imagetotext()

