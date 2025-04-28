from flask import request, jsonify
from src.models import db, User

def configure_routes(app):
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([user.username for user in users])
