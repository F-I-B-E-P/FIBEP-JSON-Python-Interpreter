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
        self.additional_content_list = []
        self.content_url = ""
        self.contract_id=""
        self.customer_id=""
        self.profile_id=""
        self.article_author = ""
        self.article_headline=""
        self.matching_words_list=[]
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
                additional_content_list = parsed_encoded_json["AdditionalContent"]
                if additional_content_list:
                    for additional_content_element in additional_content_list:
                            
                        if "Base64data" in additional_content_element:
                            base64data=additional_content_element["Base64data"]
                            file_format=additional_content_element["Format"]
                            file_name = additional_content_element["FileName"]
                            decoded_b64 = base64_decode(base64data)
                            save_attachment(decoded_b64,file_format,file_location,file_name)
                            news.additional_content_list = parsed_encoded_json["AdditionalContent"]
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
                news.matching_words_list=parsed_encoded_json["MatchingWords"]
        print(vars(news))
        return news
    except Exception as exception:
        logging.critical(f"There's an error decoding your json file, the error is the following: {exception}")
        print("There's no json file in the program's folder, please check the logs.")
        sys.exit()
def fibep_encode(news):
    try:
        parsed_news = {}
        parsed_news.update( {"Provider" : news.provider, 
                             "ItemID" : news.item_id, 
                             "Country" : news.country_iso, 
                             "Language" : news.language_iso, 
                             "SourceID" : news.source_id,
                             "SourceName" : news.source_name,
                             "PublishTime" : news.article_publication_timestamp,
                             "Lead" : news.article_lead,
                             "Text" : news.article_text,
                             "SourceChannel" : news.article_source_channel})
        if hasattr(news, 'content_url'):
            parsed_news.update({"ContentURL" : news.content_url})

        if hasattr(news, 'additional_content_list'):



                additional_content_list = parsed_encoded_json["AdditionalContent"]
                if additional_content_list:
                    for additional_content_element in additional_content_list:
                            
                        if "Base64data" in additional_content_element:
                            base64data=additional_content_element["Base64data"]
                            file_format=additional_content_element["Format"]
                            file_name = additional_content_element["FileName"]
                            decoded_b64 = base64_decode(base64data)
                            save_attachment(decoded_b64,file_format,file_location,file_name)
                            news.additional_content_list = parsed_encoded_json["AdditionalContent"]

            parsed_news.update({"AdditionalContent" : news.additional_content_list})

        if hasattr(news, 'contract_id'):
            parsed_news.update({"ContractID" : news.contract_id})

        if hasattr(news, 'customer_id'):
            parsed_news.update({"CustomerID" : news.customer_id})

        if hasattr(news, 'profile_id'):
            parsed_news.update({"ProfileID" : news.profile_id})


        if hasattr(news, 'article_author'):
            parsed_news.update({"Author" : news.article_author})

        if hasattr(news, 'article_headline'):
            parsed_news.update({"Headline" : news.article_headline})

        if hasattr(news, 'matching_words_list'):
            parsed_news.update({"MatchingWords" : news.matching_words_list})

        json.dump(news)
    except Exception as exception:
        logging.critical(f"There's an error accessing your JSON file, the error is the following: {exception}")
        print("There's no JSON file in the program's folder, please check the logs.")
        sys.exit()


