import streamlit as st

import websocket


st.title(
    "Realtime Voice AI Platform"
)


question = st.text_input(
    "Ask Something"
)


if st.button("Send"):

    ws = websocket.create_connection(
        "ws://localhost:8000/ws/chat"
    )

    ws.send(
        question
    )

    response = ws.recv()

    st.write(response)

    ws.close()