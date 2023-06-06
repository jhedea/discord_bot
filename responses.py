def get_response(message : str) -> str:
    p_message = message.lower()
    if p_message == "hello":
        return "hello! how can i help you?"

    if p_message == "weather":
        return "Today there are clear skies"

    if p_message == "!help":
        return "`help`"

    return "I do not understand"