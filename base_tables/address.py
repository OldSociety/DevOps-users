import mysql.connector
from faker import Faker

fake = Faker()

# fake generators
fake_email = fake.email()

# intentionally using country codes for testing
fake_state = fake.country_code()

fake_country = fake.current_country()
fake_zip = fake.postcode()
fake_houseNum = fake.building_number()
fake_address = fake.street_name()
fake_suffix = fake.street_suffix()

# connect to mysql database
connection = mysql.connector.connect(host='localhost', database='leftovers', user='leftover', password='9.Leftovers')

def test_db():
    # Connect to MySQL database
    assert connection.is_connected() == True
    

my_cursor=connection.cursor()

def test_append():
    # print(connection)
    # query = "SELECT * FROM customer"
    query = "INSERT INTO tbl_address(latitude, longitude, zip_code, country, state, street_address, house_number, unit_number) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    
    # query to insert all the v information about an account in tuple form
    address = ("97.00", "97.00", str(fake_zip), str(fake_country), str(fake_state), str(fake_address) + " " + str(fake_suffix), str(fake_houseNum), "C")
    
    my_cursor.execute(query, address)
    connection.commit()

    for data in my_cursor: #getting all the names using the loop
        print(data)
        
    print(my_cursor.rowcount, "records are inserted.")



def test_read():
    # read data of all the columns from the table
    query = "SELECT * FROM tbl_address"
    my_cursor.execute(query)
    res = my_cursor.fetchall() #storing the output of fetchall() in the res
    for row in res: #printing all the records in res
        print(row)
        

def test_delete_table():
    query = "DROP TABLE tbl_address"
    my_cursor.execute(query)
    print("table successfully deleted")
    
test_append()
test_read()
# test_delete_table()