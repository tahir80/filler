import os
import re

DEBUG = False
SECRET_KEY=os.urandom(24)

uri = os.getenv("HEROKU_POSTGRESQL_RED_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_TRACK_MODIFICATIONS=False


# SESSION_TYPE = 'sqlalchemy'
# SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))
# SESSION_TYPE = os.environ.get('SESSION_TYPE')
# SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))
