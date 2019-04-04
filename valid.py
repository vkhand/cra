from selenium import webdriver
import pytesseract
import requests
from seleniumrequests import Firefox
from selenium.webdriver.firefox.options import Options
import urllib3
from PIL import Image
import cv2
import boto3
from cv2 import imwrite
from cv2 import addWeighted 
from PIL import Image,ImageFilter
import cv2

from scipy.ndimage.filters import median_filter



options = Options()
options.headless = False

browser = Firefox(options=options)
browser.get('https://parivahan.gov.in/rcdlstatus/')

browser.execute_script("document.body.style.zoom='10%'")
elem = browser.find_element_by_id("form_rcdl:j_idt36:j_idt41")
loc  = elem.location
size = elem.size
x  = int(loc['x'])
y   = int(loc['y'])
w = int(size['width'])
h = int(size['height'])
# print(x,y,w,h)
browser.save_screenshot("snap.png")
img = cv2.imread("snap.png")
crop_img = img[y:y+h, x:x+w]
imwrite( "Image.png", crop_img )



# print(pytesseract.image_to_string("Image.png"))

client = boto3.client('s3', region_name='us-west-2')

client.upload_file('Image.png', 'detect-userfiles-mobilehub-466049087', 'Image.png')

# if __name__ == "__main__":

bucket='detect-userfiles-mobilehub-466049087'
photo='Image.png'

client=boto3.client('rekognition')


response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                    
textDetections=response['TextDetections']
# print ('Detected text')
for text in textDetections:

    if(text['Type'] == 'WORD'):
        cap = text['DetectedText']
        


regis1 = browser.find_element_by_id("form_rcdl:tf_reg_no1")
regis1.clear()
regis1.send_keys("ka03mq")

regis2 = browser.find_element_by_id("form_rcdl:tf_reg_no2")
regis2.clear()
regis2.send_keys("9396")


captcha = browser.find_element_by_id("form_rcdl:j_idt36:CaptchaID")
captcha.clear()
captcha.send_keys(str(cap))

# wait(10)
# import time
# time.sleep(5)

submit_button = browser.find_element_by_id("form_rcdl:j_idt47")
submit_button.click()