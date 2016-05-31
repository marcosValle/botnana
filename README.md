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

#ToDo
1. C&C collect data from daemon
    1.1 daemon collects data
    1.2 daemon sends data
    1.3 create table for victim's data (optional)
    1.4 create page to show these data

2. C&C respond with command
    2.1 Create commands list in daemon
    2.2 create C&C interface to send commands
    2.3 put command in response
    2.4 daemon executes command
    2.5 daemon sends feedback
    2.2 Set
