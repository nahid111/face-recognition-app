from app import db

class Students(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(12))
    name = db.Column(db.String(20))
    imageName = db.Column(db.String(300))
    imageData = db.Column(db.LargeBinary)
    imageEncodings = db.Column(db.PickleType)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, user, password):
    	self.user = user
    	self.password = password



# for Creating the tables
# python3
# from app import db
# db.create_all()

