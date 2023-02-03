from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
        <html>
        <head>
            <style>
            body {
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                text-align: center;
            }

        h1 {
            font-size: 48px;
            color: #333;
            margin-top: 50px;
        }
        
        p {
            font-size: 18px;
            color: #555;
            margin-top: 20px;
        }
        </style>
        </head>
        <body>
            <h1>Welcome!</h1>
            <p>We are happy to have you here.</p>
        </body>
        </html>
            """
