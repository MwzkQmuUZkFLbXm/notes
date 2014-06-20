# -*- coding: utf-8 -*-

import datetime
from app import db, oembed
from flask import Markup
from markdown import markdown
from micawber import parse_html

class Note(db.Document):
    content = db.StringField(required=True)
    timestamp = db.DateTimeField(default=datetime.datetime.now,
            required=True)
    archived = db.BooleanField(default=False)

    def __unicode__(self):
        return self.content

    def html(self):
        html = parse_html(
                markdown(self.content),
                oembed,
                maxwidth=300,
                urlize_all=True
                )
        return Markup(html)

    meta = {
            'ordering':['-timestamp']
            }
