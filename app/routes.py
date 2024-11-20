from werkzeug import Response
from flask import render_template, request, redirect, url_for
from app import app

profiles: list[dict] = []

@app.route('/', methods=['POST', 'GET'])
def index() -> Response | str:
    if request.method == 'POST':
        name: str = request.form.get('user_name')
        city: str = request.form.get('user_city')
        age: str = request.form.get('user_age')
        hobby: str = request.form.get('user_hobby')

        if name and city and age and hobby:
            profiles.append({'name': name, 'city': city, 'age': age, 'hobby': hobby})
            return redirect(url_for('index'))

    return render_template('people.html', profiles=profiles)