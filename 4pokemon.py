from flask import Flask, request, render_template, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('poke.html')

@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    if request.method == 'POST':
        pokemoncari = request.form['pokemons'].lower()
        url = 'https://pokeapi.co/api/v2/pokemon/'
        x = requests.get(url+pokemoncari)
        if x.status_code == 200:
            id = x.json()['id']
            height = x.json()['height']
            weight = x.json()['weight']
            name = x.json()['name'].capitalize()
            img = x.json()['sprites']['front_default']
            detail = {
                'id':id, 'height':height, 'weight':weight,
                'name':name, 'img':img
            }
            return render_template('result.html', data=detail)
            # return x.json()
        else:
            return '404'

if __name__ == '__main__':
    app.run(debug=True, port= 5000)