import re
import openpyxl
import openai
import time


openai.api_key = "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" #new
myprompt = 'ignore "Mexico city" do not write "flights" and write the other location only. one noun' 
#response = openai.Completion.create(
           # model="text-davinci-003",
            #max_tokens=200,
            #prompt=myprompt,
            #temperature=0.6)

wu = openpyxl.load_workbook('keywordget.xlsx')
sheet = wu['page1']


current_row = 2  #we start the sheet from the second row
for x,y in enumerate(sheet["a"]):
    if x < 1000:
        
        result = sheet[f"a{1+x}"].value
        print(2, result)
        if result is not None:
            response = openai.Completion.create(
                                model="text-davinci-003",
                                max_tokens=4000,
                                prompt=result +" \n " + myprompt,
                                temperature=0.0)
            time.sleep(10)
            sheet[f"b{1+x}"] = response.choices[0].text
            print(f"b{1+x}")
print(response.choices[0].text)
wu.save('keywordget.xlsx')


