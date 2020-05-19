class TableInfo4oracle:
    """
    테이블의 기본적인 메타 정보(행수,컬럼수,날짜 범위)를 보는 클래스
    show_table_col을 통해서 날짜 범위를 볼 컬럼을 확인->show_table_dateRange
    """
    def __init__(self, table_name, con):
        self.table_name = table_name
        self.con = con

    def show_table_col(self):
        #row count
        d(pd.read_sql(f"""
            SELECT COUNT(*) FROM {self.table_name}
            """, con=self,con))
        #col
        tmp = pd.read_sql(f"""
                SELECT * FROM {self.table_name}
                WHERE ROWNUM<4""", con=self.con)
        d(tmp.columns)
        d(tmp.T)

    def show_table_dateRange(self, date_col):
        d(pd.read_sql(f"""
                SELECT MIN({date_col}), MAX({date_col}) 
                FROM {self.table_name}""", con=self.con))