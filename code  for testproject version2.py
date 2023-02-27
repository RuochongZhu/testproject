import csv
import pandas as pd
import time
import sqlite3
def write2db(rows, db_file_pth = "./test.db"):
    conn = sqlite3.connect(db_file_pth)
    cursor = conn.cursor()
    for row in rows:
        effected_rows = cursor.execute("insert into report values(?,?,?,?,?,?,?,?,?,?,?,?,?)",row)
        print(row)
    conn.commit()
    conn.close()
def read(file_pth):
    rows = []
    with open(file_pth, encoding='utf-8') as f:
        file = csv.reader(f)
        headers = next(file)
        print(headers)
        for row in file:
            print(row)
            if len(row) != 0:
                # parse date to seconds
                # row[6] = time.mktime(pd.to_datetime(row[6]).timetuple())
                print(row[6])
                rows.append(row)
    return rows

rows = read(file_pth="apagon_data_processed(1).csv")
rows.sort(key=lambda a: a[-2])
pnt=[]#重复的行号去掉
prev_barrio_id = -1
prev_t = time.mktime(pd.to_datetime(rows[0][6]).timetuple())-61
prev_has_power = rows[0][5]
for i in range(len(rows)):
    row = rows[i]
    t = time.mktime(pd.to_datetime(row[6]).timetuple())
    barrio_id = row[-2]
    has_power = row[5]

    print(i != 0 and prev_barrio_id == barrio_id and t - prev_t <= 60 and has_power == prev_has_power)

    print(row)
    # 对比上一行
    if(i!=0 and prev_barrio_id == barrio_id and t-prev_t <= 60 and has_power == prev_has_power):
        pnt.append(i-1)
    # 更新记录
    prev_barrio_id = barrio_id
    prev_has_power = has_power
    prev_t = t
    print(i)
idx = 0
result = []
for i in range(len(rows)):
    if (idx < len(pnt) and i == pnt[idx]):
        idx = idx + 1
        continue
    result.append(rows[i])
print(result)

print(len(result))
f = open('result.csv','w', encoding='utf8')
writer = csv.writer(f)
for i in range(len(result)):
    writer.writerow(result[i])
f.close()

