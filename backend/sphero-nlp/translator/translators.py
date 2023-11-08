import os
import openai
import dotenv
from importlib.resources import open_text

dotenv.load_dotenv()

prompt = None
prompt_file_name = "prompt.txt"

# loads the system prompt from given file name
def load_prompt(prompt_file_name):
    if os.path.exists(os.path.join(os.path.dirname(__file__), prompt_file_name)):
        with open_text(__package__, prompt_file_name) as f:
            prompt = f.read()
        print(prompt)
    else:
        raise FileNotFoundError("prompt.txt not found")


# this is the translator that uses GPT-3 to translate from natural language to RADESIC
class ChatGPTTranslator:
    def __init__(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        openai.organization = os.environ["OPENAI_ORGANIZATION"]

    def translate(self, message):
        print(f"User: {message}")
        self.messages.append({"role": "user", "content": message})

        prompt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.1,
            max_tokens=256
        )

        response = prompt['choices'][0]['message']['content']
        return response

# this is a mock translator that just returns a hardcoded response
class MockTranslator:
    def __init__(self):
        pass

    def translate(self, message):
        text = f"""
BEGIN
    ROLL 0 DEGREES AT 100 SPEED FOR 10 SECONDS
END
"""
        return text
    

# for now, the script behavior is the same as the module behavior
if __name__ == "__main__":
    load_prompt(prompt_file_name)
else:
    load_prompt(prompt_file_name)