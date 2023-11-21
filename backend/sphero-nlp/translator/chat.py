import os

os.environ["TRANSFORMERS_CACHE"] = "/mnt/ACA058A9A0587C30/models"
os.environ["HF_HOME"] = "/mnt/ACA058A9A0587C30/models"

import torch
from transformers import pipeline

print(torch.cuda.is_available())


pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-alpha", torch_dtype=torch.bfloat16, device_map="auto")

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

prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.1)
print(outputs[0]["generated_text"])