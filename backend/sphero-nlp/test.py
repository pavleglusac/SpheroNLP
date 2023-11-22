from language import Language, parser
import sys
import inspect
from translator.translators import ChatGPTTranslator, MockTranslator
import json


def language_to_json(obj, depth=0, name=None):
    if type(obj) in [int, float, str, bool]:
        return obj
    
    if type(obj) == list:
        return [language_to_json(elem, depth+1) for elem in obj]
    
    attrs = vars(obj)

    class_name = obj.__class__.__name__
    json_obj = {}
    for attr in attrs:
        if attr.startswith("_") or "parent" in attr:
            continue
        json_obj[attr] = language_to_json(attrs[attr], depth+1, attr)

    json_obj["type"] = class_name
    return json_obj

text_translator = MockTranslator()


code = text_translator.translate("aa")
code_model = parser.parse(code)
json_model = language_to_json(code_model)
pretty_json = json.dumps(json_model, indent=4)
print(pretty_json)
