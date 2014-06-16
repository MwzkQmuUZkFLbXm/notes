#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from models import Note
import views
 
if __name__ == '__main__':
    Note.create_table(True)
    app.run(debug=True)
