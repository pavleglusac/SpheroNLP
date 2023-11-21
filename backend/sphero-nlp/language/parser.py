from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
import os
import language.Language as Lang
import sys
import inspect

# get all classes from the language module
classes = [cls for cls in (getattr(Lang, member) for member in dir(Lang)) if inspect.isclass(cls) and cls.__module__ == Lang.__name__]

grammar_path = "intermediate.tx"
full_grammar_path = os.path.join(os.path.dirname(__file__), grammar_path)
mm = metamodel_from_file(full_grammar_path, classes=classes)


def parse(text):
    return mm.model_from_str(text)



file_path = 'intermediate.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

model = mm.model_from_str(file_content)
print(model.to_python())
print("--------------------------")
print(model.to_javascript())
print("--------------------------")
print(model.to_codeblocks())