from flask import Flask, render_template
from models import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/item/<code>')
def item(code):
	try:
		item = Item.get(Item.code == code)

		reviews = Review.select().where(Review.code == code)

		return render_template('item.html', name=item.name, reviews=reviews, image_url=item.image_url, price=item.price)
	except Exception:
		return "Does not exist"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
