import sqlite3

# conn = sqlite3.connect("chalan.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS violations (
#     violation_name TEXT,
#     fine INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO violations (violation_name, fine)
# VALUES
# ('no helmet', 200),
# ('overspeeding', 500),
# ('triple seat', 300),
# ('no parking', 600)
# """)

# conn.commit()
# conn.close()
# conn2 = sqlite3.connect("user.db")
# cursor1 = conn2.cursor()
# cursor1.execute("""
# CREATE TABLE vehicle_owner(
# Name VARCHAR(30),vehicle_type VARCHAR(30),vehicle_number VARCHAR(20),mobile_number INTEGER)
# """)
# cursor1.execute("""
# INSERT INTO vehicle_owner(Name,vehicle_type,vehicle_number,mobile_number)
# VALUES("Rahul sharma","Bike","TS09AB1234",8888888888),
# ("Priya","Car","TS10CD5678",7778472771), 
# ("Shrikant Deshmukh","Car","UK06AR2131",8600329545)""")
# conn2.commit()
# conn2.close()
def violation_fine(violation_name):
    conn = sqlite3.connect("chalan.db")
    cursor=conn.cursor()
    query="SELECT fine FROM violations WHERE violation_name = ?"
    cursor.execute(query,(violation_name,))
    result=cursor.fetchone()
    conn.commit()
    conn.close()
    return result[0]
def user_data(vehicle_number):
    conn2 = sqlite3.connect("user.db")
    cursor1 = conn2.cursor()
    query1="SELECT * From vehicle_owner WHERE vehicle_number = ?"
    cursor1.execute(query1,(vehicle_number,))
    result=cursor1.fetchone()
    conn2.commit()
    conn2.close()
    return result
