from database.db_mysql import get_mysql_connection

def get_all_cars():
    conn = get_mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM cars")
        result = cursor.fetchall()
    conn.close()
    return result

def get_car_by_id(car_id):
    conn = get_mysql_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM cars WHERE id = %s", (car_id,))
        result = cursor.fetchone()
    conn.close()
    return result

def post_cars(cars):
    conn = get_mysql_connection()
    new_cars = []
    with conn.cursor() as cursor:
        for car in cars:
            sql = "INSERT INTO cars (modelo, ano, mpg) VALUES (%s, %s, %s)"
            cursor.execute(sql, (car['modelo'], car['ano'], car['mpg']))
            car_id = cursor.lastrowid
            new_cars.append({"id": car_id, **car})
    conn.commit()
    conn.close()
    return new_cars

def put_cars(car_id, car):
    conn = get_mysql_connection()
    with conn.cursor() as cursor:
        sql = "UPDATE cars SET modelo = %s, ano = %s, mpg = %s WHERE id=%s"
        cursor.execute(sql, (car['modelo'], car['ano'], car['mpg'], car_id))
        conn.commit()
    conn.close()
    return {"id": car_id, **car}

def delete_cars(car_id):
    conn = get_mysql_connection()
    with conn.cursor() as cursor:
        sql = "DELETE FROM cars WHERE id=%s"
        cursor.execute(sql, (car_id,))
        conn.commit()
        deleted = cursor.rowcount
    conn.close()
    return {"deleted": True, "id": car_id} if deleted > 0 else None