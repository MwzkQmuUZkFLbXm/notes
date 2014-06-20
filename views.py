# -*- coding: utf-8 -*-

from flask import abort, jsonify, render_template, request
from app import app
from models import Note

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        notes = Note.objects(archived=False)
    return render_template('index.html',notes=notes)


@app.route('/create', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form.get('content'):
            note = Note(content=request.form['content'])
            note.save()
            rendered = render_template('note.html', note=note)
            return jsonify({'note':rendered, 'success': True})
        return jsonify({'success': False})

    notes = Note.objects(archived=False)
    return render_template('homepage.html', notes=notes)

@app.route('/archive/<id>/',methods=['POST'])
def archive_note(id):
    try:
        Note.objects(id=id).update(set__archived=True)
    except Note.DoesNotExist:
        abort(404)
    return jsonify({'success': True})

@app.route('/delete/<id>/', methods=['POST'])
def delete(id):
    try:
        pass
    except Note.DoesNotExist:
        abort(404)
    return jsonify({'success': True})

