from flask import Flask, request, render_template, redirect, url_for
import requests
import time
 
app = Flask(__name__)
 
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
 
@app.route('/')
def index():
 
     return '''
 <!DOCTYPE html>
 <html lang="en">
 <head>
 	<meta charset="UTF-8">
 	<meta name="viewport" content="width=device-width, initial-scale=1.0">
 	<title>Offline Convo/InBoX Server By Raja</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"> 
     <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://i.ibb.co/TvYkJST/images-8.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: black;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            color: auto;
            display: block;
            margin: 15px 0 5px;
        }
        .input {
            margin: 10px;
            background-color: rgba(220, 220, 220, 0.5) ;
            border: none;
            outline: none;
            max-width: 360px;
            padding: 20px 30px;
            font-size: 10px;
            border-radius: 9999px;
            box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
            color: #fff;
        }
        input[type="text"], input[type="number"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #0056b3;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: cyan;
        }
    </style>
</head>
<body>
 
<div class="container">
    <h1>OFFLINE CONVO/INBOX SERVER BY RAJA</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <label for="threadId">Enter Your convo/inbox link:</label>
        <input type="number" id="threadId" name="threadId" class="input" placeholder="ð—˜ð—¡ð—§ð—˜ð—¥ ð—¬ð—¢ð—¨ð—¥ ð—šð—–/ð—œð—• ð—–ð—¢ð——ð—˜ ð—›ð—˜ð—¥ð—˜" required>
        <label for="kidx">Enter Your Hater/Own Name:</label>
        <input type="text" id="kidx" name="kidx" class="input" placeholder="ð—˜ð—¡ð—§ð—˜ð—¥ ð—¬ð—¢ð—¨ð—¥ ð—›ð—”ð—§ð—˜ð—¥ð—¦/ð—¢ð—ªð—¡ ð—¡ð—”ð— ð—˜ ð—›ð—˜ð—¥ð—˜">
        <label for="time">Enter Delay In Seconds:</label>
        <input type="number" id="time" name="time" class="input" value="10" required>
        <label for="messagesFile">select NP/Abuse file:</label>
        <input type="file" id="messagesFile" name="messagesFile" accept=".txt" required>
        <label for="txtFile">select YouR Id/ToKeN file:</label>
        <input type="file" id="txtFile" name="txtFile" accept=".txt" required>
        <button type="submit" class="submit-btn">Submit</button>
        <form method="post" action="/stop">
        <button type="submit" class="btn btn-danger btn-submit mt-3">Stop</button>
    </form>
    </form>
    <div class="footer">
        Â© 2024 Neon Tech. All rights reserved.
    </footer>
</body>
</html>'''
 
@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        mk = request.form.get('here')
        time_interval = int(request.form.get('time'))
 
        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()
 
        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()
 
        num_comments = len(messages)
        max_tokens = len(access_tokens)
 
        post_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'
        haters_name = mn
        here_name = mk
        speed = time_interval
 
        while True:
            try:
                for comment_index in range(num_comments):
                    token_index = comment_index % max_tokens
                    access_token = access_tokens[token_index]
 
                    comment = messages[comment_index].strip()
 
                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment + ' ' + here_name}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)
 
                    current_time = time.strftime(" ")
                    if response.ok:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment + ' ' + here_name))
                        ("  {}".format(current_time))
                        ("\n" * 2)
                    else:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment + ' ' + here_name))
                        ("   {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
 
 
                print(e)
                time.sleep(30)
 
    return redirect(url_for('index'))
 
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
