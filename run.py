from settings import USER, DATABASE
from api import create_app

app = create_app(user=USER, database=DATABASE)

app.run(debug=True)
