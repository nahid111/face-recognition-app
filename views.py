from app import app, db
from flask import render_template, request, redirect, url_for, send_file, session, g
from io import BytesIO
from models import Students, User
import face_recognition as fr
import numpy as np


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/compareProcess', methods=['POST','GET'])
def compareProcess():
    if request.method == 'POST':
        unknownImage = request.files['unknownImage']
        unknownImageLoad = fr.load_image_file(unknownImage)
        unknownImageEncoding = fr.face_encodings(unknownImageLoad)
        unknownImageEncodingLen = len(unknownImageEncoding)

        rows = Students.query.all()
        objList = []

        for row in rows:
            imageEncoding = np.loads(row.imageEncodings)
            for n in range(0, unknownImageEncodingLen):
                result = fr.compare_faces([imageEncoding], unknownImageEncoding[n])
                if result[0] == True:
                    obj = Students.query.get(row.sl)
                    objList.append(obj)

        #submittedImage = send_file(unknownImage, attachment_filename=unknownImage.filename, as_attachment=True)
        return render_template('index.html', rows=objList)
    else:
        return render_template('index.html')






#######################################     Admin Views    ###############################

#   Login page
@app.route('/admin/', methods=['GET','POST'])
def admin():
    msg = ''
    if request.method == 'POST':
        session.pop('user', None)
        u = request.form['username']
        p = request.form['password']
        user_temp = User.query.filter_by(user=u).first()
        if user_temp is None:
            msg = "User not found.!"
        else:
            if user_temp.password == p:
                session['user'] = request.form['username']
                return redirect(url_for('home'))
            else:
                msg = "Password is incorrect.!"

    return render_template('admin/index.html', msg=msg)



@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    #return redirect(url_for('admin', msg="You have Logged Out Successfully"))
    return render_template('admin/index.html', msg="You have Logged Out Successfully")

#   Home page
@app.route('/admin/home')
def home():
    if g.user:
        return render_template('admin/home.html')
    return render_template('admin/index.html', msg="Login to Continue")

#   READ / SHOW
@app.route('/admin/all')
def viewAll():
    if g.user:
        rows = Students.query.all()
        return render_template('admin/viewAll.html', rows=rows)
    return redirect(url_for('admin', msg="Login to Continue"))

#   function for displaying images
@app.route('/image/<sl>')
def image(sl):
    imageFile = Students.query.get(sl)
    return send_file(BytesIO(imageFile.imageData), attachment_filename=imageFile.imageName, as_attachment=True)

#   CREATE / INSERT
@app.route('/admin/insert')
def insert():
    if g.user:
        return render_template('admin/insertform.html')
    return redirect(url_for('admin', msg="Login to Continue"))


@app.route('/admin/insertionProcess', methods=['POST'])
def insertionProcess():

    id = request.form['id']
    name = request.form['name']
    file = request.files['pic']
    imageName = file.filename
    # converting the image file into binary data
    imageData = file.read()
    # converting the binary data to image
    imageEncodings = fr.load_image_file(BytesIO(imageData))
    imageEncodings = fr.face_encodings(imageEncodings)[0]
    # np array to pickled binary
    imageEncodingsBin = imageEncodings.dumps()

    row = Students(id=id, name=name, imageName=imageName, imageData=imageData, imageEncodings=imageEncodingsBin)
    db.session.add(row)
    db.session.commit()

    return redirect(url_for('viewAll'))

#   DELETE
@app.route('/admin/delete/<sl>')
def delete(sl):
    x = Students.query.get(sl)
    db.session.delete(x)
    db.session.commit()
    return redirect(url_for('viewAll'))


#  EDIT / UPDATE
@app.route('/admin/update/<sl>')
def update(sl):
    if g.user:
        row = Students.query.get(sl)
        return render_template('admin/updateform.html', row=row)
    return redirect(url_for('admin', msg="Login to Continue"))


@app.route('/admin/updateProcess', methods=['POST'])
def updateProcess():

    sl = request.form['sl']

    id = request.form['id']
    name = request.form['name']
    file = request.files['pic']
    imageName = file.filename
    # converting the image file into binary data
    imageData = file.read()
    # converting the binary data to image
    imageEncodings = fr.load_image_file(BytesIO(imageData))
    imageEncodings = fr.face_encodings(imageEncodings)[0]
    # np array to pickled binary
    imageEncodingsBin = imageEncodings.dumps()

    row = Students.query.get(sl)
    row.id = id
    row.name = name
    row.imageName = imageName
    row.imageData = imageData
    row.imageEncodings = imageEncodingsBin
    db.session.commit()

    return redirect(url_for('viewAll'))






