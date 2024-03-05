from website import crate_app
from flask import Flask, render_template

app = crate_app()   

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    #if __name__ == '__main__': (means only when app is launched the code will execute)