import hashlib
import uuid
import pymysql.cursors

connection = pymysql.connect(host='mrbartucz.com',
                             user='sq8822nj',
                             password='Whyskar|3301',
                             db='sq8822nj_Assignment_Four',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# user input
salt = uuid.uuid4().hex
userInput = input("Enter a Username: ")
passwordInput = input("Enter a Password: ")
print("Password + Salt = " + passwordInput + str(salt))

# call encode
encoded = hashlib.sha512((passwordInput + salt).encode('utf-8')).hexdigest()
print("Hashed Password: " + encoded)
args = (userInput, encoded)

# add to db
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO Us3r_Acc0unts (username, password)" \
              "VALUES (%s, %s)"
        cursor.execute(sql, args)

        connection.commit()

        sql = "SELECT * FROM Us3r_Acc0unts WHERE userName LIKE %s AND password LIKE %s"
        cursor.execute(sql, args)
except Exception as e:
    print(e)
finally:
    connection.close()

print("\nUser Data has been stored within the Database")

while True:
    userInput2 = input("\nEnter your Username: ")
    passwordInput2 = input("Enter your Password: ")

    if userInput == userInput2 and passwordInput == passwordInput2:
        print("\nCongratulations, you are signed in!")
        break
    else:
        print("Invalid Entry")
