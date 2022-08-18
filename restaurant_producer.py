import mysql.connector
from faker import Faker

fake = Faker()
fake.name()

# first and last name generator
fake_name_1 = fake.name()
full_name = fake_name_1.split()

# fake email, phone, password generator
fake_email = fake.email()
fake_phone = fake.msisdn()
fake_pwd = fake.password()

# connect to mysql database
connection = mysql.connector.connect(host='localhost', database='leftovers', user='leftover', password='9.Leftovers')

def test_db():
    # Connect to MySQL database
    assert connection.is_connected() == True
    

my_cursor=connection.cursor()

def test_append():
    # print(connection)
    # query = "SELECT * FROM customer"
    query = "INSERT INTO tbl_restaurant(name, address_id, phone_no, website, open_time, close_time, rating, rating_count) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    
    # query to insert all the v information about an account in tuple form
    account = (str(full_name[0]), str(full_name[1]),str(fake_phone), str(fake_email), str(fake_pwd), "C")
    
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