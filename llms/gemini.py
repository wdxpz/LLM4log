import sys
import os
app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import global_config

import vertexai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Part,
)

config = global_config()

PROJECT_ID = config.project.PROJECT_ID
LOCATION = config.project.LOCATION
vertexai.init(project=PROJECT_ID, location=LOCATION)


MODEL_ID = config.gemini.MODEL_ID


model = GenerativeModel(
    MODEL_ID,
    system_instruction=[],
)

# Set safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

def complete_gemini(prompt, response_schema=None):
    # Set contents to send to the model
    contents = [prompt]

    # Counts tokens
    print(model.count_tokens(contents))

    # Prompt the model to generate content
    response = model.generate_content(
        contents,
        generation_config=GenerationConfig(
            temperature=config.gemini.temperature,
            top_p=config.gemini.top_p,
            top_k=config.gemini.top_k,
            candidate_count=config.gemini.candidate_count,
            max_output_tokens=config.gemini.max_output_tokens,
            response_mime_type="application/json",
            response_schema=response_schema,
        ),
        safety_settings=safety_settings,
    )

    # Print the model response
    # print(f"\nAnswer:\n{response.text}")
    # print(f'\nUsage metadata:\n{response.to_dict().get("usage_metadata")}')
    # print(f"\nFinish reason:\n{response.candidates[0].finish_reason}")
    # print(f"\nSafety settings:\n{response.candidates[0].safety_ratings}")
    
    if response.candidates[0].finish_reason != 1: #FINISH_REASON_STOP
       raise Exception(f"Gemini generatoin not naturally stopped, while {str(response.candidates[0].finish_reason)}")

    return response.text

if __name__ == '__main__':
  prompt = """
    User input: I like bagels.
    Answer:
    """
  result = complete_gemini(prompt)
  print(result)