from os import environ as env
from flask import request, render_template
from server import init_server
from libs.debug import debug_print

app = init_server()

@app.route('/')
def index():
    return render_template('index.html')

def main():

    port = int(env.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
    main()
