from flask import render_template, jsonify, redirect, url_for, request, render_template
import app
from app import db, app
from models import transfer

from forms import auth_form
from flask_login import login_user, login_required, logout_user, LoginManager

# ==============================#
# Make sure we are logged in before hitting the endpoints
# ==============================#
login_manager = LoginManager()
login_manager.init_app(app)


# ------------------------------#
# Create a login and signup view
# ------------------------------#

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = auth_form.SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if transfer.User.query.filter_by(email=form.email.data).first():
                return "Email address already exists"
            else:
                newuser = transfer.User(form.email.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()

                return "User created!!!"
        else:
            return "Form didn't validate"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = auth_form.SignupForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user = transfer.User.query.filter_by(email=form.email.data).first()
            if user:
                if user.password == form.password.data:
                    login_user(user)
                    return "User logged in"
                else:
                    return "Wrong password"
            else:
                return "user doesn't exist"
    else:
        return "form not validated"


@login_manager.user_loader
def load_user(email):
    return transfer.User.query.filter_by(email=email).first()


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"


@app.route('/')
@login_required
def hello_world():
    app.logger.debug('Rendering home page')
    return render_template('index.html')


@app.route('/sentinel/<sentinel_num>/table/get_published_after/<date>')
@login_required
def render_nci_table(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_nci_url_published_after
    quicklook_list = []

    return_list = get_nci_url_published_after(sentinel_num, date)

    for item in return_list:
        quicklook_list.append(item.replace('.zip', '.png'))

    return render_template('table.html', table=return_list, quicklook=quicklook_list)


@app.route('/table')
@login_required
def render_table():
    """

    :return:
    """
    return_list = []
    s = transfer.Schedule.query.all()

    for item in s:
        return_list.append([item.id,
                            item.date_time,
                            item.pi,
                            item.last_published_date,
                            item.transfer_success])

    return render_template('schedule_table.html', table=return_list)


@app.route('/get_test_nci')
@login_required
def get_test_nci():
    from api.nci.get_results_from_sara import get_by_date

    result = get_by_date('2017-10-29', '2017-11-01', 2)

    return jsonify(result)


@app.route('/get_published_after_test')
@login_required
def get_published_after_test():
    from api.nci.get_results_from_sara import get_published_after

    result = get_published_after('2017-10-31', 2)

    return jsonify(result)


@app.route('/sentinel/<sentinel_num>/get_published_after/<date>')
@login_required
def get_published_after(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_published_after

    result = get_published_after(sentinel_num, date)

    return jsonify(result)


@app.route('/map')
@login_required
def return_map():
    return render_template("map.html")


@app.route('/sentinel/<sentinel_num>/get_nci_url_published_after/<date>')
@login_required
def get_nci_url_published_after(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_nci_url_published_after

    result = get_nci_url_published_after(sentinel_num, date)

    return jsonify(result)


@app.route('/get_last')
@login_required
def get_last():
    """
    For testing
    :return:
    """
    from api.db.scheduler import get_last_sync

    result = get_last_sync()

    # rint(result)
    return result


@app.route('/sentinel/<sentinel_num>/sync_nci_to_pawsey', methods=['GET', 'POST'])
@login_required
def sync_nci_to_pawsey(sentinel_num):
    """

    :param sentinel_num:
    :return:
    """

    from api.db.scheduler import sync_nci_to_pawsey
    result = sync_nci_to_pawsey(sentinel_num)

    print(url_for('render_table'))

    return redirect(url_for('render_table'))
