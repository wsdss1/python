from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
#browser = webdriver.Firefox()
browser = webdriver.Chrome()
time.sleep (5) # долго грузится - делаем задержку
browser.get ('https://egrul.nalog.ru/')

# столбец с выписками ЕГРЮЛ
   
for x in range (2,10):    # 3-конечная ячейка в столбце A. первый аргумент - номер строки      
        wb = openpyxl.load_workbook('выпискиЕГРЮЛ.xlsx')
        sheet=wb.get_active_sheet()
        a = tuple (str(sheet.cell(row=x, column=1).value)) # получаем кортеж из ОГРН в ячейке A2 
        act = browser.find_element_by_id('query')
        act.click()
        time.sleep (1)
        # вводим посимвольно в строку ОГРН, т.к. ввод сразу всего ОГРН не корректно обрабатывается
        i=0
        for i in range (13):
                act.send_keys(a[i])
                #time.sleep (0.1)
                i+=1
        act = browser.find_element_by_css_selector('.btn-search')
        act.click()
        time.sleep (3)
        act = browser.find_element_by_css_selector('button.btn-with-icon:nth-child(2)')
        act.click()
        time.sleep (30)
        act = browser.find_element_by_id('query')
        act.click() 
        #удаляем старый ОГРН
        i=0
        for i in range (13):
               act.send_keys (Keys.BACK_SPACE)                       
               i+=1           
        
x += 1
browser.quit()


