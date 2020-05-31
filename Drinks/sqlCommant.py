import sqlite3 
"""
baglanti = connect
version 1.1
"""
baglanti = sqlite3.connect("market.db")
d_cursor = baglanti.cursor()

class sqlCo():
    def create_tble():
        d_cursor.execute("create table if not exists drinks (d_name TEXT,piece INT,price INT)")
        baglanti.commit()
    def add_tble(d_name,piece,price):
        d_cursor.execute("insert into drinks values(?,?,?)",(d_name,piece,price))
        baglanti.commit()
    
    def showOn_tble():
        d_cursor.execute("select* from drinks")
        table_datas =d_cursor.fetchall()
        for table_data in table_datas:
            print(table_data)
    def update_tble(old_price,new_price):
        d_cursor.execute("update drinks set price = ? where price = ? ",(new_price,old_price))
        baglanti.commit()
    def delete_column_tble(d_name):
        d_cursor.execute("delete from Drinks where d_name= ? ",(d_name,))
"""        
create_tble()
update_tble(18, 21)
showOn_tble()
"""
