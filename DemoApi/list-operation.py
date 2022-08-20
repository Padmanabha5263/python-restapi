from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items =[]

class Item(Resource):
    def get(self,name):
        for itm in items:
            if(itm["name"]==name):
                return itm     
        return {"error":"no item found with this name"}, 404                    # error code specifiing is not an important its just for understanding

    def post(self,name):
        data =request.get_json()
        item ={
            "name":name,
            "price":data["price"]
        }
        items.append(item)
        return item, 201                


class ItemList(Resource):
    def get(self):
        return {"items":items}, 201

api.add_resource(Item, "/item/<string:name>")        #http://127.0.0.1:5000/student/padmanabha
api.add_resource(ItemList, "/items")
app.run(port=5000, debug=True)
