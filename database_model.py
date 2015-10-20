from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

# Create a new declarative_base for our database model
Base = declarative_base()

# The following classes create tables in our database
class User(Base):
    '''
    Database table for User information from OAuth provider

    Information is peeled from the Google+ user account stored in the
    login_session during execution of gconnect() and createUser() in
    itemcatalog.py when logging into the catalog.
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    picture = Column(String)


class Category(Base):
    '''Table for information about each category'''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String) # HTTP link to image instead of image data
    created = Column(DateTime, default = datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    @property
    def serialize(self):
        '''Return object data in easily serializeable format for JSON and XML'''
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'photo': self.photo,
            'user_id': self.user_id,
            'created': self.created,
        }

class Item(Base):
    '''Table for information about items'''
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String) # HTTP link to image instead of image data
    created = Column(DateTime, default = datetime.now)
    # Foreign key relation now deletes child items when category is removed
    category_id = Column(Integer, ForeignKey('categories.id',
                                              ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    category = relationship(Category)

    @property
    def serialize(self):
        '''Return object data in easily serializeable format for JSON and XML'''
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'photo': self.photo,
            'category_id': self.category_id,
            'user_id': self.user_id,
            'created': self.created,
        }

# Create a new engine instance for the specified database
engine = create_engine('postgresql://flaskapp:flaskypassy@localhost/itemcatalog')
# Create the tables and relationships defined in our classes
Base.metadata.create_all(engine)
