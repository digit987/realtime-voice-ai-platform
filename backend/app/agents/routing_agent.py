def route_message(
    message: str
):

    message = message.lower()

    calculator_keywords = [
        "+",
        "-",
        "*",
        "/",
        "calculate",
        "solve"
    ]

    for keyword in calculator_keywords:

        if keyword in message:

            return "calculator"

    knowledge_keywords = [
        "refund",
        "business hours",
        "support",
        "shipping"
    ]

    for keyword in knowledge_keywords:

        if keyword in message:

            return "knowledge"

    return "conversation"