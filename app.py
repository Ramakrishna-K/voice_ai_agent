
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from ollama import Client

# app = Flask(__name__)
# CORS(app)

# # CONNECT OLLAMA
# ollama_client = Client(host="http://localhost:11434")

# # =========================================
# # CONVERSATION MEMORY
# # =========================================
# conversation_history = []

# SYSTEM_PROMPT = """
# You are Mitra AI Assistant.

# Founder Rules:

# If anyone asks:
# Who created you?
# Who made you?
# or similar questions,

# Reply:
# I was created by Ramakrishna Katravath

# If anyone asks:
# Who is your founder?
# Who is the founder of Ram AI?
# Who founded you?

# Reply:
# My founder name is Ramakrishna Katravath

# General Rules:

# Give short and clear answers.

# For greetings and thanks:
# Reply normally in one line.

# For educational or topic based questions:
# Answer in structured numbered points.

# Keep answers readable and well formatted.

# Do not speak or explain special symbols in voice output.

# Ignore symbols while speaking, including:
# ! @ # $ % ^ & * ( ) ~ ` { } [ ] : " < > / \\

# Convert responses into clean natural speech format before voice output.

# Do not read markdown symbols or formatting characters in voice.

# Keep responses simple and voice friendly.

# Use this format:

# 1. Title or main point: Explanation.

# 2. Title or main point: Explanation.

# 3. Title or main point: Explanation.
# Sub point
# Sub point

# 4. Title or main point: Explanation.

# Additional Rules:

# Put each numbered point on a new line.

# Keep spacing between points.

# Do not combine all points into one paragraph.

# Use simple bullet points only when needed.

# Make answers easy to understand.

# If code is given:

# Explain concepts step by step.

# Keep formatting clean and readable.

# Do not add unnecessary explanations.
# """

# # ---------------- HOME ----------------
# @app.route("/", methods=["GET"])
# def home():
#     return jsonify({
#         "message": "AI Server Running"
#     })

# # ---------------- CHAT ----------------
# @app.route("/chat", methods=["POST"])
# def chat():

#     try:

#         global conversation_history

#         data = request.get_json()

#         user_message = data.get("message", "")

#         # SAVE USER MESSAGE
#         conversation_history.append({
#             "role": "user",
#             "content": user_message
#         })

#         # LIMIT MEMORY
#         if len(conversation_history) > 20:
#             conversation_history = conversation_history[-20:]

#         # FULL CHAT HISTORY
#         messages = [
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             }
#         ] + conversation_history

#         response = ollama_client.chat(
#             model="llama3",
#             messages=messages
#         )

#         ai_reply = response["message"]["content"]

#         # SAVE AI RESPONSE
#         conversation_history.append({
#             "role": "assistant",
#             "content": ai_reply
#         })

#         return jsonify({
#             "reply": ai_reply
#         })

#     except Exception as e:

#         return jsonify({
#             "error": str(e)
#         })

# # ---------------- CLEAR MEMORY ----------------
# @app.route("/clear", methods=["POST"])
# def clear_memory():

#     global conversation_history

#     conversation_history = []

#     return jsonify({
#         "message": "Conversation history cleared"
#     })

# # ---------------- RUN ----------------
# if __name__ == "__main__":

#     app.run(
#         host="0.0.0.0",
#         port=8000,
#         debug=False
#     )


from flask import Flask, request, jsonify
from flask_cors import CORS
from ollama import Client
import os

app = Flask(__name__)
CORS(app)

# =========================================
# CONNECT OLLAMA
# =========================================
ollama_client = Client(host="http://localhost:11434")

# =========================================
# CONVERSATION MEMORY
# =========================================
conversation_history = []

# =========================================
# SYSTEM PROMPT
# =========================================
SYSTEM_PROMPT = """
You are Mitra AI Assistant.

Founder Rules:

If anyone asks:
Who created you?
Who made you?
or similar questions,

Reply:
I was created by Ramakrishna Katravath

If anyone asks:
Who is your founder?
Who is the founder of Ram AI?
Who founded you?

Reply:
My founder name is Ramakrishna Katravath

General Rules:

Give short and clear answers.

For greetings and thanks:
Reply normally in one line.

For educational or topic based questions:
Answer in structured numbered points.

Keep answers readable and well formatted.

Do not speak or explain special symbols in voice output.

Ignore symbols while speaking, including:
! @ # $ % ^ & * ( ) ~ ` { } [ ] : " < > / \\

Convert responses into clean natural speech format before voice output.

Do not read markdown symbols or formatting characters in voice.

Keep responses simple and voice friendly.

Use this format:

1. Title or main point: Explanation.

2. Title or main point: Explanation.

3. Title or main point: Explanation.
Sub point
Sub point

4. Title or main point: Explanation.

Additional Rules:

Put each numbered point on a new line.

Keep spacing between points.

Do not combine all points into one paragraph.

Use simple bullet points only when needed.

Make answers easy to understand.

If code is given:

Explain concepts step by step.

Keep formatting clean and readable.

Do not add unnecessary explanations.
"""

# =========================================
# HOME ROUTE
# =========================================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Server Running 🚀"
    })

# =========================================
# CHAT ROUTE
# =========================================
@app.route("/chat", methods=["POST"])
def chat():

    try:

        global conversation_history

        data = request.get_json()

        user_message = data.get("message", "")

        # SAVE USER MESSAGE
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # LIMIT MEMORY
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]

        # FULL CHAT HISTORY
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + conversation_history

        # OLLAMA RESPONSE
        response = ollama_client.chat(
            model="llama3",
            messages=messages
        )

        ai_reply = response["message"]["content"]

        # SAVE AI RESPONSE
        conversation_history.append({
            "role": "assistant",
            "content": ai_reply
        })

        return jsonify({
            "reply": ai_reply
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

# =========================================
# CLEAR MEMORY ROUTE
# =========================================
@app.route("/clear", methods=["POST"])
def clear_memory():

    global conversation_history

    conversation_history = []

    return jsonify({
        "message": "Conversation history cleared"
    })

# =========================================
# RUN FLASK SERVER
# =========================================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        debug=False
    )
