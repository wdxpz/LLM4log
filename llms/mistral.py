import sys
import os
import json

import httpx
import google.auth
from google.auth.transport.requests import Request

app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import global_config

config = global_config()


def get_credentials():
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    return credentials.token

def build_endpoint_url(
    region: str,
    project_id: str,
    model_name: str,
    model_version: str,
    streaming: bool = False,
):
    base_url = f"https://{region}-aiplatform.googleapis.com/v1/"
    project_fragment = f"projects/{project_id}"
    location_fragment = f"locations/{region}"
    specifier = "streamRawPredict" if streaming else "rawPredict"
    model_fragment = f"publishers/mistralai/models/{model_name}@{model_version}"
    url = f"{base_url}{'/'.join([project_fragment, location_fragment, model_fragment])}:{specifier}"
    return url


# Retrieve Google Cloud Project ID and Region from environment variables
project_id = config.project.PROJECT_ID
region = config.mistral.LOCATION


# Retrieve Google Cloud credentials.
access_token = get_credentials()


model = config.mistral.MODEL_ID
model_version = config.mistral.MODEL_VERSION
is_streamed = config.mistral.is_streamed # Change to True to stream token responses


# Build URL
url = build_endpoint_url(
    project_id=project_id,
    region=region,
    model_name=model,
    model_version=model_version,
    streaming=is_streamed
)


# Define query headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json",
}

def complete_mistral(prompt):
    # Define POST payload
    data = {
        "model": model,
        "messages": [{"role": "user", "content": f"{prompt}"}],
        "stream": is_streamed,
    }


    # Make the call
    with httpx.Client() as client:
        resp = client.post(url, json=data, headers=headers, timeout=None)
        return json.loads(resp.content)['choices'][0]['message']['content']

if __name__ == '__main__':
  prompt = "Who is the best French painter?"

  result = complete_mistral(prompt)
  print(result)