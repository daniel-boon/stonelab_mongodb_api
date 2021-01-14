from pymongo import MongoClient 

# client = MongoClient()
myclient = MongoClient('mongodb://admin:secure@18.140.247.237:2277')

#Create a database, it will not show up until you put some data in it
mydb = myclient['stonelab']

#Create collection (table)
mycol = mydb['customers']
#-------------------------------------------------------------

#insert one document
# mydata = {'name':'john', 'address':'highway 37'}
# result = mycol.insert_one(mydata)
#-------------------------------------------------------------

#insert multiple documents
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# result = mycol.insert_many(mylist)
#-------------------------------------------------------------

#list all databases
# for db in myclient.list_databases():
#     print(db)
#-------------------------------------------------------------
#find one
# x = mycol.find_one()
# print(x)
#-------------------------------------------------------------
#find all
# for x in mycol.find():
#   print(x)
#-------------------------------------------------------------
#find all only some fileds
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)
#-------------------------------------------------------------

# for x in mycol.find({},{ "address": 0 }):
#   print(x)
#-------------------------------------------------------------
#query
# myquery = { "address": "Park Lane 38" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)
#-------------------------------------------------------------

# myquery = { "address": { "$gt": "S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x) 
#-------------------------------------------------------------
#find with regex
# myquery = { "address": { "$regex": "^S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)
#-------------------------------------------------------------
#sort 1 = asc, -1 = desc
# mydoc = mycol.find().sort("name", -1)

# for x in mydoc:
#   print(x)
#-------------------------------------------------------------
#limit
# myresult = mycol.find().limit(5)

#print the result:
# for x in myresult:
#   print(x)
#-------------------------------------------------------------
#update
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }

# mycol.update_one(myquery, newvalues)

#print "customers" after the update:
# for x in mycol.find():
#   print(x)
#-------------------------------------------------------------
#update many
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }

# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")
#-------------------------------------------------------------

#delete
# myquery = { "address": "Mountain 21" }

# mycol.delete_one(myquery)
#-------------------------------------------------------------
#delete many
# myquery = { "address": {"$regex": "^S"} }

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")
#-------------------------------------------------------------
#delete all documents
# x = mycol.delete_many({})

# print(x.deleted_count, " documents deleted.")
#-------------------------------------------------------------
#drop collection
# mycol.drop()


