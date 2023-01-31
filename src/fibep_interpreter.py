import json
import time
import os
import sys
import daemon
import logging
import logging.handlers as handlers
import base64


def base64_decode(b64):
    decoded_b64 = base64.b64decode(b64, validate=True)
    return decoded_b64

def save_attachment(decoded_b64,file_location,file_name ):
    decoded_b64= decoded_b64.encode('utf-8')
    with open(file_name , 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(decoded_b64)
        file_to_save.write(decoded_image_data)
def load_attachment(file_location,file_name):
    with open(file_location + file_name, 'rb') as binary_file:
        attachment = binary_file.read()
        return attachment
def base64_encode(attachment):
    encoded_b64 = base64.b64encode(attachment)
    return encoded_b64

class Article:
    def __init__(self,provider,item_id,country_iso,language_iso,source_id,source_name,publish_timestamp,article_lead,article_text):
        self.provider= provider
        self.item_id=item_id
        self.country=country_iso
        self.language=language_iso
        self.source_id=source_id
        self.source_name=source_name
        self.publish_timestamp=publish_timestamp
        self.article_lead=article_lead
        self.article_text=article_text
        self.additional_content=[]

    def additional_content_decode(self,additional_content):
        b64= additional_content["Base64data"]
        content=base64_decode(b64)
        return content
    def additional_content_encode(self,file_location, file_name):
        attachment = load_attachment(file_location,file_name)
        encoded_b64 = base64_encode(attachment)
        self.additional_content["FileName"]=file_name
        self.additional_content["Base64data"]=encoded_b64

        
        


            





def fibep_decode():
    try:
        pass
        
        
    except Exception as exception:
        logging.critical(f"There's an error accessing your config.yml file, the error is the following: {exception}")
        print("There's no config yaml file in the program's folder, please check the logs.")
        sys.exit()


def fibep_encode(news):
    try:
        pass


    except Exception as exception:
        logging.critical(f"There's an error accessing your config.yml file, the error is the following: {exception}")
        print("There's no config yaml file in the program's folder, please check the logs.")
        sys.exit()



if __name__== '__main__':
        file_location = os.path.dirname(os.path.realpath(__file__))
        main()
