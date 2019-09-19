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
"mynd":"https://images-na.ssl-images-amazon.com/images/I/71ae8LCFdZL._AC_SL1500_.jpg"
},
"2":{
"nafn":"d",
"uplýsingar":"e",
"verð":"f",
"mynd":"ss"
},
"3":{
"nafn":"g",
"uplýsingar":"e",
"verð":"k",
"mynd":"ss"
},
"4":{
"nafn":"f",
"uplýsingar":"j",
"verð":"l",
"mynd":"ss"
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
