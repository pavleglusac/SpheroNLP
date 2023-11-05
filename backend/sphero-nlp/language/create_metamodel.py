from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
import os
import Language as Lang
import sys

# get all classes from the language module
classes = [getattr(Lang, a) for a in dir(Lang) if not a.startswith("__")]

path = "./intermediate.tx"
mm = metamodel_from_file(path, classes=classes)

# parse this text
text = f"""
BEGIN
    ROLL 0 DEGREES AT 100 SPEED FOR 10 SECONDS
    LOOP TIMES 5 DO
        LET B = RANDOM 1 TO 5
        IF B > 10 THEN
            ROLL 90 DEGREES AT 50 SPEED FOR 5 SECONDS
        END
    END
END
"""

# parse the text
model = mm.model_from_str(text)

print(model.to_python())

# exec(model.to_python())

print(model)

# export the model
model_export(model, "model.dot")
os.system("dot -Tpng -O model.dot")


