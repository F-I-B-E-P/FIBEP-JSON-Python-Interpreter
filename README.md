# FIBEP-JSON-Interpreter
This is a simple interpreter for the FIBEP JSON Format. It includes both the methods to encode and decode Official FIBEP standard JSON format files.
You can easily integrate into your own software by using the methods
fibep_decode() which takes a json file as input and returns an Article class object, including the following attributes:
Mandatory:
provider, item_id, country_iso, language_iso, source_id, source_name, article_publication_timestamp, article_lead, article_text, article_source_channel

Optional:
additional_content_list, content_url, contract_id, customer_id, profile_id, article_author, article_headline, matching_words_list

additional_content_list and matching_words_list are both list of dictionaries that can contain many dictionaries.In the case of additional_content_list, if it has base64 encoded elements,
the library automatically decodes them  and regenerates the original file per the standard.

You can try the programa directly in your cli using the following syntax:
fibep_interpreter DIR -d FILETODECODE
where DIR is the directory in wich the file is in (defaults to the directory in which the program is installed).
