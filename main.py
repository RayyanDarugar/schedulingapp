import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from flask import Flask, jsonify
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers


# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.player import player_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():  # activate these items 
    initJokes()
    initUsers()
    initPlayers()

@app.route('/api/data')
def get_data():
    # start a list, to be used like a information database
    user_stats = []

    # add a row to list, an Info record
    user_stats.append({
        "ingredient_id": 10000,
        "ingredient_name": "Glycerin",
        "purpose": "Skin-Identical Ingredient, Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/glycerin",
    })

    # add a row to list, an Info record
    user_stats.append({
        "ingredient_id": 10001,
        "ingredient_name": "Hyaluronic Acid",
        "purpose": "Skin-Identical Ingredient, Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/hyaluronic-acid",
    })
    
    user_stats.append({
        "ingredient_id": 10002,
        "ingredient_name": "Niacinamide",
        "purpose": "Cell-Communicating Ingredient, Skin Brightening, Anti-Acne, Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/niacinamide",
    })
    
    user_stats.append({
        "ingredient_id": 10003,
        "ingredient_name": "Glycolic Acid",
        "purpose": "Exfoliant, Buffering",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/glycolic-acid",
    })
    
    user_stats.append({
        "ingredient_id": 10004,
        "ingredient_name": "Snail Secretion Filtrate",
        "purpose": "Antioxidant, Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/snail-secretion-filtrate",
    })
    
    user_stats.append({
        "ingredient_id": 10005,
        "ingredient_name": "Lactic Acid",
        "purpose": "Exfoliant, Moisturizer, Buffering",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/lactic-acid",
    })
    
    user_stats.append({
        "ingredient_id": 10006,
        "ingredient_name": "Retinol",
        "purpose": "Cell-Communicating Ingredient",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/retinol",
    })
    
    user_stats.append({
        "ingredient_id": 10007,
        "ingredient_name": "Tretinoin",
        "purpose": "Cell-Communicating Ingredient",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/tretinoin",
    })
    
    user_stats.append({
        "ingredient_id": 10008,
        "ingredient_name": "Pantheol",
        "purpose": "Soothing, Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/pantheol",
    })
    
    user_stats.append({
        "ingredient_id": 10009,
        "ingredient_name": "1,2-Hexanediol",
        "purpose": "Solvent",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/1-2-hexanediol",
    })
    user_stats.append({
        "ingredient_id": 10010,
        "ingredient_name": "1,2-Hexanediol",
        "purpose": "Solvent",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/1-2-hexanediol",
    })
    
    
    return jsonify(user_stats)


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="5001")
