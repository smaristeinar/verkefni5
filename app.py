from flask import Flask, render_template,request,url_for,session,redirect
import os
import time

def pack_dicta(listi, dicta):
    list_flag = []
    for k,v in dicta.items():
        for k2,v1 in v.items():
            list_flag.append(v1)
        listi.append(list_flag)
        list_flag = []

def total_price(listi):
    summa = 0
    for i in listi:
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

hlutir = listi_hlutir
@app.route("/")
def index():
    return render_template("index.html", hlutir = hlutir,teljari = len(vorulisti))

@app.route("/add/<id>")
def add(id):
     for listi in listi_hlutir:
        if listi[5] == id:
         vorulisti.append(listi)

     time.sleep(2)
     return redirect(url_for("index"))

@app.route("/checkout")
def checkout():
    vorur = vorulisti
    total = total_price(vorulisti)
    return render_template("checkout.html", vorur= vorur, total = total)

@app.route("/del/<ids>")
def dele(ids):
    counter = 0
    for lists in vorulisti:
        if ids == lists[5]:
            vorulisti.pop(counter)
            break
        counter = counter + 1
    time.sleep(2)
    return redirect(url_for("checkout"))

if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
