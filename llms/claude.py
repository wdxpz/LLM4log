import sys
import os
app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from anthropic import AnthropicVertex, APIConnectionError, RateLimitError, APIStatusError

from config.config import global_config

config = global_config()

project_id = config.project.PROJECT_ID
MODEL_ID = config.claude.MODEL_ID 
LOCATION = config.claude.LOCATION
# @param ["claude-3-5-sonnet@20240620", "claude-3-opus@20240229", "claude-3-haiku@20240307", "claude-3-sonnet@20240229" ]
# if MODEL == "claude-3-5-sonnet@20240620":
#     available_regions = ["us-east5", "europe-west1"]
# elif MODEL == "claude-3-opus@20240229":
#     available_regions = ["us-east5"]
# elif MODEL == "claude-3-haiku@20240307":
#     available_regions = ["us-east5", "europe-west1"]
# elif MODEL == "claude-3-sonnet@20240229":
#     available_regions = ["us-east5"]
client = AnthropicVertex(region=LOCATION, project_id="log-analysis-433902")

def complete_claude(prompt):
  try:
    message = client.messages.create(
      max_tokens=config.claude.max_tokens,
      messages=[
        {
          "role": "user",
          "content": f"{prompt}",
        }
      ],
      model=MODEL_ID,
      temperature=config.claude.temperature,
      top_p=config.claude.top_p,
      top_k=config.claude.top_k
    )
  except APIConnectionError as e:
      print("The server could not be reached")
      print(e.__cause__)  # an underlying Exception, likely raised within httpx.
  except RateLimitError as e:
      print("A 429 status code was received; we should back off a bit.")
  except APIStatusError as e:
      print("Another non-200-range status code was received")
      print(e.status_code)
      print(e.response)

  print(message.model_dump_json(indent=2))

if __name__ == '__main__':
  prompt = "Send me a recipe for banana bread."
  result = complete_claude(prompt)
  print(result)