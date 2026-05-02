from google import genai
from google.genai import types
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

#? Streaming Responses
#* Chunk responses and process as they arrive. In real applications it leads to better UX and faster response times.

response = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=["Explain how AI works"]
)
for chunk in response:
    print("Received Chunk: \n")
    print(chunk.text, end="")