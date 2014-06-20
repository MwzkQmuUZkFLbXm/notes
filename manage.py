# -*- coding: utf-8 -*-

from app import app
from models import Note
import views

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=False)
