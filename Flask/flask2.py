from flask import Flask

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return 'Home Page'

# Multiple routes for the same function
@app.route('/about')
@app.route('/about-us')
def about():
    return 'About Us Page'

# Dynamic routes with parameters
@app.route('/user/<username>')
def user_profile(username):
    return f'User Profile: {username}'

# Routes with type converters
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# HTTP methods
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return 'Form submitted!'
    return 'Submit form'

if __name__ == '__main__':
    app.run(debug=True)
