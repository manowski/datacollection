from models import app
from routes import users, update


app.add_url_rule('/users', view_func=users.handle_users, methods=['GET'])
app.add_url_rule('/users/<user_name>', view_func=users.handle_user, methods=['GET'])
app.add_url_rule('/top/country/<country_alias>', view_func=users.handle_top_country, methods=['GET'])

app.add_url_rule('/update_stats', view_func=update.update_stats, methods=['GET'])
app.add_url_rule('/database', view_func=update.handle_db, methods=['GET'])
