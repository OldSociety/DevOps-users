import mysql.connector
from faker import Faker

fake = Faker()

# fake generators
fake_name = fake.company()
fake_address = fake.address()
fake_phone = fake.msisdn()
fake_url = fake.url()
fake_time = fake.time()

# connect to mysql database
connection = mysql.connector.connect(host='localhost', database='leftovers', user='leftover', password='9.Leftovers')

def test_db():
    # Connect to MySQL database
    assert connection.is_connected() == True
    

my_cursor=connection.cursor()

def test_append():
    # print(connection)
    query = "INSERT INTO tbl_restaurant(name, address_id, phone_no, website, open_time, close_time, rating, rating_count) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    
    # query to insert all the v information about an account in tuple form
    account = (str(fake_name), "1",str(fake_phone), str(fake_url), str(fake_time), str(fake_time), "4.0", "7")
    
    my_cursor.execute(query, account)
    connection.commit()

    for data in my_cursor: #getting all the names using the loop
        print(data)
        
    print(my_cursor.rowcount, "records are inserted.")



def test_read():
    # read data of all the columns from the table
    query = "SELECT * FROM tbl_restaurant"
    my_cursor.execute(query)
    res = my_cursor.fetchall() #storing the output of fetchall() in the res
    for row in res: #printing all the records in res
        print(row)
        

def test_delete_table():
    query = "SET FOREIGN_KEY_CHECKS=0; DROP TABLE tbl_restaurant"
    my_cursor.execute(query)
    print("table successfully deleted")
    
test_append()
test_read()
# test_delete_table()