from flask import Flask,jsonify 





app=Flask(__name__)

@app.route("/")
def helloworld():
    return "<p>hello world<p>"

@app.route("/checkeven/<int:num>")
def Checkeven(num):
    if num%2==0:
        result={"number":num,"Even":True}
    else:
        result={"number":num,"Odd":True}    
    return jsonify(result)


if __name__=="__main__":
  app.run(debug=True)