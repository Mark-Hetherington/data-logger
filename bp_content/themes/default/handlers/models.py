from google.appengine.ext import ndb

# Put here your models or extend User model from bp_includes/models.py
class DataPoint(ndb.Model):
    path = ndb.StringProperty(required=True)
    value = ndb.IntegerProperty(required=True)
    units = ndb.StringProperty(required=True)
    when = ndb.DateTimeProperty(auto_now_add=True)