# from app.extensions import db
# from datetime import datetime


# class Company(db.Model):
#  __tablename__="Companies"
#  id =db.Column(db.Integer,primary_key=True)
#  name=db.Column(db.String(50),nullable=False,unique=True)
#  origin =db.Column(db.String(50),nullable=False)
#  description=db.Column(db.String(100),nullable=False)
#  created_at =db.Column(db.DateTime,default=datetime.now())
#  updated_at =db.Column(db.DateTime,onupdate=datetime.now()) 
#  user_id =db.Column(db.Integer, db.ForeignKey("users.id"))
#  user=db.relationship('User',backref='Companies')
 
 
#  def __init__(self,name,origin,description,user_id):
#       super(Company  ,self).__init__()
#       self.name= name
#       self.origin= origin
#       self.description= description
#       self.user_id= user_id
        
#  def __repr__(self):
#         return f'{self.name} {self.origin}'

