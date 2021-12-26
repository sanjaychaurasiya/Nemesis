# Nemesis

Heroku Link :- https://nemesis12345.herokuapp.com/

Urls detail -
1.https://nemesis12345.herokuapp.com/        
used to get all the registered users and also to register/post a user.

2.https://nemesis12345.herokuapp.com/<id:intger>/     
used to get a particular user and perform put/patch and delete request. 

3.https://nemesis12345.herokuapp.com/login/
used to login a registered used, it returns the access and refresh token of the user.

4.https://nemesis12345.herokuapp.com/api/token/refresh/
used to get new access token. Accept Post request with refresh token.

5.https://nemesis12345.herokuapp.com/register/
Used to register a user. Accept Post request with username, email, password and confirmpassword, information should be in json format.
