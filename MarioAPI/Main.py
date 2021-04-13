from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import cross_origin
from db import add_player, add_rating, add_level, get_levels, get_players, get_ratings

app = Flask(__name__)
@app.route('/levels', methods=['POST', 'GET'])
@cross_origin()
def levels():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        
        return add_level(request.get_json())
    
    return get_levels()

@app.route('/players', methods=['POST', 'GET'])
@cross_origin()
def players():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        return add_player(request.get_json())
    return get_players()

@app.route('/ratings', methods=['POST', 'GET'])
@cross_origin()
def ratings():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        
        return add_rating(request.get_json())
    return get_ratings()


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='192.168.1.111', port=8080, debug=True)