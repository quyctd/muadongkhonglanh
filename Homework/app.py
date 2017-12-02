from flask import Flask, render_template
import mlab
from mongoengine import *
from faker import Faker
app = Flask(__name__)

mlab.connect()

class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    rating = FloatField()

# f = Faker()
# for _ in range(20):
#     g = Girl(name  = f.name(),
#             image = 'https://source.unsplash.com/500x300/?girl',
#             description = f.text(),
#             rating = 4.1)
#
#     g.save()
@app.route('/')
def index():
    return render_template('homepage.html')
@app.route('/girl')
def index_girl():
    girl_list = Girl.objects()
    return render_template('girls.html',girls = girl_list)

@app.route('/list')
def list_demo():
    n_list = ['Huy', 'Tuấn Anh', 'Linh', "Trường", 'Quân', "Blablo"]
    return render_template("girls_list.html", names = n_list)

@app.route('/dict')
def dict():
    d = {
        'name': 'Sinh viên năm nhất',
        'image' :'http://www.tieuthien.com/wp-content/uploads/2016/10/hot-girl-gai-xinh-facebook-tieuthien.com-5.jpg'
    }
    return render_template('girl_dict.html', girl = d)

@app.route('/css-demo')
def css_demo():
    return render_template('css_demo.html')

if __name__ == '__main__':
  app.run(debug=True)
