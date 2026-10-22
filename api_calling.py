from google import genai
from dotenv import load_dotenv
import os



#loading the environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#Initializing client
client = genai.client(api_key = api_key)

#note generator
def note_generate(images):
    prompt = "Summarize the picture in note format at max 100 words, make sure to add necessary markdown to differentiate different section"
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [images, prompt]
        )
    return response.text