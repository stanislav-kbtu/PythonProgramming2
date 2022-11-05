import mysql.connector as sql

class DatabaseManager():

    def __init__(self):
        self.db = sql.connect(host = 'localhost', user = 'root', password = 'rootpassword23')
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS airline")
        self.db.commit()
        self.db.connect(database = 'airline')
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS passengers (user_login VARCHAR(255) NOT NULL PRIMARY KEY, 
        passwords VARCHAR(255), first_name VARCHAR(255), second_name VARCHAR(255), number_of_flights INT, penalty BOOLEAN, Age INT)""")
        self.db.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS flights(flight_id INT PRIMARY KEY,  airplane VARCHAR(255), from_city VARCHAR(255), to_city VARCHAR(255), 
        date_time DATETIME, departure_time VARCHAR(255), arrival_time VARCHAR(255), tickets INT(5))""")
        self.db.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tickets (passenger_login VARCHAR(255), flight_id INT, 
        place INT(20), cost INT(20), place_status VARCHAR(255), 
        FOREIGN KEY(passenger_login) REFERENCES passengers (user_login), FOREIGN KEY(flight_id) REFERENCES flights(flight_id))""")
        self.db.commit()

    def select_from_passengers_by_login(self, login):
        self.cursor.execute(f"SELECT * FROM passengers WHERE user_login = '{login}'")
        return self.cursor.fetchall()

    def select_from_flights_by_flightid(self, id):
        self.cursor.execute(f"SELECT * FROM flights WHERE flight_id = {id}")
        return self.cursor.fetchall()
    
    def insert_into_passengers(self, values1: list): # value = [('cd', 'Habib', 'csd', 'csasx', 10, False, 20)]
        query = 'INSERT INTO passengers (user_login, passwords, first_name, second_name, number_of_flights, penalty, Age) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        self.cursor.executemany(query, values1)
        self.db.commit()

    def insert_into_flights(self, values2: list): 
        query = 'INSERT INTO flights (flight_id,  airplane , from_city, to_city, date_time, departure_time, arrival_time, tickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
        self.cursor.executemany(query, values2)
        self.db.commit()

    def insert_into_tickets(self, values3: list):
        query = 'INSERT INTO tickets (passenger_login, flight_id, place, cost , place_status) VALUES (%s, %s, %s, %s, %s);'
        self.cursor.executemany(query, values3)
        self.db.commit()
    
    def delete_from_tickets_by_login(self, login, flight_id, seat):
        query = f"DELETE FROM tickets WHERE passenger_login='{login}' AND flight_id = {flight_id} AND place = {seat};"
        self.cursor.execute(query)
        self.db.commit()

    def select_from_flights(self, city_from = None, city_to = None, month = None):
        if city_from == None and city_to == None and month != None:
            query = f'SELECT * FROM flights WHERE MONTH(date_time) = {month}'
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data if len(data) != 0 else None
        else:
            part1 = 'SELECT * FROM flights'
            part2 = f' WHERE from_city = "{city_from}"' if city_from != None else ""
            part3 = f' AND to_city = "{city_to}"' if city_to != None else ""
            part4 = f' AND MONTH(date_time) = {month}' if month != None else ""
            self.cursor.execute(part1 + part2 + part3 + part4)
            data = self.cursor.fetchall()
            return data if len(data) != 0 else None

    def select_from_tickets_by_flight_id(self, id):
        query = f'SELECT * FROM tickets WHERE flight_id = "{id}"'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_from_tickets_by_login(self, login):
        self.cursor.execute(f"SELECT * FROM tickets WHERE passenger_login = '{login}'")
        return self.cursor.fetchall()

    def modify_tickets_in_flights(self, flight_id, add = True):
        query = f"UPDATE flights SET tickets = tickets - 1 WHERE flight_id = {flight_id}" if not add else f"UPDATE flights SET tickets = tickets + 1 WHERE flight_id = {flight_id}"
        self.cursor.execute(query)
        self.db.commit()

    def fill_flights_table(self):
        values = [
        (100, 'A501', 'Astana', 'Almaty', '2022-11-20 18:40:00', '18:40:00', "20:15", 60),
        (101, 'A502', 'Almaty', 'Astana', '2022-11-21 18:50:00', '18:50', "20:20", 60),
        (102, 'A503', 'Astana', 'Aturay', '2022-11-22 11:40:00', '11:40', "16:05", 60),
        (103, 'A504', 'Aktau', 'Aturay', '2022-11-22 14:40:00', '14:40', "18:20", 60),
        (104, 'A505', 'Shumkent', 'Taraz', '2022-11-22 16:40:00', '16:40', "19:15", 60),
        (105, 'A506', 'Taraz', 'Aktobe', '2022-11-23 15:45:00', '15:45', "18:30", 60),
        (106, 'A507', 'Semey', 'Karagnda', '2022-11-27 18:40:00', '18:40', "20:15", 60),
        (107, 'A508', 'Shymkent', 'Kyzylorda', '2022-11-30 21:40:00', '21:40', "23:35", 60),
        (108, 'A509', 'Taraz', 'Almaty', '2022-12-02 8:40:00 ', '8:40', "10:20", 60),
        (109, 'A510', 'Astana', 'Semey', '2022-12-3 10:50:00', '10:50', "14:45", 60),
        (110, 'A511', 'Taraz', 'Aktau', '2022-12-4 9:35:00', '9:35', "13:15", 60)
        ]
        self.insert_into_flights(values)
        print("Data filled in flights successfully.")

    def fill_passengers_table(self):
        values = []
        for i in range(2, 45):
            values.append((f'{i}', f'{i}', f'{i}', f'{1}', 0, 0, 18))
        self.insert_into_passengers(values)
        print("Data filled in passengers successfully.")

    def fill_tickets_table(self):
        values = []
        for i in range(2, 45):
            DB.modify_tickets_in_flights(102, add = False)
            values.append((f'{i}', 102, i, 4000, 'Econom class'))
        self.insert_into_tickets(values)
        print("Data filled in tickets successfully.")


DB = DatabaseManager()
#DB.fill_passengers_table()
#DB.fill_flights_table()
#DB.fill_tickets_table()
