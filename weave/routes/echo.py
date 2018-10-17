# import logging

from flask import request, jsonify

from weave import application as app

# logger = logging.getLogger(__name__)

@app.route('/echo', methods=['POST'])
def evaluate():
    data = request.get_json()
    app.logger.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue * inputValue
    app.logger.info("My result :{}".format(result))
    return jsonify(result)

@app.route('/alarm')
def alarm():
    return jsonify(switch = 1)