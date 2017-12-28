from flask import Flask
from flask import request, abort, jsonify
from generate_password import generate

nums = '0123456789'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_chars = '!@#$%^&*()=+/?\|[]{}`~;:,<.>'

default_charsets =[nums, lower_letters, upper_letters, special_chars]

app = Flask(__name__)


@app.route('/pwd_gen_server/api/v1.0/generate_password', methods=['GET'])
def generate_password():
    site = request.args.get('site')
    month_key = request.args.get('month_key')
    extra_secret = request.args.get('extra_secret')
    length = request.args.get('length')
    if not all([site, month_key, extra_secret, length]):
        abort(400)

    #TODO: get charsets
    charsets = None

    pwd = generate(site, month_key, extra_secret, int(length), charsets or default_charsets)
    return jsonify({'password': pwd})


if __name__ == '__main__':
    app.run()
