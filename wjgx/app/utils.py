from functools import wraps

from flask import abort
from flask_login import current_user, login_required


def manager_required(f):
    @login_required
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.auth:
            abort(403)
        return f(*args, **kwargs)
    return wrapper


def hash_filename(filename):
    import uuid
    _, _, suffix = filename.rpartition('.')
    return '%s.%s' % (uuid.uuid4().hex, suffix)
