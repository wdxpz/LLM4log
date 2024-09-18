import sys
import os

import google.auth
from google.auth.transport.requests import Request
import vertexai
# Chat completions API
import openai



app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import global_config

config = global_config()


def get_credentials():
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    return credentials.token

# Retrieve Google Cloud Project ID and Region from environment variables
project_id = config.project.PROJECT_ID
project_region = config.project.LOCATION
model_location = config.llama.LOCATION
vertexai.init(project=project_id, location=project_region) # ,staging_bucket=BUCKET_URI)


# Retrieve Google Cloud credentials.
access_token = get_credentials()

client = openai.OpenAI(
    base_url=f"https://{model_location}-aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/{model_location}/endpoints/openapi/chat/completions?",
    api_key=access_token,
)

MODEL_ID = config.llama.MODEL_ID
apply_llama_guard = config.llama.apply_llama_guard  
temperature = config.llama.temperature  
max_tokens = config.llama.max_tokens 
top_p = config.llama.top_p 
stream = config.llama.stream

def complete_llama(prompt):
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "user", "content": f"{prompt}"},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=stream,
        extra_body={
            "extra_body": {
                "google": {
                    "model_safety_settings": {
                        "enabled": apply_llama_guard,
                        "llama_guard_settings": {},
                    }
                }
            }
        },
    )

    print(response.choices[0].message.content)

if __name__ == '__main__':
  prompt = """
    User input: "What is Vertex AI?"
    Answer: "Sure, Vertex AI is:"
    """
  result = complete_llama(prompt)
  print(result)