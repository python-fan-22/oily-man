import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "axe non"

    if p_message == "!rand":
        return str(random.randrange(1, 7))