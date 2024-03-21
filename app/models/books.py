# from app.extensions import db
# from datetime import datetime



# class Books(db.Model):
    
#      __tablename__="books"
#      id =db.Column(db.Integer,primary_key=True)
#      title=db.Column(db.String(150),nullable=False)
#      description=db.Column(db.String(100),nullable=False)
#      image=db.Column(db.String(255),nullable=False)
#      price=db.Column(db.Integer,nullable=False)
#      price_unit=db.Column(db.String(50),nullable=False,default='UGX')
#      pages=db.Column(db.Integer,nullable=False) 
#      publication_date=db.Column(db.Date,nullable=False)
#      isbn = db.Column(db.String(30),nullable= True,unique=True)
#      genre=db.Column(db.String(50),nullable=False)
#      user_id =db.Column(db.Integer, db.ForeignKey("users.id"))
#      company_id=db.Column(db.Integer,db.ForeignKey('Companies.id'))
#      user=db.relationship('User',backref='books')
#      company = db.relationship('Company',backref='books' )
#      created_at = db.Column(db.DateTime,default=datetime.now())
#      updated_at = db.Column(db.DateTime,onupdate=datetime.now())
     
#      def __init__(self,title,description,image,price,price_unit,pages,publication_date,ibsn,genre,company_id,user_id):
#         super(Books,self).__init__()
#         self.title=title
#         self.description=description
#         self.image=image
#         self.price=price 
#         self.price_unit=price_unit
#         self.pages=pages
#         self.publication_date=publication_date
#         self.ibsn=ibsn
#         self.genre=genre
#         self.company_id=company_id
#         self.user_id-user_id
        
#      def __repr__(self):
#         return f'Books {self.Books_title}'