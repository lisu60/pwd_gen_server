from . import api
from flask import request, abort, jsonify, render_template
from flask_login import login_user, logout_user

from pwd_gen.helpers.generate_password import generate
from .forms import SeedDetailsForm, EmailPasswordForm


@api.route('/generate_password', methods=['POST'])
def generate_password():
    form = SeedDetailsForm(csrf_enabled=False)
    if form.validate_on_submit():
        site = form.site.data
        month_key = form.month_key.data
        extra_secret = form.extra_secret.data
        length_min = form.length_min.data
        length_max = form.length_max.data
        # cs: character set
        cs_num = form.num.data
        cs_lower = form.lower.data
        cs_upper = form.upper.data
        cs_special = form.special.data

        len_required = cs_num + cs_lower + cs_upper + cs_special
        if len_required > (length_min if length_min else length_max):
            abort(400, 'Not enough length for char-set specifications')

        length = range(length_min, length_max + 1) if length_max else length_min

        charsets = dict(zip(range(4), [int(cs) for cs in [cs_num, cs_lower, cs_upper, cs_special]] ))

        try:
            pwd = generate(site, month_key, extra_secret, length, charsets)
            return jsonify({'password': pwd})
        except ValueError as e:
            abort(400, e)

    else:
        errmsg = ''
        for field, msg in form.errors.items():
            for err in msg:
                print("%s: %s" % (field, err))
                errmsg += "%s: %s" % (field, err) + '\n'
        abort(400, errmsg)

@api.route('/signin', methods=['POST'])
def signin():
    from pwd_gen.models.User import User
    form = EmailPasswordForm(csrf_enabled=False)

    if form.validate_on_submit():
        for u in User.query:
            print("%s, %s", (u.email, u.password))
        user = User.query.filter_by(email=form.email.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)

            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failure'})
    return jsonify({'status': 'error'})

@api.route('/signout')
def signout():
    logout_user()
    return jsonify(dict(status='success'))
