import json
import time
import os
import sys
import logging
import logging.handlers as handlers
import base64
import argparse


class Article:
    def __init__(self,
                 provider,
                 item_id,
                 country_iso,
                 language_iso,
                 source_id,
                 source_name,
                 article_publication_timestamp,
                 article_lead,
                 article_text,
                 article_source_channel):
        self.provider = provider
        self.item_id = item_id
        self.country = country_iso
        self.language = language_iso
        self.source_id = source_id
        self.source_name = source_name
        self.article_publication_timestamp = article_publication_timestamp
        self.article_lead = article_lead
        self.article_text = article_text
        self.article_source_channel=article_source_channel
        self.additional_content = []
        self.content_url = ""
        self.contract_id=""
        self.customer_id=""
        self.profile_id=""
        self.article_author = ""
        self.article_headline=""
        self.matching_words={}
    def additional_content_decode(self,additional_content):
        b64 = additional_content["Base64data"]
        content=base64_decode(b64)
        return content
    def additional_content_encode(self,file_location, file_name):
        attachment = load_attachment(file_location,file_name)
        encoded_b64 = base64_encode(attachment)
        self.additional_content["FileName"] = file_name
        self.additional_content["Base64data"] = encoded_b64
def base64_decode(b64):
    decoded_b64 = base64.b64decode(b64, validate=True)
    return decoded_b64
def save_attachment(decoded_b64,file_format,file_location,file_name):
    #decoded_b64= decoded_b64.encode('utf-8')
    file=os.path.join(file_location, file_name + "." + file_format)
    with open(file , 'wb') as file_to_save:
        file_to_save.write(decoded_b64)
        file_to_save.close()
def load_attachment(file_location,file_name):
    with open(file_location + file_name, 'rb') as binary_file:
        attachment = binary_file.read()
        return attachment
def base64_encode(attachment):
    encoded_b64 = base64.b64encode(attachment)
    return encoded_b64
def fibep_decode(encoded_json):
    try:
        encoded_json = open(encoded_json,encoding="utf8")
        parsed_encoded_json=json.load(encoded_json)
        news = Article(parsed_encoded_json["Provider"],
                       parsed_encoded_json["ItemID"],
                       parsed_encoded_json["Country"],
                       parsed_encoded_json["Language"],
                       parsed_encoded_json["SourceID"],
                       parsed_encoded_json["SourceName"],
                       parsed_encoded_json["PublishTime"],
                       parsed_encoded_json["Lead"],
                       parsed_encoded_json["Text"],
                       parsed_encoded_json["SourceChannel"])

        if "ContentURL" in parsed_encoded_json:
            if parsed_encoded_json["ContentURL"]:
                news.content_url = parsed_encoded_json["ContentURL"]
        if "AdditionalContent" in parsed_encoded_json:
            if parsed_encoded_json["AdditionalContent"]:
                additional_content = parsed_encoded_json["AdditionalContent"]
                if additional_content:
                    for additional_content_element in additional_content:
                            
                        if "Base64data" in additional_content_element:
                            base64data=additional_content_element["Base64data"]
                            file_format=additional_content_element["Format"]
                            file_name = additional_content_element["FileName"]
                            decoded_b64 = base64_decode(base64data)
                            save_attachment(decoded_b64,file_format,file_location,file_name)
                            news.additional_content = parsed_encoded_json["AdditionalContent"]
        if "ContractID" in parsed_encoded_json:
            if parsed_encoded_json["ContractID"]:
                news.contract_id=parsed_encoded_json["ContractID"] 
        if "CustomerID" in parsed_encoded_json:
            if parsed_encoded_json["CustomerID"]:
                news.customer_id=parsed_encoded_json["CustomerID"]
        if "ProfileID" in parsed_encoded_json:
            if parsed_encoded_json["ProfileID"]:
                news.profile_id=parsed_encoded_json["ProfileID"]
        if "Author" in parsed_encoded_json:
            if parsed_encoded_json["Author"]:
                news.article_author = parsed_encoded_json["Author"]
        if "Headline" in parsed_encoded_json:
            if parsed_encoded_json["Headline"]:
                news.article_headline=parsed_encoded_json["Headline"]
        if "MatchingWords" in parsed_encoded_json:
            if parsed_encoded_json["MatchingWords"]:
                news.matching_words=parsed_encoded_json["MatchingWords"]
        #print(vars(news))
        return news
    except Exception as exception:
        logging.critical(f"There's an error decoding your json file, the error is the following: {exception}")
        print("There's no json file in the program's folder, please check the logs.")
        sys.exit()
def fibep_encode(news):
    try:

        json.dump(news)
    except Exception as exception:
        logging.critical(f"There's an error accessing your JSON file, the error is the following: {exception}")
        print("There's no JSON file in the program's folder, please check the logs.")
        sys.exit()
def main():
    try:
        parser = argparse.ArgumentParser(description='This is a simple python script to encode or decode files according to the FIBEP JSON open standard.')
        parser.add_argument('dir', nargs="?", default=file_location)
        parser.add_argument('-e', type=str, help='Encode the file quoted after the e.')
        parser.add_argument('-d', type=str, help='Decode the file quoted after the d.')
        parser.add_argument('-DEBUG', action='store_true', help='Add Debug messages to log.')
        args = parser.parse_args()
        if getattr(args,'e') is not None:
            decoded_json = os.path.join(args.dir, args.e)
            logging.info("Running with -e to encode a JSON file.")
            fibep_encode(decoded_json)
        elif getattr(args,'d'):
            encoded_json = os.path.join(args.dir, args.d)
            logging.info("Running with -d to decode a JSON file.")
            fibep_decode(encoded_json)
        if getattr(args,'DEBUG'):
            logging.info("Running with -DEBUG in DEBUG log mode.")
    except Exception as exception:
        logging.critical(f"There's an error accessing your JSON file, the error is the following: {exception}")
        print("There's no JSON file in the program's folder, please check the logs.")
        sys.exit()
if __name__== '__main__':
        file_location = os.path.dirname(os.path.realpath(__file__))
        main()

