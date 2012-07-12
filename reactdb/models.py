from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    Unicode,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session (sessionmaker (extension=ZopeTransactionExtension () ) )
Base = declarative_base ()

image_keyword_association = Table ('image_keyword_association', Base.metadata,
    Column ('image_id', BigInteger, ForeignKey ('image.id', ondelete = 'cascade') ),
    Column ('keyword_id', BigInteger, ForeignKey ('keyword.id', ondelete = 'cascade') ),
    mysql_engine = 'InnoDB'
)

class InnoDB (object):
    __table_args__ = {'mysql_engine': 'InnoDB'}

class Image (Base, InnoDB):
    __tablename__ = 'image'

    id = Column (BigInteger, primary_key = True)
    filename = Column (Unicode (30), unique = True)

    keywords = relationship ('Keyword', secondary = image_keyword_association, backref = 'images')

    def __init__ (self, filename):
        self.filename = filename

class Keyword (Base, InnoDB):
    __tablename__ = 'keyword'

    id = Column (BigInteger, primary_key = True)
    value = Column (Unicode (30), unique = True)

def initialize_db (engine):
    DBSession.configure (bind = engine)
    Base.metadata.bind = engine
    Base.metadata.create_all (engine)
