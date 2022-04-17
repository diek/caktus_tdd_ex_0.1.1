import random

import requests


def generate_random():
    try:
        source = "https://www.random.org/integers/?num=1&min=1&max=57970&col=5&base=10&format=plain&rnd=new"
        number = requests.get(source)
        return int(number.text)
    except:
        print("error")
        return random.randint(1, 57970)
