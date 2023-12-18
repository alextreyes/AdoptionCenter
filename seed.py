from app import app
from models import db, Pet  

db.drop_all()
db.create_all()


pet1 = Pet(name='choe',
           species='idk' )
pet2 = Pet(name='chloer',
           species='idk')
pet3 = Pet(name='chossse',
           species='idkbutmaybe')
pet4 = Pet(name='chossse',
           species='idkbutmaybe',
           available = False)

pets = [pet1,pet2,pet3,pet4]
db.session.add_all(pets)
db.session.commit()