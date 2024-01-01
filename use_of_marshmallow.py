from flask import Flask,jsonify,request
from marshmallow import Schema , fields


app=Flask(__name__)
class BookSchema(Schema):
    title=fields.Str(required=True)
    author=fields.Str(required=True)



books=[{"id":1,"title":"Rex Rhegum","author":"Haroon Rasheed"},
       {"id":2,"title":"A love found in shadow","author":"Arwa Soltan"}

    ]
@app.route("/books",methods=['GET'])
def get_books():
        result=BookSchema().dump(books,many=True)
        return jsonify(result),200
@app.route("/books/<int:id>",methods=["GET"])
def get_books1(id):
     book=None
     for i in books:
          if id==i["id"]:
               book=i
     if book!=None:
          result=BookSchema().dump(book)
          return jsonify(result),200 
     return jsonify({"message":"out of range"}),404         
@app.route("/add",methods=["POST"])
def add():
     data=request.get_json()
     newbook=BookSchema().load(data)
     newbook["id"]=len(books)+1
     books.append(newbook)
     print("this is books",books)
     return jsonify({"message":"book is successfully inserted"}),200        

if __name__=="__main__":
    app.run(debug=True)
