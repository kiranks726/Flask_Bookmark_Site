from Thermos import app,db
from Thermos.Models import User
from flask_script import Manager, prompt_bool

manager=Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="farhan",email="farahan@gmail.com"))
    db.session.add(User(username="vihan", email="vihan@gmail.com"))
    db.session.commit()
    print("Initialized the database")
@manager.command
def dropdb():
    if prompt_bool("Do u want to lose all your data?"):
        db.drop_all()
        print("Dropped the Database")

if __name__=="__main__":
    manager.run()
