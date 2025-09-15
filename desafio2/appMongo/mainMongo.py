from flask import Flask
from routes.mongo_routes import car_bp

app = Flask(__name__)
app.register_blueprint(car_bp)

if __name__ == "__main__":
    app.run(debug=True)