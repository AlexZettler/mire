from flask import render_template

from app import app

# @app.route('/')
# def index():
# 	return render_template('index.html')

# @app.route('/about')
# def about():
# 	return render_template('about.html')

# Just serve the game at the index
@app.route('/')
def game():
	return render_template('game.html')

# @app.route('/chat')
# def chat():
# 	return render_template('chat.html')