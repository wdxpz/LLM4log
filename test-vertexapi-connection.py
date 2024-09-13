import vertexai
from vertexai.generative_models import GenerativeModel

import os
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPs_PROXY'] = 'http://127.0.0.1:10809'

# TODO(developer): Update and un-comment below line
project_id = "log-analysis-433902"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

response = model.generate_content(
    "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
)

print(response.text)