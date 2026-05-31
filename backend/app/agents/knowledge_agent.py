import json


with open(
    "data/faq.json",
    "r"
) as f:

    FAQS = json.load(f)


def run_knowledge_agent(
    query: str
):

    query = query.lower()

    for key, value in FAQS.items():

        if key in query:

            return value

    return (
        "I could not find relevant information in the knowledge base."
    )