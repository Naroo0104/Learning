import cx_Oracle

#회원정보 조회하기
def getMemberList():
    try:
        #서버 찾아가기
        dsn=cx_Oracle.makedsn('localhost',1521,'xe')
        #서버와 접속하기(통로 생성)
        conn=cx_Oracle.connect("GWANGJU_B","DBDB", dsn)
        #커서 받아오기(서버에 sql구문 및 결과를 실어나르는 역할)
        cursor=conn.cursor()
        
        #sql 구문 작성
        sql="""
            SELECT MEM_ID, MEM_PASS, MEM_NAME, MEM_ADD1 
            FROM MEMBER 
            ORDER BY MEM_NAME ASC
        """
        #구문을 서버에 보내서 요청하고 결과 받아오기
        cursor.execute(sql)
        #받아온 결과를 달라고 요청
        row=cursor.fetchall()
        
        #커서 역할 종결(반납)
        cursor.close()
        #접속 끊기(통로 삭제)
        conn.close()
    except:
        return "Error다!"
    
    return row  
