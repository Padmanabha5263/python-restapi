from flask import Flask, jsonify, request

app = Flask(__name__)

#manually defining stores to save and retrive operation
stores = [
    {
        'name':"Gopi-Condiments",
        'items':[
            {
                'name':'Candy',
                'price':150
            }
        ]
    },
    {
        'name':"Vinod-Condiments",
        'items':[
            {
                'name':'Candy',
                'price':200
            }
        ]
    }
]

#to save the new store detailes into the stores list
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    newStore = {
        "name" :data["name"],
        "items" :[]
    }
    stores.append(data)
    return jsonify(stores)

#to get the list of stores object
@app.route('/stores', methods=['GET', 'POST'])                #  methods=['GET', 'POST']: it accept either get or  post method from user
def get_stores():
    return jsonify({"stores":stores})

#to get the the perticular store using name
@app.route('/store/<string:name>', methods=['GET', 'POST'])                #it accept either get or  post method from user
def get_store_by_name(name):
    for store in stores:
        if(name==store["name"]):
            return jsonify(store)
    return jsonify({"message":"NO match found"})
            

app.run(port=5000)