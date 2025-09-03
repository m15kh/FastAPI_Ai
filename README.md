# FastAPI for AI Model Development

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It is particularly well-suited for serving AI models due to its asynchronous capabilities and ease of use.

## Example: Connecting a Large Language Model (LLM) with FastAPI

Below is an example of how you can use FastAPI to serve an LLM model:

1. Load your AI model (e.g., an LLM) using a library like `transformers`.
2. Create FastAPI endpoints to interact with the model.
3. Deploy the FastAPI app to make the model accessible.

### Visual Representation

The following diagram illustrates the connection between FastAPI and an LLM model:

<div style="display: flex; justify-content: center; gap: 20px;">
    <img src="assets/llm.png" alt="LLM Model with FastAPI Connection" style="width: 300px; height: 300px; object-fit: cover;">
    <img src="assets/vison.png" alt="Vision Generator Model with FastAPI Connection" style="width: 300px; height: 300px; object-fit: cover;">
</div>

This setup allows you to send requests to the FastAPI app, which processes the input and returns the model's response.

---

## How to Run the Application

Follow these steps to run the FastAPI server and Streamlit client:

1. **Start the FastAPI Server**  
   Open a terminal and run the following command:
   ```bash
   uvicorn server:app --reload

2. Start the streamlit Server
    ```bash
    streamlit run client.py



