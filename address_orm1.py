from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from orm3 import User,engine,Addresses


Session=sessionmaker(bind=engine)
session=Session()

'''Address objects are created'''
tim = User(name='timothy', fullname='Timothy Wiilams', nickname='timmy')
session.add(tim)
session.commit()



'''Associate a Address object with jack user object'''
add1=Addresses(states_address="Mineapolos , Minnesota")
add2=Addresses(states_address="Illinois , Chicago")


#userobj=session.query(User.id,User.addresses).filter(User.name.ilike('j%')).one_or_none()
tim.addresses.extend([add1,add2])
session.add(tim)
session.commit()
'''Add a 3 address to the Tim user'''
#add3=Addresses(states_address="Sunnyvale , CaliFornia")
userobj=session.query(User).filter(User.name.ilike('t%')).one_or_none()
for a in userobj.addresses:
    print(a.states_address)
'''Demonstrate a join between User and Address'''


