import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class ToukouUser(db.Document):
    userId      = db.IntField( unique=True )
    fnameJp     = db.StringField( max_length=8 )
    lnameJp     = db.StringField( max_length=16 )
    fnameEn     = db.StringField( max_length=16 )
    lnameEn     = db.StringField( max_length=20 )
    username    = db.StringField( max_length=12, unique=True)
    email       = db.StringField( max_length=40, unique=True )
    password    = db.StringField( max_length=16 )
    statusNow   = db.StringField( max_length=30 )
    university  = db.StringField( max_length=100 )
    majorType   = db.StringField( max_length=10 )
    country     = db.StringField( max_length=30 )
    #picture     = db.StringField( max_length=30 )

    def SetPassword(self, password):
        self.password = generate_password_hash(password)

    def GetPassword(self, password):
        return check_password_hash(self.password, password)

class IppanUser(db.Document):
    userId      = db.IntField( unique=True )
    username    = db.StringField( max_length=12, unique=True )
    email       = db.StringField( max_length=40, unique=True )
    statusNow   = db.StringField( max_length=30, unique=True )