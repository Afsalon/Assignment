# Assignment
Assignment for interview
The Assigment consists of 3 Models 
User
Content 
Category(extra)

User model inherits AbstractUser, instead of using the usual approach of creating a one to one relationship with the default user model.


The Content model has a foreign key relationship with category model and User model.

The user field on content is not editable, the current logged in user is used.


create_admins.py script can be used for seeding 


python manage.py shell < create_admins.py running this command completes the seeding process, and creates 3 superusers/admins


all apis besides signup/create user requires authorization 


jwt authentication is used, passed as bearer token in postman and verified all the apis.

![crows](https://github.com/Afsalon/Assignment/assets/68525687/ac062e27-cde8-44e6-b0ab-7c927e7fe0d2)

<img width="1385" alt="history-bg" src="https://github.com/Afsalon/Assignment/assets/68525687/686dc167-2d17-4afb-ba9a-e01b4c2dc92e">

Admin can create, get,edit and delete any content 


other non superusers can only perform CRUD on their contents.


