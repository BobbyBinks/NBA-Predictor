import requests
from bs4 import BeautifulSoup
import openpyxl
import numpy as np
import pandas as pd
from time import sleep
import random

# Make a request to the webpage
URL = ['/boxscores/202312090LAL.html', '/boxscores/202312110CHO.html', '/boxscores/202312110DET.html', '/boxscores/202312110ORL.html', '/boxscores/202312110PHI.html', '/boxscores/202312110ATL.html', '/boxscores/202312110NYK.html', '/boxscores/202312110HOU.html', '/boxscores/202312110MEM.html', '/boxscores/202312110MIL.html', '/boxscores/202312110NOP.html', '/boxscores/202312110OKC.html', '/boxscores/202312110SAC.html', '/boxscores/202312110LAC.html', '/boxscores/202312120BOS.html', '/boxscores/202312120DAL.html', '/boxscores/202312120CHI.html', '/boxscores/202312120PHO.html', '/boxscores/202312120LAC.html', '/boxscores/202312130DET.html', '/boxscores/202312130WAS.html', '/boxscores/202312130MIA.html', '/boxscores/202312130TOR.html', '/boxscores/202312130HOU.html', '/boxscores/202312130MIL.html', '/boxscores/202312130SAS.html', '/boxscores/202312130PHO.html', '/boxscores/202312130UTA.html', '/boxscores/202312140BOS.html', '/boxscores/202312140MIA.html', '/boxscores/202312140DAL.html', '/boxscores/202312140DEN.html', '/boxscores/202312140POR.html', '/boxscores/202312140SAC.html', '/boxscores/202312140LAC.html', '/boxscores/202312150CHO.html', '/boxscores/202312150PHI.html', '/boxscores/202312150WAS.html', '/boxscores/202312150BOS.html', '/boxscores/202312150SAS.html', '/boxscores/202312150TOR.html', '/boxscores/202312150MEM.html', '/boxscores/202312150PHO.html', '/boxscores/202312160MIL.html', '/boxscores/202312160CHO.html', '/boxscores/202312160CLE.html', '/boxscores/202312160MIA.html', '/boxscores/202312160MIN.html', '/boxscores/202312160GSW.html', '/boxscores/202312160DEN.html', '/boxscores/202312160POR.html', '/boxscores/202312160SAC.html', '/boxscores/202312160LAC.html', '/boxscores/202312170BOS.html', '/boxscores/202312170SAS.html', '/boxscores/202312170MIL.html', '/boxscores/202312170PHO.html', '/boxscores/202312170POR.html', '/boxscores/202312180CLE.html', '/boxscores/202312180IND.html', '/boxscores/202312180PHI.html', '/boxscores/202312180ATL.html', '/boxscores/202312180MIA.html', '/boxscores/202312180TOR.html', '/boxscores/202312180OKC.html', '/boxscores/202312180DEN.html', '/boxscores/202312180UTA.html', '/boxscores/202312180SAC.html', '/boxscores/202312180LAL.html', '/boxscores/202312190NOP.html', '/boxscores/202312190MIL.html', '/boxscores/202312190GSW.html', '/boxscores/202312190POR.html', '/boxscores/202312200CLE.html', '/boxscores/202312200IND.html', '/boxscores/202312200ORL.html', '/boxscores/202312200PHI.html', '/boxscores/202312200BRK.html', '/boxscores/202312200TOR.html', '/boxscores/202312200CHI.html', '/boxscores/202312200HOU.html', '/boxscores/202312200DAL.html', '/boxscores/202312200SAC.html', '/boxscores/202312210DET.html', '/boxscores/202312210CLE.html', '/boxscores/202312210CHI.html', '/boxscores/202312210MEM.html', '/boxscores/202312210MIL.html', '/boxscores/202312210OKC.html', '/boxscores/202312210MIN.html', '/boxscores/202312210POR.html']
input = int(input("Enter the row from which to start the player output:"))
arr=[]
for n in range(0,len(URL)):
    page = requests.get("https://www.basketball-reference.com"+URL[n])
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all('div',class_='table_container')
    list=[]
#Away team
    for table in tables[2].find_all('table'):
        for name in table.find_all('a')[0:5]:
            list.append(str(name.get_text()))
#Home team
    for table in tables[13].find_all('table'):
        for name in table.find_all('a')[0:5]:
            list.append(str(name.get_text()))
#Away
    for table in tables[0].find_all('tfoot'):
        #assists
        list.append(str(table.find_all('td')[13].get_text()))
        #turnovers
        list.append(str(table.find_all('td')[16].get_text()))
        #offensive rebounds
        list.append(str(table.find_all('td')[10].get_text()))
        #free throw
        list.append(str(table.find_all('td')[7].get_text()))
        #field goal
        list.append(str(table.find_all('td')[1].get_text())) 
#Home
    for table in tables[8].find_all('tfoot'):
        #if statement added as noticed sometimes table 8 (home team basic stats) gets pushed to table 9 due to away team advanced stats table
        if (float(table.find_all('td')[1].get_text())) <1:
            for table in tables[9].find_all('tfoot'):
                list.append(int(table.find_all('td')[13].get_text()))
                list.append(int(table.find_all('td')[16].get_text()))
                list.append(int(table.find_all('td')[10].get_text()))
                list.append(int(table.find_all('td')[7].get_text()))
                list.append(int(table.find_all('td')[1].get_text()))  
        else:
            list.append(int(table.find_all('td')[13].get_text()))
        #turnovers
            list.append(int(table.find_all('td')[16].get_text()))
        #offensive rebounds
            list.append(int(table.find_all('td')[10].get_text()))
        #free throw
            list.append(int(table.find_all('td')[7].get_text()))
        #field goal
            list.append(int(table.find_all('td')[1].get_text()))  
    print(list)
    sleep(random.uniform(8,12))
#    workbook = openpyxl.load_workbook('NBA Referee Assignments 2023-2024.xlsx')
#    worksheet = workbook['Players input']
#    for col in range(1, len(list) + 1):
#        cell = worksheet.cell(row=n+input, column=col)
#        cell.value = list[col - 1]
#    workbook.save('NBA Referee Assignments 2023-2024.xlsx')

#df = pd.DataFrame(arr)
# Specify the Excel file path
#excel_file_path = 'NBA Referee Assignments 2023-2024.xlsx'
# Open the Excel file
#with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
    # Write the DataFrame to the Excel file starting from the specified row
#    df.to_excel(writer, sheet_name='Players Input', index=False, startrow=input, header=False)