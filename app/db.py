import mysql.connector


class Mysql():
    
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "wiom_todo"
        self.init_connection()
    
    def init_connection(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        return self.conn
    
    def create(self, table, data):
        cursor = self.conn.cursor()
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        # Execute query
        cursor.execute(sql, values)
        self.conn.commit()
        return True
    
    def get(self, table, filters={}):
        cursor = self.conn.cursor(dictionary=True)
        query = f"SELECT * FROM {table}"

        if filters:
            conditions = " AND ".join([f"{key} = %s" for key in filters.keys()])
            query += f" WHERE {conditions}"
            values = tuple(filters.values())
        else:
            values = ()

        cursor.execute(query, values)
        results = cursor.fetchall()

        return results
    
    def update(self, table, data, condition):
        cursor = self.conn.cursor()
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        set_values = tuple(data.values())

        where_clause = " AND ".join([f"{key} = %s" for key in condition.keys()])
        where_values = tuple(condition.values())

        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

        cursor.execute(query, set_values + where_values)
        self.conn.commit()
        return 
    
    def raw_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query,())
        self.conn.commit()
        return


# Create a cursor object
# cursor = conn.cursor()

# # Execute a query
# cursor.execute("SELECT DATABASE();")

# # Fetch and print the result
# db_name = cursor.fetchone()
# print("Connected to database:", db_name[0])

# # Close the cursor and connection
# cursor.close()
# conn.close()
