from . import api
from flask import request, abort, jsonify

from helpers.generate_password import generate

@api.route('/generate_password', methods=['GET'])
def generate_password():
    site = request.args.get('site')
    month_key = request.args.get('month_key')
    extra_secret = request.args.get('extra_secret')
    length = request.args.get('length')
    # cs: character set
    cs_num = request.args.get('num')
    cs_lower = request.args.get('lower')
    cs_upper = request.args.get('upper')
    cs_special = request.args.get('special')
    if not all([site, month_key, extra_secret, length, cs_num, cs_lower, cs_upper, cs_special]):
        abort(400)

    charsets = dict(zip(range(4), [int(cs) for cs in [cs_num, cs_lower, cs_upper, cs_special]] ))

    try:
        pwd = generate(site, month_key, extra_secret, int(length), charsets)
        return jsonify({'password': pwd})
    except ValueError as e:
        abort(400, e)
