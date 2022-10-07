import numpy as np
import pymysql

db = None
cur = None
db = pymysql.connect(host='192.168.200.2', user='swcore', password='core2020', db='logger', charset='utf8')

with open('tail2.log', 'r', encoding='UTF8') as file:
  for line in file.readlines():
    list = []
    txtv = ""
    sqlv = ""
    tk = len(line.split(','))
    if len(line.split(',')) >= 60:
      for i in range(0,tk):
        list = np.append(list, np.array([line.split(',')[i]]))
        if i == tk-1:
          sqlv = sqlv +"'"+ list[i]+"'"
        else:
          sqlv = sqlv + "'"+ list[i] +"'" + ","
        if i == tk - 1:
          txtv = txtv + "d"+ str('{0:03}'.format(i+1))
        else:
          txtv = txtv + 'd' + str('{0:03}'.format(i+1)) + ','
      print(sqlv)
      print(txtv)
      if list[3] == "SYSTEM":
        pass
      else:
        cur = db.cursor()
        sql = f"INSERT INTO logger.inoutT " +"("+ txtv +")"+ f" VALUES "+"("+ sqlv +")"
        print(sql)
        cur.execute(sql)
        db.commit()
    else:
      pass