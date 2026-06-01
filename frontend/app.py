import os
import json
import uuid

import requests
import streamlit as st
import websocket

from streamlit_mic_recorder import (
    mic_recorder
)


BACKEND_URL = st.secrets.get(
    "BACKEND_URL",
    os.getenv(
        "BACKEND_URL",
        "http://127.0.0.1:8000"
    )
)


st.set_page_config(
    page_title="Realtime Voice AI Platform",
    layout="wide"
)


if "session_id" not in st.session_state:

    st.session_state.session_id = str(
        uuid.uuid4()
    )


if "messages" not in st.session_state:

    st.session_state.messages = []


st.title(
    "🎙️ Realtime Voice AI Platform"
)

st.caption(
    f"Session: {st.session_state.session_id[:8]}"
)


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


audio = mic_recorder(
    start_prompt="🎤 Speak",
    stop_prompt="⏹ Stop"
)


if audio:

    try:

        transcription_response = (
            requests.post(
                f"{BACKEND_URL}/api/transcribe",

                files={
                    "audio": (
                        "audio.wav",
                        audio["bytes"],
                        "audio/wav"
                    )
                },

                timeout=120
            )
        )

        transcript = (
            transcription_response
            .json()
            ["transcript"]
        )

        st.session_state.messages.append(
            {
                "role": "user",
                "content": transcript
            }
        )

        with st.chat_message(
            "user"
        ):

            st.markdown(
                transcript
            )

        ws_url = (
            BACKEND_URL
            .replace(
                "https://",
                "wss://"
            )
            .replace(
                "http://",
                "ws://"
            )
        )

        ws = websocket.create_connection(
            f"{ws_url}/ws/chat"
        )

        payload = {

            "session_id":
                st.session_state.session_id,

            "message":
                transcript
        }

        ws.send(
            json.dumps(
                payload
            )
        )

        full_response = ""

        assistant_placeholder = (
            st.empty()
        )

        while True:

            chunk = ws.recv()

            if chunk == "[END]":

                break

            full_response += chunk

            assistant_placeholder.markdown(
                full_response
            )

        ws.close()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )

        speech_response = requests.post(
            f"{BACKEND_URL}/api/speak",

            json={
                "text": full_response
            },

            timeout=120
        )

        st.audio(
            speech_response.content,
            format="audio/mp3"
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )