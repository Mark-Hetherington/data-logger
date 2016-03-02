from google.appengine.ext import ndb


class DataPath(ndb.Model):#'path' is key
    units = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)


class DataPoint(ndb.Model):
    path = ndb.KeyProperty(kind=DataPath)
    value = ndb.IntegerProperty(required=True)
    when = ndb.DateTimeProperty(required=True)


class RejectedSubmission(ndb.Model):
    data = ndb.StringProperty(required=True)
    when = ndb.DateTimeProperty(required=True)
