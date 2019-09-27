from flask import Flask, render_template,request,url_for,session,redirect,request
import os
import time


def pack_dicta(listi, dicta):
    list_flag = []
    for k,v in dicta.items():
        for k2,v1 in v.items():
            list_flag.append(v1)
        listi.append(list_flag)
        list_flag = []

def total_price():
    summa = 0
    for i in session["karfa"]:
        summa = summa + int(i[4])
    return summa

stor_items = {
"1":{
"nafn":"Skófla",
"uplýsingar":"létt og sterk skófla",
"verð":"1000kr",
"mynd":"https://www.pngarts.com/files/3/Shovel-Transparent-Image.png",
"verð-pure":"1000",
"id":"1"
},
"2":{
"nafn":"Hrífa",
"uplýsingar":"Traust hrífa sem svíkur ekki",
"verð":"500kr",
"mynd":"http://pluspng.com/img-png/png-of-a-rake-rake-png-475.png",
"verð-pure":"500",
"id":"2"
},
"3":{
"nafn":"Hjólbara",
"uplýsingar":"Góð hjólbara sem tekur allt að 100L",
"verð":"2000kr",
"mynd":"https://i1.wp.com/freepngimages.com/wp-content/uploads/2015/05/wheelbarrow.png?resize=900%2C900",
"verð-pure":"2000",
"id":"3"

},
"4":{
"nafn":"Strákústur",
"uplýsingar":"Strákústur með spítu skafti",
"verð":"900kr",
"mynd":"http://pngimg.com/uploads/broom/broom_PNG50.png",
"verð-pure":"900",
"id":"4"
}

}

listi_hlutir = []

pack_dicta(listi_hlutir, stor_items)

vorulisti = []
teljari = 0

app = Flask(__name__)
app.config["SECRET_KEY"]  ="blab"
hlutir = listi_hlutir



@app.route("/")
def index():
    if "karfa" not in session:
        session["karfa"] = []
    return render_template("index.html", hlutir = hlutir,teljari = len(session["karfa"]))

@app.route("/add/<id>")
def add(id):
    place_holder_list = []
    if "karfa" in session:
     for items in session["karfa"]:
         place_holder_list.append(items)
     for listi in listi_hlutir:
        if listi[5] == id:
            place_holder_list.append(listi)
            session["karfa"] = place_holder_list
            place_holder_list = []



    return redirect(url_for("index"))

@app.route("/checkout")
def checkout():
    vorur = session.get("karfa")
    total = total_price()
    return render_template("checkout.html", vorur= vorur, total = total)

@app.route("/del/<ids>")
def dele(ids):
    counter = 0
    place_holder_del_list = []
    for items in session["karfa"]:
        place_holder_del_list.append(items)
    for lists in place_holder_del_list:
        if ids == lists[5]:
            place_holder_del_list.pop(counter)
            session["karfa"] = place_holder_del_list
            place_holder_del_list = []
            break
        counter = counter + 1
    time.sleep(2)
    return redirect(url_for("checkout"))

@app.route("/checkoutfinal", methods=["GET","POST"])
def checkoutfinal():
    req = request.form
    if request.method == "POST":
        nafn = req.get("name")
        email = req.get("email")
        number = req.get("phone")
    total = total_price()
    return render_template("final.html", nafn = nafn, email = email, number=number, vorur = len(session["karfa"]), total = total)


@app.route("/popout")
def popout():
    session.pop("karfa", None)
    return redirect(url_for("index"))

@app.errorhandler(404)
def error(error):
    return"""vialla kom upp <a href="/">Heim</a>"""
    

@app.errorhandler(505)
def error(error):
    return"""vialla kom upp <a href="/">Heim</a>"""


if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
