# Mini Project 4

This project is to practice and learn Python Django!

## Description

For the project I followed along with the tutorials linked in acknowledgments. The Youtube series was followed
to learn how to incorporate my own code into the project. The tutorial is well documented in the tutorial link below.
I also found an additional that was loosely followed with login/authentication and well as a small use of ChatGPT to
understand login/authentication better, so I could incorporate those pages in my project myself. This project is a 
polls website that I flavored into a Halo E-sports poll site. There is also the admin side iof these project that 
shows how to easily manage the site, or you can create a account and just be a normal user. More information on that 
will be in teh Executing Programs below. 

### Dependencies

```
pip install -r requirements.txt
```

### Executing program
First run this so that the SQL entries go into your database 
```
python manage.py makemigrations
```

Next you need to run apply the migrations using this command
```
python manage.py migrate
```

To create a admin user for the admin side of the project us the command below
```
python manage.py createsuperuser
```
After the superuser is made and you execute the program you will load a page to your localhost, from there in the url
type /admin and use the superuser info to login to the admin side. If you wan to be a normal user you can register one 
on the admin side or you can use /polls/login and click register then register a account this way to and login through
the login page to see it from a none admin account. 

## Authors

Riley Weaver


## Acknowledgments

Inspiration, code snippets, etc.
* [Login/authentication](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication)
* [Youtube](https://www.youtube.com/watch?v=UB7XFf0Q_M4)
* [Tutorial](https://docs.djangoproject.com/en/4.2/)
* [ChatGPT]((https://chatgpt.com/share/67f3098f-b0c0-8005-bd08-754c64af7082))
