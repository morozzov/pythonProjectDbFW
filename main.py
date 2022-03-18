import user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
import json


engine = create_engine('postgresql+psycopg2://Username:Password@Host/Database')

# user.DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

newUser = User(login="user5", password="user5pass", name="user5name")
session.add(newUser)
session.commit()

for currentUser in session.query(User):
    print(json.dumps(currentUser.as_dict()))
    print(currentUser.id, " ", currentUser.login, " ", currentUser.password, " ", currentUser.name)