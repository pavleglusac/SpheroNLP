import requests
from langchain.llms import Ollama

llm = Ollama(model="codellama:7b-instruct")

prompt = """
    You have every standard python library available to you, including spherov2.
    Here are the functions you can use in spherov2:
    - find_toy // this returns a toy object
    - set_main_led(self, color: Color) // this sets the main LED to a color, color is a tuple of (r, g, b)
    - spin(self, angle: int, duration: float) // this spins the toy by angle degrees for duration seconds
    - roll(self, heading: int, speed: int, duration: float) // this rolls the toy in a direction for a duration
    - set_heading(self, heading: int) // this sets the heading of the toy in degrees
    - set_speed(self, speed: int) // this sets the speed of the toy in cm/s

    Do the following:
    Every 5 seconds move the ball forward 10 cm.

    Output ONLY the appropriate code to do this.
"""


res = llm.predict(prompt)
print (res)