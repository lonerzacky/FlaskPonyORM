import hashlib
import json
import queryUtils

from flask import jsonify


def give_response(response_code, response_message, response_data=""):
    if response_code == "00":
        status = "success"
    else:
        status = "failed"
    response = {'response_code': response_code, 'response_message': response_message, 'response_data': response_data}
    queryUtils.create_log(json.dumps(response), status)
    return jsonify(response)


def create_hash(var):
    return hashlib.sha1(var.encode()).hexdigest()
