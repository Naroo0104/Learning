import cx_Oracle

# DB연결, 접속, 커서 받아오기
# -리턴값: 커서
def getDBConnCursor():
    try:
        #서버 찾아가기
        dsn=cx_Oracle.makedsn('localhost',1521,'xe')
        #서버와 접속하기(통로 생성)
        conn=cx_Oracle.connect("GWANGJU_B","DBDB", dsn)
        #커서 받아오기(서버에 sql구문 및 결과를 실어나르는 역할)
        cursor=conn.cursor()
    except:
        return False
    
    return conn, cursor

# DB접속 해제
def DBClose(cursor, conn):
    #커서 역할 종결(반납)
    cursor.close()
    #접속 끊기(통로 삭제)
    conn.close()


#여러 건 처리 : [{},{}] 형태로 리턴
def getFetchAll(colname, rows):
    #컬럼명만 추출해 리스트에 담기
    col=[]

    for i in colname:
        col.append(i[0].lower())
        # col.append(i[0].lower())
    
    # 딕셔너리에 담기
    #
    list_row=[]

    # 풀어헤치기
    for cols in rows:
        dict_col={}
        for i in range(0,len(cols),1):
            dict_col[col[i]]=cols[i]
            # print("key[{}]/value[{}]".format(col[i],cols[i]))
        list_row.append(dict_col)
        # 이 결과가 objects.all이 던져주는 값과 같음
        
    return list_row


#주문정보 조회하기
def getCartList():    
    conn, cursor=getDBConnCursor()
   
    
         
    #sql 구문 작성
    sql="""
        SELECT CART_MEMBER, CART_NO, CART_PROD, CART_QTY 
        FROM CART
        ORDER BY CART_MEMBER ASC
    """
    #구문을 서버에 보내서 요청하고 결과 받아오기
    cursor.execute(sql)
    #받아온 결과를 달라고 요청
    rows=cursor.fetchall()
    
    
    #컬럼명 조회
    colname=cursor.description
    
    list_row=getFetchAll(colname, rows)
        
        
    DBClose(cursor, conn)
    
    return list_row 
