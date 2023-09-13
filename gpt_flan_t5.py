import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_TOKEN_HUGGINGFACE = os.getenv('HUGGING_FACE_TOKEN')

def summarize_transciption(full_text):
    print('Using google/flan-t5-base GPT model...')
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    headers = {"Authorization": f"Bearer {API_TOKEN_HUGGINGFACE}"}
    # For the summary
    body_summary = {"inputs": f'Summarize as few words as possible the text "{full_text}"?'}
    response_summary = requests.request("POST", API_URL, headers=headers, data= json.dumps(body_summary))
    body_title = {"inputs": f'Can you summarize in less than 10 words the text "{full_text}"?'}
    response_title = requests.request("POST", API_URL, headers=headers, data= json.dumps(body_title))
    # For the title
    try:
        response_summary.raise_for_status()
        response_title.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error:"+" ".join(response_summary.json()['error'])
    else:
        print('Success in getting summary and title using google/flan-t5-base GPT model...')
        return response_summary.json()[0]['generated_text'], response_title.json()[0]['generated_text']