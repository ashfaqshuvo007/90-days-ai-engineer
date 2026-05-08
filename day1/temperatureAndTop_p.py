from google import genai
from google.genai import types
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

#? Fiddling with default generation parameters. e.g. temperature, top_p etc.
#* temperature controls the randomness of the output. 
#*    - Higher (e.g., 0.8) makes it more random.
#*    - While lower (e.g. 0.1) makes it more focused and deterministic.
#* 

# responseWithLowTemperature = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=["Explain how AI works"],
#     config=types.GenerateContentConfig(
#         temperature=0.1
#     )
# )


# print(responseWithLowTemperature.text)
# print("============\n")

# responseWithHighTemperature = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=["Explain how AI works"],
#     config=types.GenerateContentConfig(
#         temperature=0.8
#     )
# )
# print(responseWithHighTemperature.text)

#? Text generation with different top_p values.
#* top_p (nucleus sampling/probaility mass) - diversity control.
#*   - Higher (e.g., 0.9) allows for more diverse outputs by considering a larger pool of potential next words.
#*   - Lower (e.g., 0.3) - output more focused and deterministic - by considering only the most probable next words.

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        temperature=0.8,
        top_p=0.3
    )
)
print(response.text)