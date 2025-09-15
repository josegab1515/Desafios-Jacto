from flask import Flask
from routes.mysql_routes import car_bp

app = Flask(__name__)
app.register_blueprint(car_bp)

if __name__ == "__main__":
    app.run(debug=True)