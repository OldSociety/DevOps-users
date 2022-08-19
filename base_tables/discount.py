import mysql.connector
from faker import Faker

fake = Faker()

# fake generators
fake_code = fake.ean(prefixes=('45', '49'))

# connect to mysql database
connection = mysql.connector.connect(host='localhost', database='leftovers', user='leftover', password='9.Leftovers')

def test_db():
    # Connect to MySQL database
    assert connection.is_connected() == True
    

my_cursor=connection.cursor()

def test_append():
    # print(connection)
    # query = "SELECT * FROM customer"
    query = "INSERT INTO tbl_discount(code, percent, value) VALUES(%s, %s, %s)"
    
    # query to insert all the v information about an account in tuple form
    discount = (str(fake_code),"97.00", "5.00")
    
    my_cursor.execute(query, discount)
    connection.commit()

    for data in my_cursor: #getting all the names using the loop
        print(data)
        
    print(my_cursor.rowcount, "records are inserted.")



def test_read():
    # read data of all the columns from the table
    query = "SELECT * FROM tbl_discount"
    my_cursor.execute(query)
    res = my_cursor.fetchall() #storing the output of fetchall() in the res
    for row in res: #printing all the records in res
        print(row)
        

def test_delete_table():
    query = "DROP TABLE tbl_discount"
    my_cursor.execute(query)
    print("table successfully deleted")
    
test_append()
test_read()
# test_delete_table()