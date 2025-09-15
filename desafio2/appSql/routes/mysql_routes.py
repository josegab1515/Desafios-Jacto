from flask import Blueprint, jsonify, request
from controllers.crud_mysql import get_all_cars, get_car_by_id, post_cars, put_cars, delete_cars
from models.cars_schema import CarSchema, ValidationError
car_bp = Blueprint("car_bp", __name__)

@car_bp.route("/cars/mysql", methods = ["GET"])
def get_all_cars_route():
    data = get_all_cars()
    return jsonify(data)

@car_bp.route("/cars/mysql/<int:car_id>", methods=["GET"])
def get_car_by_id_route(car_id):
    car = get_car_by_id(car_id)
    if car:
        return jsonify(car)
    else:
        return jsonify({"error": "Carro não encontrado"}), 404

@car_bp.route("/cars/mysql", methods = ["POST"])
def post_cars_route():
    data = request.json
    carros = data if isinstance(data, list) else [data]
    try:
        carros_validados = [CarSchema(**car).dict() for car in carros]
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422

    return jsonify(post_cars(carros_validados)), 201

@car_bp.route("/cars/mysql/<int:car_id>", methods = ["PUT"])
def put_cars_route(car_id):
    car = request.json
    if car:
        return jsonify(put_cars(car_id, car))
    else:
        return jsonify({"error": "Carro não encontrado"}), 404

@car_bp.route("/cars/mysql/<int:car_id>", methods=["DELETE"])
def delete_cars_route(car_id):
    result = delete_cars(car_id)
    if result:
        return jsonify({"message": f"Carro com ID {car_id} deletado com sucesso!"})
    else:
        return jsonify({"error": "Carro não encontrado"}), 404



