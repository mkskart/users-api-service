from flask import request, jsonify, Blueprint
from . import db
from .models import User
from .schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def register_routes(app):
    bp = Blueprint('users', __name__)

    @bp.route('/users', methods=['POST'])
    def create_user():
        # Validate and deserialize input
        data = user_schema.load(request.json)
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(user_schema.dump(new_user)), 201

    @bp.route('/users', methods=['GET'])
    def get_users():
        all_users = User.query.all()
        return jsonify(users_schema.dump(all_users)), 200

    @bp.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        return jsonify(user_schema.dump(user)), 200

    @bp.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        data = user_schema.load(request.json)
        user.name = data.get('name')
        user.email = data.get('email')
        db.session.commit()
        return jsonify(user_schema.dump(user)), 200

    @bp.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200

    app.register_blueprint(bp)