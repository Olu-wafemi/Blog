from flask import Flask, render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '85ca0127fc38f63e8b2e077ab9213ecdf960c97c4506151948982696d16aea05'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)
class  BlogPost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content =db.Column(db.Text,nullable=False)
    author = db.Column(db.String(20),nullable=False,default='N/A')
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    
    def __repr__(self):
        return 'Blog post '+ str(self.id)




all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author':'Femi'
    },
      {
        'title': 'Post 2',
        'content': 'This is the content of post 2'
    }

]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/posts',methods=['GET','POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content  = request.form['content']
        author = request.form['author']
        new_post=  BlogPost(title=post_title,content=post_content,author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.title).all()

        return render_template('posts.html',posts =all_posts)
@app.route('/home')
def hello():
    return 'Hello World'


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')
@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
       
        post.title = request.form['title']
        post.author = request.form['author']
        post.content= request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html',post=post)
@app.route('/posts/new',methods=['GET','POST'])
def new_post():
    if request.method == 'POST':
        post.title = request.form['title']
        post.content  = request.form['content']
        post.author = request.form['author']
        new_post=  BlogPost(title=post_title,content=post_content,author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html')


@app.route('/login' )
def login():
    form = LoginForm()
    return render_template('login.html',form=form)
      

if __name__ == 'main':
    app.run(debug=True)