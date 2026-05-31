from prometheus_client import (
    Counter,
    Histogram,
    generate_latest
)


REQUEST_COUNT = Counter(
    "voice_ai_requests_total",
    "Total requests"
)

CONVERSATION_AGENT_COUNT = Counter(
    "conversation_agent_calls_total",
    "Conversation agent calls"
)

CALCULATOR_AGENT_COUNT = Counter(
    "calculator_agent_calls_total",
    "Calculator agent calls"
)

KNOWLEDGE_AGENT_COUNT = Counter(
    "knowledge_agent_calls_total",
    "Knowledge agent calls"
)

REQUEST_LATENCY = Histogram(
    "voice_ai_latency_seconds",
    "Request latency"
)


def get_metrics():

    return generate_latest()