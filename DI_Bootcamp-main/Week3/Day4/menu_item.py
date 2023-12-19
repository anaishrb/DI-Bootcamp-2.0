import psycopg2
conn=psycopg2.connect(
    dbname='user_management',
    user='postgres',
    password='pgjav',
    host='localhost',
    port='5432'
)


# Create a cursur object to execute SQL queries
cur = conn.cursor()

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

def save(self):
        conn = self.connect_to_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                               (self.name, self.price))
                conn.commit()
                cursor.close()
                print("Item saved successfully")
            except psycopg2.Error as e:
                print("Error saving item:", e)
            finally:
                conn.close()
        else:
            print("Connection to the database failed")

    # Add other methods: delete, update...

if __name__ == "__main__":
    # Creating a new menu item instance
    new_item = MenuItem(None, "Pizza", 15)

    # Saving the new item to the database
    new_item.save()

conn.commit()


cur.close()
conn.close()