import streamlit as st
from streamlit_chat import message

# ---------------------------------------------
# 🎯 CONFIGURATION
# ---------------------------------------------
st.set_page_config(page_title="EBS App Chatbot Demo", page_icon="⚡", layout="centered")

st.markdown("<h2 style='text-align:center;'>⚡ EBS App Chatbot Demo ⚡</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask me about bill payment, meter reading, or app usage!</p>", unsafe_allow_html=True)

# ---------------------------------------------
# 🧠 Initialize Chat History
# ---------------------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi there! 👋 I’m your EBS App Assistant. How can I help you today?"}
    ]

# ---------------------------------------------
# 🧩 Bot Logic
# ---------------------------------------------
def chatbot_response(user_input):
    text = user_input.lower()

    if any(word in text for word in ["bill", "payment", "pay", "due"]):
        return "You can view and pay your bill directly from the app. Open the meter dashboard. Click on the 👁️ icon to view the current invoice. Click on 'Pay Now' and choose your preferred payment method."

    elif any(word in text for word in ["meter", "reading", "submit"]):
        return "To submit your meter reading, open the app and tap *Submit Reading*. You can even use your phone camera — the app’s OCR feature will auto-detect the numbers!"

    elif any(word in text for word in ["app", "download", "install"]):
        return "You can download the Utility App from the **Play Store** or **App Store**. Just search for *UtilityConnect* and install it."

    elif any(word in text for word in ["help", "support", "contact", "chat"]):
        return "For support, open the app and go to *Help → Chat* to chat with us, *Help → Phone* to call us and *Help → Support Email* to write to us."

    elif any(word in text for word in ["bye", "exit", "thanks", "thank you"]):
        return "You're most welcome! 😊 Have a great day ahead!"

    else:
        return "Hmm... I’m not sure about that. Try asking about *bill payment*, *meter reading*, or *app download*."

# ---------------------------------------------
# 💬 Chat Display
# ---------------------------------------------
for i, msg in enumerate(st.session_state["messages"]):
    if msg["role"] == "user":
        message(msg["content"], is_user=True, key=f"user_{i}")
    else:
        message(msg["content"], key=f"assistant_{i}")

# ---------------------------------------------
# 🧍‍♂️ User Input
# ---------------------------------------------
with st.form("chat_input_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your question here...", key="input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Save user input
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get bot response
    response = chatbot_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})

    st.rerun()
