from google import genai
from google.genai import errors
import os


async def correct_phrases(content:str):

    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

    prompt = (
        "Correct the following text to standard English. Output STRICTLY the "
        "corrected sentence phrases and nothing else. Do not provide options, explanations, "
        f"or conversational filler. Here is the text:\n\n{content}"
    )

    try:
        response = await client.aio.models.generate_content(
            model=os.environ.get("GEMINI_MODEL"),
            contents=prompt
        )
        print(response.text)
        return "true" ,response.text
    except errors.ClientError as e:
        print(f"Gemini API Quota Error: {e}")
        return "false", "We are currently experiencing high traffic. Please try again in a few moments."