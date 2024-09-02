from flask import Flask
from my_flasky.my_app.routes.app import user_bp

app = Flask(__name__, template_folder="templates")

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
