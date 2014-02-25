import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Sanyam', 'lastname':'Kamat'}
print doc
print "About to insert the document"

try:
	users.insert(doc)
except:
	print "Insert failed: ", sys.exc_info()[0]

print doc

print "\nInserting again"
# Without this reassignment pymongo would have given below ERROR
# insert failed:  <class 'pymongo.errors.DuplicateKeyError'>
doc = {'firstname':'Sanyam', 'lastname':'Kamat'}
try:
	users.insert(doc)
except:
	print "insert failed: ", sys.exc_info()[0]

print doc