import base64
import os
from webapp2_extras import security
import yaml
import bp_includes.models as models

def basic_auth(func):
  def callf(webappRequest, *args, **kwargs):
    # Parse the header to extract a user/password combo.
    auth_header = webappRequest.request.headers.get('Authorization')
    # if the auth header is missing popup a login dialog
    if auth_header == None:
      __basic_login(webappRequest)
    else:
      (username, password) = base64.b64decode(auth_header.split(' ')[1]).split(':')
      if(__basic_lookup(username) == __basic_hash(password)):
        return func(webappRequest, *args, **kwargs)
      else:
        __basic_login(webappRequest)
  return callf

def __basic_login(webappRequest):
  webappRequest.response.set_status(401, message="Authorization Required")
  webappRequest.response.headers['WWW-Authenticate'] = 'Basic realm="Secure Area"'

def __basic_lookup(username):
    user = models.User.query(models.User.username==username).fetch()
    if len(user) == 1:
        return __basic_hash(user[0].password)

def __basic_hash(password):
  return security.hash_password(password, method='sha1')