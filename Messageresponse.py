import streamlit as st
from google import genai


import os
from dotenv import load_dotenv


# MUST call load_dotenv() before accessing env variables
load_dotenv()

# Initialize client using the loaded key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


st.set_page_config(
    page_title="AI Message Reply Generator",
    layout="centered"
)

st.title("AI Message Reply Generator")

st.write(
    "Paste a message and generate a clear and suitable reply."
)

received_message = st.text_area(
    "Received Message",
    placeholder="Example: Hi, can you please send me the project details?",
    height=180
)

reply_tone = st.selectbox(
    "Select Reply Tone",
    [
        "Professional",
        "Friendly",
        "Polite",
        "Formal",
        "Short and Direct",
        "Customer Support"
    ]
)

reply_language = st.selectbox(
    "Select Reply Language",
    [
        "English",
        "Hindi",
        "Hinglish"
    ]
)

additional_instruction = st.text_input(
    "Additional Instruction",
    placeholder="Example: Mention that I will send the details tomorrow"
)

if st.button(
    "Generate Reply",
    type="primary",
    use_container_width=True
):

    if received_message.strip() == "":
        st.warning("Please enter the received message.")

    else:
        prompt = f"""
You are a WhatsApp message reply assistant.

Create a suitable reply to the following WhatsApp message.

Received Message:
{received_message}

Reply Tone:
{reply_tone}

Reply Language:
{reply_language}

Additional Instruction:
{additional_instruction}

Instructions:
- Write a clear and natural WhatsApp reply.
- Follow the selected tone and language.
- Keep the reply suitable for WhatsApp.
- Do not make the reply unnecessarily long.
- Do not add headings or explanations.
- Return only the reply message.
"""

        with st.spinner("Generating reply..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.success("Reply generated successfully.")

        st.subheader("Generated Reply")

        st.text_area(
            "Reply",
            value=response.text,
            height=200,
            label_visibility="collapsed"
        )

