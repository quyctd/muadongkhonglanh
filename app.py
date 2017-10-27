from flask import Flask, render_template, request, g, redirect, url_for
import mlab
from mongoengine import *
from faker import Faker
import random

app = Flask(__name__)

mlab.connect()


class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    g_id = IntField()

f = Faker()
# for _ in range(10):
#     g = Girl(name  = f.name(),
#             image = 'https://source.unsplash.com/500x300/?girl',
#             description = f.text(),
#             g_id= random.randint(1000,9999))
#
#     g.save()


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/admin')
def admin():

    girl_list = Girl.objects()
    return render_template('admin.html', girls= girl_list)

@app.route('/add-girl' , methods=['GET', 'POST'])
def addgirl():
    if request.method == "GET":
        return render_template('add_girl.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        image = form['image']
        description = form['description']

        girl = Girl(name = name, description = description, image =image, g_id = random.randint(1000,9999))
        girl.save()

        girllist_after = Girl.objects()
        return render_template("admin.html", girls = girllist_after)




    #Start Here
@app.route('/delete/<int:id>', methods=['POST'])
def remove(id):
    Girl.objects(g_id = id).delete()
    girllist_after_delete = Girl.objects()
    return render_template("admin.html", girls = girllist_after_delete)


@app.route('/delete-girl/<girl_id>')
def delete_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if girl is None:
        print("not found")
    else:
        girl.delete()
    return "Delete "+girl_id

@app.route('/update-girl/<girl_id>', methods=['GET', 'POST'])
def update(girl_id):
    if request.method == "GET":
        girl = Girl.objects().with_id(girl_id)

        return render_template('update_girl.html', girl = girl)
    elif request.method == "POST":
        girl = Girl.objects().with_id(girl_id)
        form = request.form
        girl.name = form['name']
        girl.image = form['image']
        girl.description = form['description']


        girl.save()
        #Cách khác
        #name = form['name']
        #image = form['image']
        #description = form['description']
        #girl.update(set__name = name, set__image = image, set__description == description)

        return redirect(url_for('admin'))

# @app.route('/girl')
# def index_girl():
#     girl_list = Girl.objects()
#     return render_template('girls.html',girls = girl_list)
#
# @app.route('/list')
# def list_demo():
#     n_list = ['Huy', 'Tuấn Anh', 'Linh', "Trường", 'Quân', "Blablo"]
#     return render_template("girls_list.html", names = n_list)
#
# @app.route('/dict')
# def dict():
#     d = {
#         'name': 'Sinh viên năm nhất',
#         'image' :'http://www.tieuthien.com/wp-content/uploads/2016/10/hot-girl-gai-xinh-facebook-tieuthien.com-5.jpg'
#     }
#     return render_template('girl_dict.html', girl = d)



if __name__ == '__main__':
  app.run(debug=True)
