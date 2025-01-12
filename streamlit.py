import streamlit as st
import requests
import json
from PIL import Image

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "468406f1-1b12-48c1-965c-4bbdb89cfd0e"
FLOW_ID = "6f86ed9c-4333-46a8-a0fc-a9a527ab85b4"
APPLICATION_TOKEN = "AstraCS:LmjiylHpKapQNRRNfZsRUcDt:f88ead8132e1f88a4281f7edbb7386c5571fddcc3833d24560f7d0366bc83682"  # Replace with your actual token
ENDPOINT = "JoelPawar"

# Function to call the Langflow API
def run_flow(message: str):
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        try:
            # Extract message text from the response JSON
            response_json = response.json()
            message = response_json.get("outputs", [])[0].get("outputs", [])[0].get("results", {}).get("message", {}).get("text", "")
            return message
        except json.JSONDecodeError:
            return "Error decoding the response JSON."
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit UI
st.set_page_config(page_title="Langflow Chatbot", layout="wide")
st.title("🗣️ Basic Prompting Using Langflow and Streamlit")
st.markdown(
    """
    This application demonstrates a simple chat interface powered by **Langflow** and **Streamlit**. 
    Ask your questions, and get intelligent responses from Langflow's API.
    """
)

# Chat Input
user_query = st.text_input("Enter your query:", placeholder="Type your question here...", label_visibility="collapsed")

# Display Chat History (Optional Feature)
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Submit"):
    if user_query:
        with st.spinner("Fetching response..."):
            response = run_flow(user_query)
        st.success("Response fetched!")
        
        # Add user query and response to history
        st.session_state.history.append({"user": user_query, "response": response})

# Display Chat History
if st.session_state.history:
    st.markdown("### Chat History")
    for chat in st.session_state.history:
        st.markdown(f"**You:** {chat['user']}")
        st.text_area("Response:", value=chat["response"], height=200, max_chars=500, key=f"response_{chat['user']}", disabled=True)

# Flow Image
st.markdown("### Flow Diagram")
flow_image_path = "flow.png"  # Replace with your actual image path
try:
    flow_image = Image.open(flow_image_path)
    st.image(flow_image, caption="Langflow Chat Flow", use_column_width=True)
except FileNotFoundError:
    st.error("Flow image not found. Please ensure the image is available at the specified path.")

# Description
st.markdown("### Description")
st.write(
    "This is a basic chatbot interface that uses Langflow for prompt engineering and Streamlit for creating a simple user interface. "
    "The Langflow API processes user queries and returns intelligent responses. It can handle various user requests and showcase a smooth user experience."
)

# Styling with custom CSS
st.markdown(
    """
    <style>
        .stTextInput input {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stTextArea textarea {
            border-radius: 8px;
            font-size: 16px;
            padding: 10px;
        }
        .stMarkdown {
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True
)
