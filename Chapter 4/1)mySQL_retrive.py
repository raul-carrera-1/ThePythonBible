## DATA TABLE NAME: The data base name
##  age  name  position
##  100  Raul   Boss
##  21   Henry  Cashier



## pip install mysql-connector-python pandas
import mysql.connector, pandas as pd

# Establish connection to MySQL and fetch data into DataFrame

connection = mysql.connector.connect(
    host = "localhost",
    user = "username",
    password = "YourPass",
    database = "The data base name"
)
cursor = connection.cursor()
query = "SELECT * FROM Shop"
cursor.execute(query)
result = cursor.fetchall()

df = pd.DataFrame(result, columns=[col[0] for col in cursor.description])

for index, row in df.iterrows():
    if row['name'] == 'raul':
        print("Hello Boss")
    else:
        print("Hey Custumer")

connection.commit()
cursor.close()
connection.close()

print(df)
# Prints
##  age  name  position
##  100  Raul   Boss
##  21   Henry  Cashier