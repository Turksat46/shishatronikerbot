import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hey there!"

    if p_message.startswith("lets go"):
        return "JAAAAAA DU HURENSOHN"

    if p_message == "beleidige mein sohn":
        beleidigungen=["DU HURENSOHN", "ich ficke dich", "kis umuk ya sippe", "to qfisha none", "mistgeburt", "wuff wuff", "wichser", "ich reite dich wie ein esel", "sg (siktir git)"]
        return random.choice(beleidigungen)
