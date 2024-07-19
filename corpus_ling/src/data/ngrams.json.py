import csv, json

with open("coca_ngrams.tsv") as tsvfile:
  tsvreader = csv.reader(tsvfile, delimiter = "\t")
  jsoned = []
  for line in tsvreader:
    if int(line[0]) >= 350:
      if jsoned == []:
        nuevo5 = {}
        nuevo5["name"] = line[5]
        nuevo5["value"] = line[0]
        nuevo4 = {}
        nuevo4["name"] = line[4]
        nuevo4["children"] = [nuevo5]
        nuevo3 = {}
        nuevo3["name"] = line[3]
        nuevo3["children"] = [nuevo4]
        nuevo2 = {}
        nuevo2["name"] = line[2]
        nuevo2["children"] = [nuevo3]
        nuevo1 = {}
        nuevo1["name"] = line[1]
        nuevo1["children"] = [nuevo2]
        jsoned.append(nuevo1)
      for x in jsoned:
        padre = next((x for x in jsoned if x["name"] == line[1]), None)
        if padre == None:
          nuevo5 = {}
          nuevo5["name"] = line[5]
          nuevo5["value"] = line[0]
          nuevo4 = {}
          nuevo4["name"] = line[4]
          nuevo4["children"] = [nuevo5]
          nuevo3 = {}
          nuevo3["name"] = line[3]
          nuevo3["children"] = [nuevo4]
          nuevo2 = {}
          nuevo2["name"] = line[2]
          nuevo2["children"] = [nuevo3]
          nuevo1 = {}
          nuevo1["name"] = line[1]
          nuevo1["children"] = [nuevo2]
          jsoned.append(nuevo1)
        else:
          padre2 = next((x for x in padre["children"] if x["name"] == line[2]), None)
          if padre2 == None:
            nuevo5 = {}
            nuevo5["name"] = line[5]
            nuevo5["value"] = line[0]
            nuevo4 = {}
            nuevo4["name"] = line[4]
            nuevo4["children"] = [nuevo5]
            nuevo3 = {}
            nuevo3["name"] = line[3]
            nuevo3["children"] = [nuevo4]
            nuevo2 = {}
            nuevo2["name"] = line[2]
            nuevo2["children"] = [nuevo3]
            padre["children"].append(nuevo2)
          else:
            padre3 = next((x for x in padre2["children"] if x["name"] == line[3]), None)
            if padre3 == None:
              nuevo5 = {}
              nuevo5["name"] = line[5]
              nuevo5["value"] = line[0]
              nuevo4 = {}
              nuevo4["name"] = line[4]
              nuevo4["children"] = [nuevo5]
              nuevo3 = {}
              nuevo3["name"] = line[3]
              nuevo3["children"] = [nuevo4]
              padre2["children"].append(nuevo3)
            else:
              padre4 = next((x for x in padre3["children"] if x["name"] == line[4]), None)
              if padre4 == None:
                nuevo5 = {}
                nuevo5["name"] = line[5]
                nuevo5["value"] = line[0]
                nuevo4 = {}
                nuevo4["name"] = line[4]
                nuevo4["children"] = [nuevo5]
                padre3["children"].append(nuevo4)
              else:
                padre5 = next((x for x in padre4["children"] if x["name"] == line[5]), None)
                if padre5 == None:
                  nuevo5 = {}
                  nuevo5["name"] = line[5]
                  nuevo5["value"] = line[0]
                  padre4["children"].append(nuevo5)


mjsoned = {}
mjsoned["name"] = "m"
mjsoned["children"] = jsoned
with open("ngrams.json", "w") as outfile:
  json.dump(mjsoned, outfile)