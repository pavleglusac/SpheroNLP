from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
import os
import Language as Lang
import sys
import inspect

classes = []
for member in dir(Lang):
    attribute = getattr(Lang, member)
    if inspect.isclass(attribute) and attribute.__module__ == Lang.__name__:
        # Ensure we are adding the class itself, not a string representation or instance.
        classes.append(attribute)
# Debugging line to check the content of classes list before passing to metamodel_from_file
for c in classes:
    print(type(c))

# Assuming you have the correct classes list




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


