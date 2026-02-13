import streamlit as st
# import predict
from predict import predict_intent
st.set_page_config(page_title="ML Chatbot")
st.title("ML Powered Chatbot")
st.write("Chatbot with intent...")
user_input = st.text_input("Enter something")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if st.button("send"):
    if user_input.strip() != "":
        st.session_state.chat_history.append(("You",user_input))
        prediction = predict_intent(user_input)
        if prediction == "greet" :
            response = "Hello how can I help you!!"
        elif prediction == "weather" :
            response = "Current weather is..."
        else:
            response = "I didn't unserstand that"
        st.session_state.chat_history.append(("Bot",response))
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You** {message}")
    else:
        st.markdown(f"**Bot** {message}")