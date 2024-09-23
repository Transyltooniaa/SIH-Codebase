from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from huggingface_hub import InferenceClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Initialize the Hugging Face Inference Client
client = InferenceClient(
    "mistralai/Mistral-Nemo-Instruct-2407",
    token="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",
)

# Temporary storage for recommendations (for simplicity, we use in-memory storage)
recommendation_store = []

# Define a request body model
class SentenceInput(BaseModel):
    input_sentence: str

# POST endpoint to get sentence recommendations
@app.post("/generate_recommendations/")
async def generate_sentence_recommendations(sentence_input: SentenceInput):
    user_input = sentence_input.input_sentence
    messages = [
        {
            "role": "user",
            "content": f"You are a model that will recommend 2-3 sentences so that it helps dyslexic students to write complete sentences based on the following input but do not give extra information.: '{user_input} '",
        }
    ]

    # Store the recommendations in a list
    recommendations = []

    # Call the API for chat completion with a streaming response
    for message in client.chat_completion(
        messages=messages,
        max_tokens=150,
        stream=True,
    ):
        if message.choices[0].delta:
            recommendations.append(message.choices[0].delta.get("content", ""))

    # Join the parts into a single string
    generated_text = "".join(recommendations)

    # Store the result for retrieval via GET later
    recommendation_store.append(generated_text)

    # Return the generated recommendations
    return {"recommendations": generated_text}

# GET endpoint to retrieve all previous recommendations
@app.get("/get_recommendations/", response_model=List[str])
async def get_all_recommendations():
    # Return the stored recommendations
    return recommendation_store

# To run the app, use the command: `uvicorn main:app --reload`
