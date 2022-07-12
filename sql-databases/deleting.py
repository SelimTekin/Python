from re import X
from matplotlib.pyplot import connect
import mysql.connector

def deleteProduct(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "delete from products where id=%s" # where olmazsa tablodaki bütün kayıtlar silinir.
    sql = "delete from products where id="+id # böyle de olabilir ama o zaman sql injection riskine karşı önlem alınmamış olur.  
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

deleteProduct(5)