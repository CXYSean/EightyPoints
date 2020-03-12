import random

def dispose_cards():
    cards = list(range(1,109))
    res = random.choices(cards,20)
    return res
