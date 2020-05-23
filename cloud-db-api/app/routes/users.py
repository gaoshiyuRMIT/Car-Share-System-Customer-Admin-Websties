from . import request, url_for, Blueprint, g
from app.UserManager import UserManager
from . import jsonifyResponseData


bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/registerUser", methods=["POST"])
@jsonifyResponseData
def registerUser():
    usMgr = UserManager()
    newUserVal = request.json
    usrPK = usMgr.addOne(newUserVal)
    success = True if usrPK else False
    result = {"success":success}
    return result

@bp.route("/search", methods=["POST"])
@jsonifyResponseData
def findUser():
    usMgr = UserManager()
    username = request.json.get('username')
    result = usMgr.getOne(username)
    success = True if result is not None else False
    return {"success": success}

@bp.route("/login", methods=["POST"])
@jsonifyResponseData
def login():
    usMgr = UserManager()
    username, password = map(request.json.get, ("username", "password"))
    one = usMgr.getOne(username)
    result = {"success": False, "fname": ""}
    if one is not None and one["password"] == password:
        result["success"] = True
        result["fname"] = one.get("fName", "")
    return result
