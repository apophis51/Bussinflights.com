import re
import openpyxl
import openai
import time

wu = openpyxl.load_workbook('keywordget - Copy.xlsx')
sheet = wu['page1']


current_row = 2  #we start the sheet from the second row
for x,y in enumerate(sheet["a"]):
    if x < 1000:
        try:
            Dino = sheet[f"e{1+x}"].value
            Dino = Dino.replace("#",sheet[f"a{1+x}"].value)
            Distance = sheet[f"c{1+x}"].value
            Time = sheet[f"d{1+x}"].value
           # Distance = sheet[f"c{1+x}"].value

            Dino = Dino.replace("@", f" ( Use {Time})")
            Dino = Dino.replace("%", f" ( Use {Distance}) miles")

            Dino = Dino.replace("$"," (use Tuseday)")

            Dino = Dino.replace("#",sheet[f"a{1+x}"].value)
            sheet[f"e{1+x}"] = Dino
            print(Dino)
        except:
            continue
          #  sheet[f"e{1+x}"] = sheet[f"d{1+x}"].replace("#",sheet[f"e{1+x}"])
wu.save('keyword get - Copy.xlsx')
