from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    return '''
        <html>
        <head>
        </head>
        <body>
            <button id="clickbutton" onclick="pressMeFunction()">Press me</button>
            <h2 id="put-text-in-here"></h2>
            <script>
                function pressMeFunction() {
                    document.getElementById("put-text-in-here").innerHTML = "Hello CircleCI!";
                }
            </script> 
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')