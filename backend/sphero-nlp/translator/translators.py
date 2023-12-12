import os
import openai
import dotenv
from importlib.resources import open_text

dotenv.load_dotenv()

system_prompt = None
prompt_file_name = "prompt.txt"

# loads the system prompt from given file name
def load_prompt(prompt_file_name):
    global system_prompt
    if os.path.exists(os.path.join(os.path.dirname(__file__), prompt_file_name)):
        with open_text(__package__, prompt_file_name) as f:
            system_prompt = f.read()
        print(system_prompt)
    else:
        raise FileNotFoundError("prompt.txt not found")


# this is the translator that uses GPT-3 to translate from natural language to RADESIC
class ChatGPTTranslator:
    def __init__(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        # openai.organization = os.environ["OPENAI_ORGANIZATION"]
        self.messages = [
            {"role": "system", "content": system_prompt},
        ]

    def translate(self, message):
        print(f"User: {message}")
        self.messages.append(
            {"role": "user", "content": message}
        )

        print(self.messages)

        prompt = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            temperature=0,
            max_tokens=256
        )


        response = prompt['choices'][0]['message']['content']
        print(f"Translator: {response}")
        return response

# this is a mock translator that just returns a hardcoded response
class MockTranslator:
    def __init__(self):
        pass

    def translate(self, message):
#         text = f"""
# BEGIN
#     ROLL 0 DEGREES AT 50 SPEED FOR 3 SECONDS
#     LED 0 0 255
#     LOOP TIMES 5 DO
#         LET B = 11
#         LED 255 0 255
#         IF B > 10 THEN
#             ROLL 90 DEGREES AT 25 SPEED FOR 1 SECONDS
#         END
#         LED 0 0 255
#     END
#     LED 0 0 255
#     ROLL 180 DEGREES AT 150 SPEED FOR 1 SECONDS
# END
# """
        text = f"""
BEGIN
    ROLL 0 DEGREES AT 50 SPEED FOR 3 SECONDS
    ROLL 90 DEGREES AT 50 SPEED FOR 3 SECONDS
    ROLL 90 DEGREES AT 50 SPEED FOR 3 SECONDS
END
"""

        return text
    

# BEGIN
#     ROLL 0 DEGREES AT 100 SPEED FOR 10 SECONDS
#     LED 0 0 255
#     LOOP TIMES 5 DO
#         LET B = 11
#         LED 255 0 255
#         IF B > 10 THEN
#             ROLL 90 DEGREES AT 25 SPEED FOR 5 SECONDS
#         END
#         LED 0 0 255
#     END
#     LED 0 0 255
# END
    

# for now, the script behavior is the same as the module behavior
if __name__ == "__main__":
    load_prompt(prompt_file_name)
else:
    load_prompt(prompt_file_name)