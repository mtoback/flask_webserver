from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__, static_folder='templates', static_url_path='/')

# Use the route() decorator to bind a function to a URL.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello'


'''You can add variable sections to a URL by marking sections with <variable_name>. 
   Your function then receives the <variable_name> as a keyword argument. Optionally, 
   you can use a converter to specify the type of the argument like <converter:variable_name>.
'''
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

'''The following two rules differ in their use of a trailing slash.
   The canonical URL for the projects endpoint has a trailing slash. 
   It’s similar to a folder in a file system. 
   If you access the URL without a trailing slash, 
   Flask redirects you to the canonical URL with the trailing slash.

   The canonical URL for the about endpoint does not have a trailing slash. 
   It’s similar to the pathname of a file. Accessing the URL with a trailing slash 
   produces a 404 “Not Found” error. This helps keep URLs unique for these resources, 
   which helps search engines avoid indexing the same page twice.
'''
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
