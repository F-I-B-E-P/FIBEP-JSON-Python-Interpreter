import json
import time
import os
import sys
import logging
import logging.handlers as handlers
import base64
import argparse
from.fibep_interpreter import fibep_decode, fibep_encode
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