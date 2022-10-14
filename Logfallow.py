import time
import numpy as np
import os
import pymysql

db =None
cur = None
db = pymysql.connect(host='localhost', user='swcore', password='core2020', db='logger', charset='utf8')

def follow(thefile):
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line

if __name__ == '__main__':
    i = 0
    logfile = open("/var/log/syslog","r")
    loglines = follow(logfile)
    # iterate over the generator
    for line in loglines:
        lc = len(line.split(','))
        rline = []
        txtv = ""
        sqlv = ""
        if len(line.split(',')) >= 60:
            for i in range(0,lc):
                rline = np.append(rline, np.array([line.split(',')[i]]))
                if i == lc-1:
                    sqlv = sqlv + "'"+ rline[i]+"'"
                    txtv = txtv + "d"+ str('{0:03}'.format(i+1))
                else:
                    sqlv = sqlv + ","+ rline[i]+"',"
                    txtv = txtv + 'd' + str('{0:03}'.format(i+1)) + ','
            if rline[3] == "SYSTEM":
                pass
            else:
                cur = db.cursor()
                sql = f"INSERT INTO logger.inoutT " +"("+ txtv +")"+ f" VALUES "+"("+ sqlv +")"
                print(sql)
                cur.execute(sql)
                db.commit()
        else:
            pass
