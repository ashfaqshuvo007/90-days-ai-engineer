from google import genai
from google.genai import types
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

#? Text Generation Basic
# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
# )

#? Text generation with thinking 
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does AI work?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_level="low")
#     ),
# )

# print(response.text)