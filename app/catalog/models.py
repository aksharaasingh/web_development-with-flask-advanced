from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Publisher is {}'.format(self.name)

class Book(db.Model):
    __tablename__ = 'book'



    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)


    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

class Data(db.Model):
    __tablename__ = 'data_collected'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    state = db.Column(db.String(30))
    district = db.Column(db.String(40))
    crop = db.Column(db.String(50))
    season = db.Column(db.String(13))
    sowing_month = db.Column(db.String(10))
    harvesting_month = db.Column(db.String(10))

    def __init__(self,name,state,district,crop,season,sowing_month,harvesting_month):
        self.name = name
        self.state = state
        self.district = district
        self.crop = crop
        self.season = season
        self.sowing_month = sowing_month
        self.harvesting_month = harvesting_month

