import mysql.connector
from faker import Faker

fake = Faker()

# fake generators
fake_tagname = fake.ripe_id()

# connect to mysql database
connection = mysql.connector.connect(host='localhost', database='leftovers', user='leftover', password='9.Leftovers')

def test_db():
    # Connect to MySQL database
    assert connection.is_connected() == True
    

my_cursor=connection.cursor()

def test_append():
    # print(connection)
    # query = "SELECT * FROM customer"
    query = "INSERT INTO tbl_tag(name) VALUES(%s)"
    
    # query to insert all the v information about an account in tuple form
    tag = (str(fake_tagname),)
    
    my_cursor.execute(query, tag)
    connection.commit()

    for data in my_cursor: #getting all the names using the loop
        print(data)
        
    print(my_cursor.rowcount, "records are inserted.")



def test_read():
    # read data of all the columns from the table
    query = "SELECT * FROM tbl_tag"
    my_cursor.execute(query)
    res = my_cursor.fetchall() #storing the output of fetchall() in the res
    for row in res: #printing all the records in res
        print(row)
        

def test_delete_table():
    query = "DROP TABLE tbl_tag"
    my_cursor.execute(query)
    print("table successfully deleted")
    
test_append()
test_read()
# test_delete_table()