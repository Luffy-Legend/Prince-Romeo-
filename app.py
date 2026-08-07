from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Web Server</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #333;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 400px;
                width: 90%;
            }
            h1 {
                color: #4a4a4a;
                margin-bottom: 15px;
                font-size: 24px;
            }
            p {
                color: #666;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            .status-badge {
                display: inline-block;
                background: #28a745;
                color: white;
                padding: 6px 15px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Server Active!</h1>
            <p>Welcome! Your Python Flask server is running live on Render.</p>
            <div class="status-badge">Status: Online</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
