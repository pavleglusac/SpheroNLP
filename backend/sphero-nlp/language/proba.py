import inspect
import os

from flask import Flask, jsonify
from flask_cors import CORS
from textx import metamodel_from_file
import language.Language as Lang


app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    classes = [cls for cls in (getattr(Lang, member) for member in dir(Lang)) if
               inspect.isclass(cls) and cls.__module__ == Lang.__name__]

    grammar_path = "intermediate.tx"
    full_grammar_path = os.path.join(os.path.dirname(__file__), grammar_path)
    mm = metamodel_from_file(full_grammar_path, classes=classes)
    file_path = 'intermediate.txt'
    with open(file_path, 'r') as file:
        file_content = file.read()

    model = mm.model_from_str(file_content)
    # exec(model.to_python())
    return [model.to_javascript(), model.to_codeblocks()]


if __name__ == '__main__':
    app.run(debug=True)
