
import pymongo
from icecream import ic



'''
Replace <password> with the password for the <username> user. Replace myFirstDatabase with the name of the database that connections will use by default. 
Ensure any option params are URL encoded.
'''

client = pymongo.MongoClient("mongodb+srv://m220student:m220password@mflix.3souz.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client.server_info()
db = client.list_database_names()

ic(db)
ic('---------------------------------------------')

client1 = pymongo.MongoClient("mongodb+srv://userMongo1:pwdMongo1@cluster0.0njxn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db1 = client1.list_database_names()



ic(db1)

