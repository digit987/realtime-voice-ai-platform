import re


def run_calculator_agent(
    expression: str
):

    try:

        expression = expression.lower()

        expression = expression.replace(
            "calculate",
            ""
        )

        expression = expression.replace(
            "solve",
            ""
        )

        expression = expression.replace(
            "plus",
            "+"
        )

        expression = expression.replace(
            "minus",
            "-"
        )

        expression = expression.replace(
            "times",
            "*"
        )

        expression = expression.replace(
            "multiplied by",
            "*"
        )

        expression = expression.replace(
            "x",
            "*"
        )

        expression = expression.replace(
            "divided by",
            "/"
        )

        expression = expression.replace(
            "over",
            "/"
        )

        expression = expression.strip()

        expression = re.sub(
            r"[^0-9+\-*/(). ]",
            "",
            expression
        )

        result = eval(
            expression
        )

        return str(result)

    except Exception:

        return (
            "Invalid calculation."
        )