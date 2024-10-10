from anthropic import AnthropicVertex

LOCATION="us-east5"
project_id="log-analysis-433902"

client = AnthropicVertex(region=LOCATION, project_id="log-analysis-433902")

message = client.messages.create(
  max_tokens=1024,
  messages=[
    {
      "role": "user",
      "content": "Send me a recipe for banana bread.",
    }
  ],
  model="claude-3-opus",
)
print(message.model_dump_json(indent=2))