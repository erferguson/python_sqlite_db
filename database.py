import sqlite3

# Query The DB & Return All Records
def show_all():
    # Connect to DB
    connection = sqlite3.connect("customer.db")

    # Create a Cursor
    c = connection.cursor()

    # Query the DB
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    print("Command executed successfully...")
    # Commit our command
    connection.commit()

    # Close our connection
    connection.close()

# ADD new record to Table
def add_one(first, last, email):
    # Connect to DB
    connection = sqlite3.connect("customer.db")

    # Create a Cursor
    c = connection.cursor()

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit our command
    connection.commit()

    # Close our connection
    connection.close()

# DELETE Record from Table
def delete_one(id):
    # Connect to DB
    connection = sqlite3.connect("customer.db")
    # Create a Cursor
    c = connection.cursor()

    c.execute("DELETE from customers WHERE rowid = (?)", id)

     # Commit our command & Close our connection
    connection.commit()
    connection.close()

def add_many(list):
    # Connect to DB & Create a Cursor
    connection = sqlite3.connect("customer.db")
    c = connection.cursor()

    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))

     # Commit our command & Close our connection
    connection.commit()
    connection.close()

# Lookup with WHERE
def email_lookup(email):
     # Connect to DB & Create a Cursor
    connection = sqlite3.connect("customer.db")
    c = connection.cursor()

    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,)) # this is a TUPLE, passing one thing -- need the trailing COMMA , 

    items = c.fetchall()
    for item in items:
        print(item)

     # Commit our command & Close our connection
    connection.commit()
    connection.close()


#DELETE Records
# c.execute("DELETE from customers WHERE rowid = 6")

# UPDATE Records
# c.execute("""UPDATE customers SET first_name = 'John'
        # WHERE rowid = 1
    # """)
# connection.commit()

# Query the DB -- Order By
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# Query the DB -- AND/OR
# c.execute("SELECT rowid, * FROM customers LIMIT 4")

# DROP TABLE -- table deleted!
# c.execute("DROP TABLE customers")
# connection.commit()

# WHERE ___ '__'
# LIKE '%__'

# print(c.fetchone()[0])
# print(c.fetchmany(4))
# items = c.fetchall()
# for item in items:
#     print(item)


# FOR loop w/ f"{strings}
# for item in items:
    # print(f"{item[0]} {item[1]} \t {item[2]}")

# print(c.fetchall())

# CREATE a Table w/ doc strings --> 
# c.execute("""CREATE TABLE customers (
    # first_name text,
    # last_name text,
    # email text
    # )""")

# Add MANY
# many_customers = [
    # ('Wes', 'Brown', 'wesb@brown.wes'),
    # ('Jon', 'Appleseed', 'jappleseedb@js.com'),
    # ('Evita', 'Gray', 'ev@gray.com'),
    # ('Calvin', 'Hobbs', 'cb@hobbs.com'),
    # ]

# Add MANY
# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)



# DATA TYPES:
#NULL
# INTEGER
# REAL -- decimal number
# TEXT
# BLOB -- img, mp3