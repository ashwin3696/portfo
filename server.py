from flask import Flask, render_template,url_for,request,redirect
import csv
app=Flask(__name__)
print(__name__)

#Reads the url and prints the same in page along with no. eg http://127.0.0.1:5000/anushree/3
#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None,post_id=None):
    #return render_template('index.html',name=username,post_id=post_id)

@app.route('/')
def my_home():
    return render_template('index.html')

#To work dynamically the HTML page
@app.route('/<string:page_name>')
def html_about(page_name):
    return render_template(page_name)

#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/works.html')
#def works():
#    return render_template('works.html')

#@app.route('/contact.html')
#def contact():
#    return render_template('contact.html')

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')
'''
def write_to_csv(data):
    with open('database.csv', newline='',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
'''

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong,try again'
'''
#for running the website
1.set Flask_APP=server.py
2.flask run

#to activate debug
set Flask_ENV=development
'''