I defined the data models for the blog application.

The user will be prompted to enter email, password, and username.

---------
Username (leave blank to use 'xuz17'): 
Email address: 
Password:
Password (again):
---------

And the passowrd is non-visible. If you password is too easy, suach as less than 8 character, 
system will prompt you your password is too easy.

---------
This password is too short. It must contain at least 8 characters.
---------

However, if you just want this password, you can enter y in the following prompt. 

---------
Bypass password validation and create user anyway? [y/N]: 
User created successfully.
---------

Then, run manage.py and go to the blog application website http://127.0.0.1:8000/, it will require the user
to enter the username and password they entered earlier.