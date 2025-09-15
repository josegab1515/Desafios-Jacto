from database.db_mongo import get_mongo_connection
from bson import ObjectId

def get_all_cars():
    db = get_mongo_connection()
    cars = list(db.carros.find({}))
    for car in cars:
        car["_id"] = str(car["_id"])
    return cars

def get_car_by_id(car_id):
    db = get_mongo_connection()
    try:
        car = db.carros.find_one({"_id": ObjectId(car_id)})
        if car:
            car["_id"] = str(car["_id"])
        return car
    except Exception as e:
        print(f"Erro ao buscar carro por ID: {e}")
        return None

def post_cars(cars):
    db = get_mongo_connection()
    result = db.carros.insert_many(cars)
    new_cars = []
    for inserted_id, car in zip(result.inserted_ids, cars):
        car["_id"] = str(inserted_id)
        new_cars.append(car)
    return new_cars

def put_cars(car_id, car):
    db = get_mongo_connection()
    result = db.carros.update_one(
        {"_id": ObjectId(car_id)},
        {"$set": car}
    )
    if result.modified_count > 0:
        return {"_id": car_id, **car}
    else:
        return None

def delete_cars(car_id):
    db = get_mongo_connection()
    result = db.carros.delete_one({"_id": ObjectId(car_id)})
    if result.deleted_count > 0:
        return {"deleted": True, "id": car_id}
    else:
        return None