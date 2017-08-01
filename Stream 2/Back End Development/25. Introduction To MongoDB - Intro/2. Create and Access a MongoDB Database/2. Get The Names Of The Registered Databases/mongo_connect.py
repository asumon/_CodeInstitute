import pymongo

def mongo_connect():
    try:
        connection = pymongo.MongoClient()
        print "MongoDB is connected!"
        return connection
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

connection = mongo_connect()
db = connection['twitter_stream']
print conn.database_names()  # [u'local', u'test']
