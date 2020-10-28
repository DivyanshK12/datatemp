from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pickle

ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Randomness1234567898763535' 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect('/upload')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file found')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            data = []
            with open('picklefile','wb') as picklefile:
                for line in file:
                    subdata = line.decode('utf-8').strip().split(',')
                    data.append(subdata)
                pickle.dump(data,picklefile)
            #return redirect('/app1')
            return redirect('/preview')
    return render_template('try4.html')

@app.route('/preview')
def show_csv():
    data = []
    with open('picklefile','rb') as pf:
        data = pickle.load(pf)
    return render_template('display.html',data=data)

if __name__ == "__main__":
    app.run(debug = True)