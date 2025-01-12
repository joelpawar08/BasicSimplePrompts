# Simple Prompting Bot

Welcome to the **Simple Prompting Bot**! This project demonstrates a simple chatbot interface powered by **Langflow** and **Streamlit**. The bot processes user input and provides intelligent responses through the Langflow API. I have used **Streamlit** to create a seamless and interactive user interface.

---

## 📝 Project Overview

This chatbot application enables users to ask questions, and it fetches responses from the Langflow API, which processes the input. The application is designed to be simple and easy to use, leveraging **Streamlit** for the front end and **Langflow** for the backend logic.

---

## 🗂️ File Details

1. **`Langflow.py`**:
   - Contains the core Langflow Python API implementation.
   - It does not have any UI integration and focuses solely on handling API requests to Langflow.

2. **`Streamlit.py`**:
   - Integrates the Langflow API with a user-friendly UI using Streamlit.
   - It allows users to enter queries, view responses, and interact with the chatbot seamlessly.

---

## 🔑 API Key Used

This project utilizes the **Gemini API 1.5 Flash** key for Langflow interactions.

---

## 🚀 Demo Link

Check out the live demo of the chatbot application here:

[**Demo Link**](https://joellangapp.streamlit.app)

---

## 🛠️ Technologies Used

- **Langflow**: For processing user input and generating responses.
- **Streamlit**: For creating the interactive web interface.
- **Python**: Backend logic for handling API calls and requests.

---

## 👨‍💻 Developed By

- **Joel Pawar**  
  A Computer Engineering student with a passion for AI, Web Development, and Building Innovative Solutions.

---

## 💡 How It Works

1. **User Input**: The user submits a query through the input field.
2. **API Call**: The input is sent to the Langflow API for processing.
3. **Response**: The response is fetched and displayed back to the user in the chat interface.

---

## ⚙️ Installation

To run this application locally, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/simple-prompting-bot.git
    cd simple-prompting-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run Streamlit.py
    ```

4. Open your browser and navigate to `http://localhost:8501` to view the application.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute or create issues for further improvements. Happy coding! 🎉
