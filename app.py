from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def hello():

    return render_template("index.html")

@app.route("/",methods=['POST'])
def add():
    name1="SandeepPrasad123"
    val=request.form["age"]
    print(type(val))

    import pickle
    model=pickle.load(open("model.pkl","rb"))
    import numpy as np
    val=np.array(int(val))
    print("Intial dimension=",val.ndim)
    val=val.reshape(-1,1)
    print("Updated dimenssion",val.ndim)
    value=model.predict(val)
    print(value)

    return render_template("about.html",name22=value)


app.run(debug=True)
