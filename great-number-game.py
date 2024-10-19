from flask import Flask, render_template, request, redirect ,session
import random


app = Flask(__name__)
app.secret_key = 'Husam 1333'

  
acutal_number=random.randint(1, 100)

@app.route('/checknumber' ,methods=['POST'])
def checknumber():
    user_input=request.form.get("user_input")
    count=session.get("times",0)
    text=""
    print(acutal_number)
    print(user_input)
    w="200px"
    h="200px"
    boxcolor="green"
    
    if (int(acutal_number)>int(user_input)):
            boxcolor="aqua"
            text="Too low !"
            session['times']=count+1
    elif(int(acutal_number)<int(user_input)):
        boxcolor="red"
        text="Too High !"
        session['times']=count+1
    else:
        boxcolor="green"
        text="Great Job, Correct ! # is:"+str(acutal_number)
    return render_template("index.html",user_input=user_input,w=w,h=h,boxcolor=boxcolor,text=text,times=session['times'])


# ask about use many keys and seesions !

@app.route('/restcounter' ,methods=['POST'])
def restcounter():
    session.clear()
    return redirect("/")
  
@app.route('/')         
def index():
    return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True) 
