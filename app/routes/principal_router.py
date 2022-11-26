from flask import Blueprint,render_template

principal_bp = Blueprint('index_bp', __name__)


@principal_bp.route("/")
def index():
    return render_template("index.html")

@principal_bp.route("/home")
def home():
    return render_template("home.html")