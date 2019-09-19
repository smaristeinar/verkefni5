from flask import Flask, render_template
import os
import csv

def opnaSkra(file,listi):
    try:
        with open(file, "r") as csv_file:
            new_file = csv.reader(csv_file, delimiter=';')
            for lines in new_file:
                listi.append(listi)
    except IOError:
        print("villa komupp þegar það ver reint að lesa skjalið")
    finally:
        print("það tókst að lesa skránna!")
        csv_file.close()

def writeFile(file, listi):
    try:
        string = ""
        with open(file, "w", ) as csv_file:
            for msg in listi:
                csv_file.write(msg)

    except IOError:
        print("villa kom upp við skrift a skalinu")
    finally:
        csv_file.close()

def pack_dicta(listi, dicta):
    list_flag = []
    for k,v in dicta.items():
        for k2,v1 in v.items():
            list_flag.append(v1)
        listi.append(list_flag)
        list_flag = []

stor_items = {
"1":{
"nafn":"Skófla",
"uplýsingar":"létt og sterk skófla",
"verð":"1000kr",
"mynd":"https://www.pngarts.com/files/3/Shovel-Transparent-Image.png",
"verð-pure":"500"
},
"2":{
"nafn":"Hrífa",
"uplýsingar":"Traust hrífa sem svíkur ekki",
"verð":"500kr",
"mynd":"http://pluspng.com/img-png/png-of-a-rake-rake-png-475.png",
"verð-pure":"500"
},
"3":{
"nafn":"Hjólbara",
"uplýsingar":"Góð hjólbara sem tekur allt að 100L",
"verð":"2000kr",
"mynd":"https://i1.wp.com/freepngimages.com/wp-content/uploads/2015/05/wheelbarrow.png?resize=900%2C900",
"verð-pure":"2000"
},
"4":{
"nafn":"Strákústur",
"uplýsingar":"Strákústur með spítu skafti",
"verð":"900kr",
"mynd":"http://pngimg.com/uploads/broom/broom_PNG50.png",
"verð-pure":"900"
}

}

listi_hlutir = []

pack_dicta(listi_hlutir, stor_items)

app = Flask(__name__)

@app.route("/")
def index():
    hlutir = listi_hlutir
    return render_template("index.html", hlutir = hlutir)




if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
