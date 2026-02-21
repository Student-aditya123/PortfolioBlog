import os
from groq import Groq
from django.conf import settings
from .prompts import SYSTEM_PROMPT

client = Groq(api_key=settings.GROQ_API_KEY)


def get_chatbot_response(user_message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # CURRENT WORKING MODEL
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=300,
        )

        return response.choices[0].message.content

    except Exception as e:
        print("GROQ ERROR:", e)
        return "Sorry, I'm having trouble responding right now."