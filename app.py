from App import create_app
from App.route import site

app = create_app()
app.register_blueprint(site)
