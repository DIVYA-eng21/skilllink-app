import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator

# ------------------ Page Config ------------------
st.set_page_config(page_title="SkillLink AI", page_icon="💼", layout="centered")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("background.jpg");
    background-size: cover;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
.chat-bubble-user {
    background-color: #DCF8C6;
    border-radius: 1.2rem;
    padding: 10px;
    margin-bottom: 10px;
    max-width: 80%;
    margin-left: auto;
    word-wrap: break-word;
}
.chat-bubble-ai {
    background-color: #E6E6FA;
    border-radius: 1.2rem;
    padding: 10px;
    margin-bottom: 10px;
    max-width: 80%;
    margin-right: auto;
    word-wrap: break-word;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "active" not in st.session_state:
    st.session_state.active = True


# ------------------ Model Loading ------------------
@st.cache_resource
def load_model():
    model_name = "Divya21026/flan-skilltitle-model"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

with st.spinner("Loading SkillLink AI model... please wait ⏳"):
    tokenizer, model = load_model()
translator = GoogleTranslator(source='auto', target='en')
st.success("Model loaded successfully ✅")

# ------------------ Title ------------------
#st.image("logo.png", width=150)
st.markdown("<h2 style='text-align:center;'>💼 SkillLink AI</h2>", unsafe_allow_html=True)
st.write("Describe your skill in any language and I’ll predict your job title! 🌍")
# ------------------ Chat Form ------------------
st.markdown("### 💬 Chat with SkillLink AI")

# Use form to prevent page reload
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your skill description (type 'quit' to end):")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    if user_input.lower() == "quit":
        st.session_state.active = False
        st.session_state.conversation.append(("user", user_input))
        st.session_state.conversation.append(("ai", "Session ended. Goodbye! 👋"))
    elif st.session_state.active:
        # Translate input to English
        translated = translator.translate(user_input)

        # Generate prediction
        input_text = f"Given a worker's skill description, generate a short job title.\nDescription: {translated}\nTitle:"
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=16)
        title = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Save conversation
        st.session_state.conversation.append(("user", user_input))
        st.session_state.conversation.append(("ai", title))

# ------------------ Display Chat ------------------
for role, text in st.session_state.conversation:
    if role == "user":
        st.markdown(f"<div class='chat-bubble-user'><b>You:</b> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-ai'><b>SkillLink AI:</b> {text}</div>", unsafe_allow_html=True)