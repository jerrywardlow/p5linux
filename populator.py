from database_model import *

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#Create User
test_user = User(name="Jan Ullrich",
                 email="info@janullrich.de",
                 picture="http://i.imgur.com/M8kYwF4.jpg")
session.add(test_user)
session.commit()

#Create Categories
test_category1 = Category(user_id=1,
                         name="Bicycles",
                         description="Bicycles are the most efficient human powered means of transportation.",
                         photo="http://i.imgur.com/tPHRk6r.jpg")
session.add(test_category1)
session.commit()

test_category2 = Category(user_id=1,
                         name="Knives",
                         description="Knives are the LEAST efficient means of human powered transportation.",
                         photo="http://i.imgur.com/9vnMa4h.jpg")
session.add(test_category2)
session.commit()

#Create Test Items
item1 = Item(user_id=1,
             category_id=1,
             name="Giant TCR Composite",
             description='Built with many of the same design philosophies as bikes ridden by Giant pros, TCR Composite delivers sharp handling and snappy acceleration with just enough compliance for racing and long training days. The PowerCore bottom bracket area and asymmetrical chainstays produce maximum pedaling efficiency. The OverDrive steerer tube technology, which features a tapered, oversized design, adds front-end stiffness and steering precision.',
             photo='http://i.imgur.com/XLQT0UH.jpg')
session.add(item1)
session.commit()

item2 = Item(user_id=1,
             category_id=1,
             name='Bianchi XL Evolution EV4',
             description='This is the lightest frame and complete bike, for lighter riders and serious climbers. The frame is an ultra high performance, triple-butted, foam reinforced 7000 series aluminum hyperalloy with wall thickness that varies from 1.15mm to 0.6mm and gives an ultimate tensile strength of 650 N/mm2. MegaTube Evolution down tube. Bianchi patented structural foam injection. The fork is the Bianchi Reparto Corse XL full carbon.',
             photo='http://i.imgur.com/a7pkVc3.jpg')
session.add(item2)
session.commit()

item3 = Item(user_id=1,
             category_id=2,
             name="Kershaw Blur",
             description='Like all Blurs it is equipped with a big, slightly recurved blade that is ideal for multitasking. The blade shape offers both excellent slicing and piercing capabilities and the high-performance Sandvik 14C28N stainless blade steel offers corrosion resistance and hardness. The black Blur has a DLC (Diamond-Like Carbon) coated blade for extra corrosion resistance and enhanced looks.',
             photo='http://i.imgur.com/kNRowVk.png')
session.add(item3)
session.commit()

item4 = Item(user_id=1,
             category_id=2,
             name="CRKT Squid",
             description='This Lucas Burnley-designed everyday carry knife is compact in stature but packs some heat in the features department. It comes with a frame lock for safety, and friction grooves on the drop-point blade for a secure grip. Be careful where you point it.',
             photo='http://i.imgur.com/ZyXfqOV.jpg')
session.add(item4)
session.commit()
