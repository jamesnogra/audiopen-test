# Uses the model meta-llama/Llama-2-70b-chat-hf according to https://github.com/Soulter/hugging-chat-api
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Log in to huggingface and grant authorization to huggingchat
sign = Login(os.getenv('GPT_EMAIL'), os.getenv('GPT_PASSWORD'))
# Save cookies to the local directory
cookies = sign.login()
cookie_path_dir = "./cookies_snapshot"

# Summarizes a long text
def summarize_transciption(full_text):
    try:
        print('Getting summary from the full text using meta-llama/Llama-2-70b-chat-hf model...')
        sign.saveCookiesToDir(cookie_path_dir)
        # Create the summary
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
        summary = chatbot.chat(f'Summarize as few words as possible the text "{full_text}"?')
        # New a conversation to create a title
        print('Getting title from the full text using meta-llama/Llama-2-70b-chat-hf model...')
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        title = chatbot.chat(f'Can you summarize in less than 10 words the text "{full_text}"?')
        print('Success in getting a summary and title using meta-llama/Llama-2-70b-chat-hf model......')
        return summary.replace('<|endoftext|>', ''), title.replace('<|endoftext|>', '')
    except Exception as e:
        print(e)
        return f'Error: {e} meta-llama/Llama-2-70b-chat-hf https://github.com/Soulter/hugging-chat-api', 'Error'
    