from api import create_app
from settings import DATABASE

#print(DATABASE)

app = create_app(DATABASE)

app.run(debug=True)