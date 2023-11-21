# openai
import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.organization = os.environ["OPENAI_ORGANIZATION"]

messages = [
    {
        "role": "system",
        "content": """
        You are an interface from natural language to python.
        You have every standard python library available to you, including spherov2.
        Here are the functions you can use in spherov2:
        - find_toy // this returns a toy object
        - set_main_led(self, color: Color) // this sets the main LED to a color, color is a tuple of (r, g, b)
        - spin(self, angle: int, duration: float) // this spins the toy by angle degrees for duration seconds
        - roll(self, heading: int, speed: int, duration: float) // this rolls the toy in a direction for a duration
        - set_heading(self, heading: int) // this sets the heading of the toy in degrees
        - set_speed(self, speed: int) // this sets the speed of the toy in cm/s

        Some examples of things you can do:

        User: Roll the ball forward, then turn it red.
        System: 
            import spherov
            sphero = sphero_skd.find_toy()
            sphero.roll(0, 100, 1)
            sphero.set_main_led(sphero.Color(r=255, g=0, b=0))
        """,
    },
    {"role": "user", "content": "Every 5 seconds move the ball forward 10 cm."},
]

print("User: Every 5 seconds move the ball forward 10 cm.")

prompt = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.1,
    max_tokens=256,
)

response = prompt['choices'][0]['message']['content']

print(f"Response:\n{response}")