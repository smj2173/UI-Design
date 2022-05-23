from inspect import isdatadescriptor
from flask import Flask
from flask import render_template, url_for, redirect
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 11

data = {
    "1":{
        "id" : "1",
        "flavor" : "pumpkin cheesecake",
        "description" : "Nothing makes us happier than this Pumpkin Cheesecake Ice Cream. Lightly spiced with cinnamon and nutmeg, with honey graham cracker crust. It’s like if fall and autumn had a baby and that baby grew up to be a real champ",
        "price" : "12.00",
        "ingredients": "cream, milk, cane sugar, pumpkin puree, egg yolks, cream cheese (milk, cream, cheese culture, salt, carob bean gum), butter, enriched wheat flour (unbleached wheat, malted barley, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid), whole wheat flour, brown sugar, salt, honey, cinnamon, nutmeg, baking soda, ginger",
        "features" : ["limited edition", "organic"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2021/10/PUMPKIN-CHEESECAKE_OVERSCOOPED.jpeg",
        "rating": "4",
        "calories":"330",
        "stores":["Westside Market", "Morton Williams", "Hmart"],
    },
    "2":{
        "id" : "2",
        "flavor" : "chocolate fudge brownie",
        "description" : "Nothing makes us happier than this Chocolate Fudge Brownie Ice Cream. Now, are rich chocolate fudge and chewy chocolate brownies good for you? Probably not. But on the other hand, are rich chocolate fudge and chewy chocolate brownies good for you? Probably. That’s just science.",
        "price":"12.00",
        "ingredients": "milk, cream, cane sugar, eggs, cocoa liquor, cocoa powder, filtered water, tapioca syrup, canola oil, wheat flour, malted barley flour, salt, vanilla extract (grain alcohol, vanilla bean), baking powder (sodium acid, pyrophosphate, baking soda, corn starch, monocalcium phosphate), corn starch",
        "features" : [],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/CHOCOLATE-FUDGE-BROWNIE_OVERSCOOPED-1.jpg",
        "rating":"3",
        "calories":"330",
        "stores":["Westside Market"],
    },
    "3":{ 
        "id" : "3",
        "flavor" : "honeycomb",
        "description" : "Nothing makes us happier than this Honeycomb Ice Cream. Despite being called honeycomb, it’s not made from any honey at all. It’s made with caramel candy. That all might seem confusing until you realize that ice cream is also made without ice. Your whole life has been a lie.",
        "price" : "12.00",
        "ingredients": "milk, cream, cane sugar, egg yolks, organic brown rice syrup or tapioca syrup, coconut oil, brown sugar, vanilla extract (grain alcohol, vanilla bean), baking soda, salt",
        "features" : [],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/HONEYCOMB_OVERSCOOPED.jpeg",
        "rating":"4",
        "calories":"320",
        "stores":["Hmart"],
    },
    "4":{   
        "id" : "4",
        "flavor" : "marionberry cheesecake",
        "description" : "Nothing makes us happier than this Marionberry Cheesecake Ice Cream. If you’re going to go all the way to the freezer for this, the least we could do is make our graham crumble in-house and go to Stahlbush Island Farms for the marionberries that we use to make the jam.",
        "price" : "12.00",
        "ingredients": "milk, cream, cane sugar, egg yolks, cream cheese (milk, cream, cheese culture, salt, carob), marionberries, butter, enriched wheat flour (unbleached wheat, malted barley, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid), whole wheat flour, tapioca syrup, brown sugar, salt, honey, cinnamon, nutmeg, ginger, tapioca starch, baking soda, pectin, citric acid",
        "features" : ["organic"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2021/02/MARIONBERRY-CHEESECAKE_OVERSCOOPED-1.jpg",
        "rating":"5",
        "calories":"340",
        "stores":["Morton Williams", "Hmart"],
    },
    "5":{
        "id" : "5",
        "flavor" : "earl grey tea",
        "description" : "Nothing makes us happier than this Earl Grey Tea Ice Cream. Hand-harvested Rishi Tea leaves from the tea tree forests in the Yunnan province of China, a little bergamot citrus, your mouth. Teamwork!",
        "price" : "12.00",
        "ingredients": "cream, milk, cane sugar, egg yolks, earl grey tea (organic black tea leaves, organic bergamot oil), salt",
        "features" : ["limited edition"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/EARL-GREY_OVERSCOOPED-1.jpg",
        "rating":"2",
        "calories":"230",
        "stores":[],
    },
    "6":{
        "id" : "6",
        "flavor" : "pumpkin cinnamon roll",
        "description" : "Nothing makes us happier than this Vegan Pumpkin Cinnamon Roll Ice Cream. Pureed pumpkin. Vegan cinnamon rolls. A little nutmeg. Swirls of cinnamon caramel. Maybe that autumn chill in the air is coming from the freezer?",
        "price" : "12.00",
        "ingredients": "oat milk (filtered water, gluten-free oats), cane sugar, coconut cream, pumpkin puree, cocoa butter, organic virgin coconut oil, enriched wheat flour (unbleached wheat, malted barley, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid), apples, brown sugar, vanilla extract (grain alcohol, vanilla bean), canola oil, salt, ginger, cinnamon, carob bean gum, lemon juice, cream of tartar, baking soda, tapioca starch, nutmeg, allspice, cloves",
        "features" : ["limited edition", "vegan", "organic"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2021/10/VEGAN-PUMPKIN-CINNAMON-ROLL_OVERSCOOPED.jpeg",
        "rating":"5",
        "calories":"410",
        "stores":["Westside Market", "Morton Williams"],
    },
    "7":{
        "id" : "7",
        "flavor" : "strawberry",
        "description" : "Nothing makes us happier than this Vegan Strawberry Ice Cream. Oregon-grown strawberries. Delicately picked at peak ripeness. Then shoved into a dark alley where oats get to work initiating strawberries into the ice cream gang.",
        "price" : "12.00",
        "ingredients": "oat milk (filtered water, gluten-free oats), cane sugar, strawberries, coconut cream, cocoa butter, organic virgin coconut oil, carob bean gum, salt",
        "features" : ["vegan", "organic"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/OAT-STRAWBERRY_OVERSCOOPED-1.jpg",
        "rating":"3",
        "calories":"380",
        "stores":["Westside Market", "Hmart", "Morton Williams"],
    },
    "8":{
        "id" : "8",
        "flavor" : "cookie crumble strawberry jam",
        "description" : "Nothing makes us happier than this Vegan Cookie Crumble Strawberry Jam Ice Cream. With cold-ground Tahitian vanilla, jam from Oregon-grown strawberries, and crumbles of gluten-free oat cookies, eating vegan isn’t just better for the planet, it’s better for the mouth.",
        "price" : "12.00",
        "ingredients": "cashew milk (filtered water, raw cashews), cane sugar, coconut cream, organic virgin coconut oil, cocoa butter, strawberries, gluten-free oats, buckwheat flour, vanilla extract (grain alcohol, vanilla bean), tapioca syrup, brown sugar, rice flour, salt, canola oil, carob bean gum, tapioca starch, baking soda, pectin",
        "features" : ["vegan"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/COOKIE-CRUMBLE-STRAWBERRY-JAM_OVERSCOOPED-1.jpg",
        "rating":"5",
        "calories":"360",
        "stores":["Westside Market"],
    },
    "9":{
        "id" : "9",
        "flavor" : "cookies and cream caramel swirl",
        "description" : "Nothing makes us happier than this Vegan Cookies & Cream Caramel Swirl Ice Cream. Cream-filled dark chocolate cookies, folded into our creamy vegan base. A touch of cold-ground Tahitian vanilla. And a swirl of housemade caramel. It’s as if everything good in the world moved in to a pint-sized condo.",
        "price" : "12.00",
        "ingredients": "cashew milk (filtered water, raw cashews), cane sugar, coconut cream, virgin coconut oil, cocoa butter, wheat flour, cocoa powder, sunflower oil, vanilla extract (grain alcohol, vanilla bean), baking soda, sunflower lecithin, salt, carob bean gum",
        "features" : ["vegan", "organic"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/COOKIES-_-CREAM-CARAMEL-SWIRL_OVERSCOOPED-1.jpg",
        "rating":"4",
        "calories":"400",
        "stores":["Morton Williams", "Hmart"],
    },
    "10":{
        "id" : "10",
        "flavor" : "sicilian pistachio",
        "description" : "Nothing makes us happier than this Vegan Sicilian Pistachio Ice Cream. Certified by the International Slow Food Institute, these special pistachios are only found on Mount Etna. In Bronte, Italy, to be precise. So they’re renowned for their fragrance and flavor. And their neck scarves.",
        "price" : "12.00",
        "ingredients": "cashew milk (filtered water, raw cashews), cane sugar, coconut cream, virgin coconut oil, sicilian pistachios, cocoa butter, salt, carob bean gum",
        "features" : ["vegan"],
        "photo": "https://vanleeuwenicecream.com/wp-content/uploads/2020/03/PISTACHIO_OVERSCOOPED-1.jpg",
        "rating":"3",
        "calories":"320",
        "stores":[],
    }  
}

options_flavor = [val["flavor"] for key, val in data.items() if "flavor" in val]
flavor_id = [val["id"] for key, val in data.items() if "id" in val]
flavor_dict = dict(zip(flavor_id, options_flavor))

options_vegan = [val["flavor"] for key, val in data.items() if "vegan" in val["features"]]
vegan_id = [val["id"] for key, val in data.items() if "vegan" in val["features"]]
vegan_dict = dict(zip(vegan_id, options_vegan))


options_organic = [val["flavor"] for key, val in data.items() if "organic" in val["features"]]
organic_id = [val["id"] for key, val in data.items() if "organic" in val["features"]]
organic_dict = dict(zip(organic_id, options_organic))

options_limited = [val["flavor"] for key, val in data.items() if "limited edition" in val["features"]]
limited_id = [val["id"] for key, val in data.items() if "limited edition" in val["features"]]
limited_dict = dict(zip(limited_id, options_limited))


options_mw = [val["flavor"] for key, val in data.items() if "Morton Williams" in val["stores"]]
mw_id = [val["id"] for key, val in data.items() if "Morton Williams" in val["stores"]]
mw_dict = dict(zip(mw_id, options_mw))


options_ws = [val["flavor"] for key, val in data.items() if "Westside Market" in val["stores"]]
ws_id = [val["id"] for key, val in data.items() if "Westside Market" in val["stores"]]
ws_dict = dict(zip(ws_id, options_ws))


options_hmart = [val["flavor"] for key, val in data.items() if "Hmart" in val["stores"]]
hmart_id = [val["id"] for key, val in data.items() if "Hmart" in val["stores"]]
hmart_dict = dict(zip(hmart_id, options_hmart))





# ROUTES

@app.route('/')
def welcome():
    global data
    return render_template('welcome.html', data = data) 


@app.route('/search', methods=['GET', 'POST'])
def search():
    global data 
    global options_flavor
    if request.method == "POST":
        search_string = request.form.get("search")
    search_string = search_string.lower()
    if search_string in "vegan" or search_string in "organic" or search_string in "limited edition" or search_string in "westside market" or search_string in "hmart" or search_string in "morton williams":
        return redirect(url_for('results', search_string=search_string))
    matching = [s for s in options_flavor if search_string in s] #title
    if len(matching) > 1:
        return redirect(url_for('results', search_string=search_string))
    elif len(matching) == 1:
        page = ""
        for key, value in data.items():
            #each dictionary
            for i in value:
                if i == "flavor" and value[i] == matching[0]:
                    page = value["id"]
        return redirect(url_for('display_page', page=page))
    else:
        return redirect(url_for('results', search_string=search_string))


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit/<id>')
def edit(id):
    global data
    return render_template('edit.html', id=id, data=data)


@app.route('/search_results/<search_string>')
def results(search_string):
    global data
    global limited_dict
    global organic_dict
    global vegan_dict
    global ws_dict
    global mw_dict
    global hmart_dict

    matching = [s for s in options_flavor if search_string in s]
    #get options for each search object
    if search_string in "limited edition":
        return render_template('search_results.html', data = data, result=limited_dict, search_string=search_string)
    elif search_string in "organic":
        return render_template('search_results.html', data = data, result=organic_dict, search_string=search_string)
    elif search_string in "vegan":
        return render_template('search_results.html', data = data, result=vegan_dict, search_string=search_string)
    elif search_string in "morton williams":
        return render_template('search_results.html', data = data, result=mw_dict, search_string=search_string)
    elif search_string in "westside market":
        return render_template('search_results.html', data = data, result=ws_dict, search_string=search_string)
    elif search_string in "hmart":
        return render_template('search_results.html', data = data, result=hmart_dict, search_string=search_string)

    
    if len(matching) == 0:
        result = dict()
        return render_template('search_results.html', data = data, result=result, search_string=search_string)
    #make dictionary of flavor/id pairs
    else:
        ids = []
        for k in matching:
            x = ""
            for key, value in data.items():
                #each dictionary
                for i in value: #for each trait
                    if i == "flavor" and value[i] == k:
                        x = value["id"]
                        ids.append(x)
        result = dict(zip(ids, matching))
        return render_template('search_results.html', data = data, result=result, search_string=search_string) 




@app.route('/view/<page>')
def display_page(page):
    return render_template("view.html", data=data, page=page)

@app.route('/add_entry', methods = ['GET', 'POST'])
def add_entry():
    global data
    global current_id
    global limited_dict
    global organic_dict
    global vegan_dict
    global ws_dict
    global mw_dict
    global hmart_dict

    json_data = request.get_json()
    
    sub_dict = {
        "id" : str(current_id),
        "flavor" : json_data["flavor"],
        "description": json_data["description"],
        "price": json_data["price"],
        "ingredients": json_data["ingredients"],
        "features": json_data["features"],
        "photo": json_data["photo"],
        "rating": json_data["rating"],
        "calories":json_data["calories"],
        "stores":json_data["stores"],
    }
    #update databases for searching
    options_flavor.append(json_data["flavor"])
    if "limited" in json_data["features"]:
        limited_dict[str(current_id)] = json_data["flavor"]
    if "organic" in json_data["features"]:
        organic_dict[str(current_id)] = json_data["flavor"]
    if "vegan" in json_data["features"]:
        vegan_dict[str(current_id)] = json_data["flavor"]
    if "Morton Williams" in json_data["stores"] or "morton williams" in json_data["stores"]:
        mw_dict[str(current_id)] = json_data["flavor"]
    if "Westside Market" in json_data["stores"] or "westside market" in json_data["stores"]:
        ws_dict[str(current_id)] = json_data["flavor"]
    if "Hmart" in json_data["stores"] or "Hmart" in json_data["stores"]:
        hmart_dict[str(current_id)] = json_data["flavor"]

    data[str(current_id)] = sub_dict
    temp_id = current_id
    current_id += 1
    return jsonify(data=data, temp_id=temp_id)

@app.route('/edit_entry',  methods = ['GET', 'POST'])
def edit_entry():
    global data
    global limited_dict
    global organic_dict
    global vegan_dict
    global ws_dict
    global mw_dict
    global hmart_dict

    json_data = request.get_json()
    id = json_data["id"]
    sub_dict = {
        "id" : id,
        "flavor" : json_data["flavor"],
        "description": json_data["description"],
        "price": json_data["price"],
        "ingredients": json_data["ingredients"],
        "features": json_data["features"],
        "photo": json_data["photo"],
        "rating": json_data["rating"],
        "calories":json_data["calories"],
        "stores": json_data["stores"],
    }

    features = json_data["features"]
    print(features)
    for i in range(len(features)):
        features[i] = features[i].strip()

    stores = json_data["stores"]
    for i in range(len(stores)):
        stores[i] = stores[i].strip()


    if json_data["flavor"] != data[id]["flavor"]: #name change
        if id in limited_dict:
            limited_dict[id] = json_data["flavor"]
        if id in organic_dict:
            organic_dict[id] = json_data["flavor"]
        if id in vegan_dict:
            vegan_dict[id] = json_data["flavor"]
        if id in hmart_dict:
            hmart_dict[id] = json_data["flavor"]
        if id in mw_dict:
            mw_dict[id] = json_data["flavor"]
        if id in ws_dict:
            ws_dict[id] = json_data["flavor"]

    #adjust features (add)
    if "vegan" in features:
        vegan_dict[id] = json_data["flavor"]
    if "limited edition" in features:
        limited_dict[id] = json_data["flavor"]
    if "Hmart" in stores:
        hmart_dict[id] = json_data["flavor"]
    if "Morton Williams" in stores:
        mw_dict[id] = json_data["flavor"]
    if "Westside Market" in stores:
        ws_dict[id] = json_data["flavor"]
    if "organic" in features:
        organic_dict[id] = json_data["flavor"]

    if "organic" in data[id]["features"]:
        if "organic" not in features:
            del organic_dict[id]
    if "vegan" in data[id]["features"]:
        if "vegan" not in features:
            del vegan_dict[id]
    if "limited edition" in data[id]["features"]:
        if "limited edition" not in features:
            del limited_dict[id]
    if "Morton Williams" in data[id]["stores"]:
        if "Morton Williams" not in stores:
            del mw_dict[id]
    if "Westside Market" in data[id]["stores"]:
        if "Westside Market" not in stores:
            del ws_dict[id]
    if "Hmart" in data[id]["stores"]:
        if "Hmart" not in stores:
            del hmart_dict[id]
    

    data[id] = sub_dict

    #redefining dict values if they changed
    return jsonify(data=data, id=id)




if __name__ == '__main__':
   app.run(debug = True)




