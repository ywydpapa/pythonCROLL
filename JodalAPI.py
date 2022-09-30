from datetime import datetime,timedelta
import requests
import pandas as pd
import pymysql

db = None
cur = None
db = pymysql.connect(host='192.168.200.2', user='swcore', password='core2020', db='jodal', charset='utf8')

fromdate = datetime.today()
todate = datetime.today() - timedelta(1)
datafrom = "" #시작일
datato = "" #종료일

if datafrom is None:
    datafrom = fromdate.strftime("%Y%m%d")
if datato is None:
    datato = todate.strftime("%Y%m%d")

vatno = "6058177638"

url ="https://apis.data.go.kr/1230000/ShoppingMallPrdctInfoService05/getSpcifyPrdlstPrcureInfoList?serviceKey=pLPvMUbq1ZSf6B3nwMFV0mvd6rOMYxX%2BwmcX7rwwvjlsXnH5v5OvgEu0ikW8Nux5L2RVG%2Bz51wb5KyDsQTvQ2Q%3D%3D&numOfRows=999&pageNo=1&type=json&inqryDiv=1&inqryBgnDate="+datafrom+"&inqryEndDate="+datato+"&inqryPrdctDiv=2&dtilPrdctClsfcNoNm=%EB%B0%A9%ED%99%94%EB%B2%BD&bizno="+vatno
resource = requests.get(url, verify=False).json()
pdata = resource.get('response')
gdata = pdata.get('body')
idata = gdata.get('items')
df = pd.DataFrame(idata)

for i in range(len(df)):
    val01 = '100001' #회사코드
    val02 = df.iloc[i]["dminsttCd"] #수요기관코드
    val03 = df.iloc[i]["dminsttNm"] #수요기관명
    val04 = df.iloc[i]["dmndInsttDivNm"] #수요기관종류
    val05 = df.iloc[i]["dminsttRgnNm"] #수요지역
    val06 = df.iloc[i]["cntrctDlvrReqNo"] #계약번호
    val07 = df.iloc[i]["prdctClsfcNo"] #계약물품번호
    val08 = df.iloc[i]["prdctClsfcNoNm"] # 계약품목
    val09 = df.iloc[i]["prdctUprc"] #단가
    val10 = df.iloc[i]["prdctUnit"] #수량
    val11 = df.iloc[i]["prdctQty"] #단위
    val12 = df.iloc[i]["prdctAmt"] #금액
    val13 = df.iloc[i]["cntrctDlvrReqNm"] #계약건명
    val14 = df.iloc[i]["incdecQty"] #증감수량
    val15 = df.iloc[i]["incdecAmt"] #증감금액
    val16 = df.iloc[i]["cntrctDlvrReqDate"] #계약일자
    val17 = df.iloc[i]["dlvrTmlmtDate"] #기한일자
    val18 = df.iloc[i]["dlvrPlceNm"] #납품장소
    cur = db.cursor()
    sql1 =  f"SELECT COUNT(*) EXT from swc_pps where reqNo = '{val06}'"
    cur.execute(sql1)
    rtn = cur.fetchone()
    if rtn[0] < 1:
        sql = f"INSERT INTO swc_pps (compNo,buyerCode,buyerName,buyerArea,buyerAreacode,reqNo,reqItemcode,reqItem,itemNetprice,itemQty,itemUnit,itemAmount,contractTitle,modQty,modAmount,contractDate,deliveryDate,deliveryPlace,regDate) values ('{val01}','{val02}','{val03}','{val04}','{val05}','{val06}','{val07}','{val08}','{val09}','{val10}','{val11}','{val12}','{val13}','{val14}','{val15}','{val16}','{val17}','{val18}',now())"
        cur.execute(sql)
        db.commit()
    else:
        print("중복 데이터")
