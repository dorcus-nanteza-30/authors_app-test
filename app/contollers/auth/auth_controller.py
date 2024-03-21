from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED
import validators
from app.models.users import User
from app.extensions import db,bcrypt



auth = Blueprint('auth', __name__,url_prefix='/api/v1/auth')

#user registration

@ auth.route('/register',methods=['POST'])
def register_user():
    data = request.Json
    first_name= data.get('first_name')
    last_name= data.get('last_name')
    contact= data.get('contact')
    email= data.get('email')
    type= data.get('type') if'user_type' is data else "author" 
    password= data.get('password')
    biography= data.get('biography') if type=='author' else''
    
    #validation of data
    
    if not first_name or not last_name or not contact or not password or not email:
        return jsonify({"error": "All fields are requied"}),HTTP_400_BAD_REQUEST
    
    if type =='author'and not biography:
        return jsonify({"error": "Enter your author biography"}),HTTP_400_BAD_REQUEST
    
    if len(password)<8:
        return jsonify({"error": "Password must be at least 8 characters"}),HTTP_400_BAD_REQUEST
    
    if not validators.email(email):
         return jsonify({"error": "email is not valid"}),HTTP_400_BAD_REQUEST
     
    if User.query.filter_by(email=email).first() is not None:
         return jsonify({"error": "email is already in use"}),HTTP_409_CONFLICT
     
    if User.query.filter_by(contact= contact).first() is not None:
         return jsonify({"error": "contact is already registered"}),HTTP_409_CONFLICT
     
    try:
        #hashing password
      hashed_password = bcrypt.generate_password_hash('password')
      #creating a new user
      new_user= User(first_name=first_name,last_name=last_name,password= hashed_password,email=email,contact=contact,biography=biography,user_type= User)
      db.session.add(new_user)
      db.session.commit()
      
      #username
      username= new_user.get_full_name()
      
      return jsonify({
        'message': username + 'has been successfully created as an' +new_user.user_type,
          'user':{
              'id':new_user.id,
              'first_name':new_user.first_name,
              'last_name':new_user.last_name,
              'email':new_user.email,
              'contact':new_user.contact,
              'biography':new_user.biography,
              'user_type':new_user.user_type
          }
      }),HTTP_201_CREATED
      
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    
    
    # defining the delete user endpoint 
    # @auth.route('/delete/<int:user_id>', method=['DELETE']) 
    # def delete_user(user_id):
    #     try:
    #         user = user.query.get(user_id)
    #         if not user:
    #             return jsonify({'error':'user not found'}),
            
         
    #         db.session.delete(user)
    #         db.session.commit()
             
    #         return jsonify({'message':'user deleted successfully'}),HTTP_201_CREATED
         
         
    #     except Exception as e:
    #       db.session.rollback()
    #       return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    
    
    
    
    
    
