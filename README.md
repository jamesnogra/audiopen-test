# Installation
 - Install flac `apt-get install flac`
 - Install ffmpeg `apt-get install ffmpeg`
 - Install libraries `pip install -r requirements.txt`

# Start the project
 - Run the command `python app.py`
 - Open browser `http://127.0.0.1:5000`

# Running on Server
 - In the app.py, do not forget to include `sslify = SSLify(app)` after line `app = Flask(__name__)`
 - Add the parameters `port=8443` and `ssl_context=("/etc/letsencrypt/live/www.iamcebu.com/fullchain.pem", "/etc/letsencrypt/live/www.iamcebu.com/privkey.pem")`. Make sure the pem keys are the ones generated by certbot
 - The demo is at https://www.iamcebu.com:8443/