# Assignment
Assignment for interview
The Assigment consists of 3 Models 
User
Content 
Category(extra)

User model inherits AbstractUser, instead of using the usual approach of creating a one to one relationship with the default user model.


The Content model has a foreign key relationship with category model. 


create_admins.py script can be used for seeding 


python manage.py shell < create_admins.py running this command completes the seeding process, and creates 3 superusers/admins


all apis besides signup/create user requires authorization 


jwt authentication is used, passed as bearer token in postman and verified all the apis.



Admin can create, get,edit and delete any content 


other non superusers can only perform CRUD on their contents.


