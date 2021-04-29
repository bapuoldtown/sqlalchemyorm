from sqlalchemy import *
from sqlalchemy.orm import *
from orm3 import *

Session=sessionmaker(bind=engine)
session=Session()
'''Add address objects into the table'''
#add4=Addresses(states_address="Rayleigh, North carolina")
#session.add(add4)
#session.commit()
'''Get the user object and add an address by issuing a join statement'''


usrobj=session.query(User).join(Addresses).filter(User.name.like('t%')).first()


'''Display all rows here'''
#for r in usrobj.addresses:
    #print(r)


'''Demonstrates left join or left outer join michael left being user right being address'''
results=session.query(Addresses,User).outerjoin(User,User.id == Addresses.user_id).all()

'''Demonstrates right join with Address on left and user on right'''
results=session.query(Addresses,User).outerjoin(User,User.id == Addresses.user_id).all()

for r in results:
    print(r.User.name)
