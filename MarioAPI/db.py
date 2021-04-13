import os
import pymysql
from flask import jsonify

def open_connection():
    connection = pymysql.connect(host='35.228.63.189',
                                user='root',
                                password='Toilon123',
                                database='mtdb',
                                cursorclass=pymysql.cursors.DictCursor)

    return connection

def get_levels():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM Levels;')
        levels = cursor.fetchall()
        if result > 0:
            got_levels = jsonify(levels)
        else:
            got_levels = 'No levels in DB'
    conn.close()
    return got_levels

def add_level(level):
    conn = open_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO Levels (LevelName, FitnessFunction) VALUES(%s, %s);', (level["LevelName"], level["FitnessFunction"]))
        conn.commit()
        conn.close()
        return "Success! Level added!", 200

    except Exception as exception:
        conn.commit()
        conn.close()
        return str(exception), 500


def get_players():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM Players;')
        levels = cursor.fetchall()
        if result > 0:
            got_players = jsonify(levels)
        else:
            got_players = 'No players in DB'
    conn.close()
    return got_players

def add_player(player):
    conn = open_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO Players (PlayerId, Gender, Age, GamingExperience) VALUES(%s, %s, %s, %s);', (player["PlayerId"], player["Gender"], player["Age"], player["GamingExperience"]))                
        conn.commit()
        conn.close()
        return "Success! Player added!"

    except Exception as exception:
        conn.commit()
        conn.close()
        return str(exception), 500                



def get_ratings():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM Ratings;')
        levels = cursor.fetchall()
        if result > 0:
            got_ratings = jsonify(levels)
        else:
            got_ratings = 'No ratings in DB'
    conn.close()
    return got_ratings

def add_rating(rating):
    conn = open_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO Ratings (PlayerId, LevelName, Enjoyment, Aesthetics, Difficulty) VALUES(%s, %s, %s, %s, %s);', (rating["PlayerId"], rating["LevelName"], rating["Enjoyment"], rating["Aesthetics"], rating["Difficulty"]))
            conn.commit()
            conn.close()
            return "Success! Rating added!"
    except Exception as exception:
        conn.commit()
        conn.close()
        return str(exception), 500