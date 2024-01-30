from flask import Blueprint, request, jsonify
from .models import db, ResourceModel

resources = Blueprint('resources', __name__)


@resources.route('/resources', methods=['GET'])
def get_resources():
    resources = ResourceModel.query.all()
    return jsonify([r.to_dict() for r in resources])


@resources.route('/resources', methods=['POST'])
def add_resource():
    data = request.get_json()
    name = data['name']
    icon_url = data['icon_url']
    desc = data['description']
    resource = ResourceModel(name=name, icon_url=icon_url, description=desc)

    db.session.add(resource)
    db.session.commit()

    return jsonify(resource.to_dict())


@resources.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = ResourceModel.query.get(resource_id)
    return jsonify(resource.to_dict())


@resources.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    data = request.get_json()
    resource = ResourceModel.query.get(resource_id)

    if 'name' in data:
        resource.name = data['name']
    if 'icon' in data:
        resource.icon = data['icon']
    if 'description' in data:
        resource.description = data['description']

    db.session.commit()
    return jsonify(resource.to_dict())