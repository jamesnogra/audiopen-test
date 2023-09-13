from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login('james.arnold.nogra@fullspeedtechnologies.com', 'Qwerty789&theBrownFox41')
# Save cookies to the local directory
cookies = sign.login()
cookie_path_dir = "./cookies_snapshot"

# Summarizes a long text
def summarize_transciption(full_text):
    sign.saveCookiesToDir(cookie_path_dir)
    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    summary = chatbot.chat(f'Summarize as few words as possible the text "{full_text}"?')
    return summary.replace('<|endoftext|>', '')