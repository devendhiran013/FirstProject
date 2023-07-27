from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("registration.html") 
@app.route("/Register",methods=["POST","GET"])
def Register():
    if request.method=="POST":
        name=request.form.get('name')
        age=request.form.get('age')
        Address=request.form.get('Address')
        Contact=request.form.get('Contact')
        Mail=request.form.get('Mail')
        return render_template("result.html",name=name,age=age,Address=Address,Contact=Contact,Mail=Mail)
    
if __name__=='__main__':
    app.run(debug=True)