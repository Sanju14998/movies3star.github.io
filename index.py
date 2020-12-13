from flask import *
import datetime
import time
app = Flask(__name__)



@app.route('/')
def home():
     while True:
    

        a= datetime.datetime.now()
        date = a.date()
        time = a.time()
        # time.sleep(1)
        return render_template('movie.html',date=date,time=time)


@app.route('/login' ,methods=['POST','GET'])
def login():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        againPassword = request.form['password']

    return render_template('success.html',email=email)

                                      # ''' HOLLYWOOD  MOVIES PAGES LIST'''
                                        

@app.route('/hollywood1')
def hollywood1():
    return render_template('Hollywood_page_1.html')


@app.route('/hollywood2')
def hollywood2():
    return render_template('Hollywood_page_2.html')

@app.route('/hollywood3')
def hollywood3():
    return render_template('Hollywood_page_3.html')


@app.route('/hollywood4')
def hollywood4():
    return render_template('Hollywood_page_4.html')


@app.route('/hollywood5')
def hollywood5():
    return render_template('Hollywood_page_5.html')












                                # ''' HOLYWOOD MOVIES INFORMATION  ABOUT EACH MOVIES
                                # eg ki SCREEN SHOT AND DOWNLOAD SECTIONMI  THIS HTML FILE'''
                                
                                

@app.route('/movie1')
def movies1():
    return render_template('hollywood_movies_info_1.html')













# >>>>>>>>>>>>>>>>>>>>>> EVERY MOVIES WATCGH TRAILOR >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>






























@app.errorhandler(404)
def error(e):
    return render_template('error.html')
if __name__=="__main__":
    app.run(debug=True)