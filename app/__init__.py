"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7shrhp8u7g2efktp0-a.oregon-postgres.render.com",
        database="todo_nq7b",
        user="root",
        password="V22Th2wF3l2ax3cea42W7xrwPjdBaCMQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
