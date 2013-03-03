from sqlalchemy import Column, Integer, String, Text, DateTime
from flaski.database import Base
from datetime import datetime
from docutils.core import publish_parts
overrides = {'doctitle_xform': 0,
             'initial_header_level': 2}


class WikiContent(Base):
    __tablename__ = 'wikicontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)

    @property
    def html(self):
        parts = publish_parts(source=self.body,
                              writer_name="html",
                              settings_overrides=overrides
                              )
        return parts['html_body']
