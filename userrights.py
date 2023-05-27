import time
from functools import wraps
from flask_login import current_user
from flask import abort


def admin_only(f):
    @wraps(f)
    def check_user_id(*arg, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*arg, **kwargs)
    return check_user_id
