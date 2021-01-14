from flask import Flask, request 

app = Flask(__name__, static_folder="../build", static_url_path='/')



@app.route('/')
def index():
    return app.send_static_file('index.html')




@app.route('/api',methods=['GET','POST'])
def api():
    return {
            'userId': 1,
            'tile': 'Flask React Applications',
            'info': 'Aqui va informacion'
        }
