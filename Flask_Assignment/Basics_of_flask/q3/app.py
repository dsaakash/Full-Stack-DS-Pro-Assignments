from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # Display the user profile for a given username
    return f'User profile for {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Display a specific post based on the post ID
    return f'Post with ID {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
