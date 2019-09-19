import csv


def opnaSkra(file,listi3):
    try:
        with open(file, "r") as csv_file:
            new_file = csv.reader(csv_file, delimiter=';')
            for lines in new_file:
                print(lines)
    except IOError:
        print("villa komupp þegar það ver reint að lesa skjalið")
    finally:
        print("það tókst að lesa skránna!")
        csv_file.close()

def writeFile(file, listi):
    try:
        string = ""
        with open(file, "w",) as csv_file:
            for msg in listi:
                string = msg + ";"
                csv_file.write(string + "\n")
                string = ""

    except IOError:
        print("villa kom upp við skrift a skalinu")
    finally:
        csv_file.close()

listi2 = ["hallo","heimur","ég","vona að þetta virki og ég vona að þessi strengur komist líka í gegn plís",]
opnaSkra("shitmsg.txt", listi2)
#writeFile("shitmsg.txt", listi)



for i in listi2:
    print(i)
