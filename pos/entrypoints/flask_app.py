from flask import Flask, jsonify, request
from pos.service_layer.services import create_company
from pos.service_layer import create_compay, unit_of_work

app = Flask(__name__)

@app.route("companies", methods=['POST'])
def create_compay():
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    create_company(request.json['fiscal_name'],
                   request.json['comercial_name'], request.json['rfc'], uow)
