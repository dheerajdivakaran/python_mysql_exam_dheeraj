import mysql.connector

class ProductManager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dheeraj@2004",
            database="shop_db"
        )
        self.mycursor = self.mydb.cursor()

    #GET all products
    def get(self):
        self.mycursor.execute("SELECT * FROM product")
        data = self.mycursor.fetchall()

        for i in data:
            print(i)

    #get ONE PRODUCT OBJECT
    def get_object(self,id):
        self.mycursor.execute("SELECT * FROM product where id=%s",(id,))
        data = self.mycursor.fetchone()
        return data

    #retrieve one product
    def retrieve(self,id):
        data = self.get_object(id)
        if data :
            print("product details:",data)
        else:
            print("product not found")

    #insert product
    def post(self,**kwargs):
        fields=",".join(kwargs.keys())
        placeholders=",".join(["%s"]*len(kwargs))
        values=tuple(kwargs.values())

        query= f"insert into product({fields}) values({placeholders})"

        self.mycursor.execute(query,values)
        self.mydb.commit()

        print("product added successfully")

    #update product
    def put(self,id,**kwargs):
        data = self.get_object(id)

        if data:
            fields = ",".join(
                [f"{key}=%s" for key in kwargs.keys()]
            )
            values = tuple(kwargs.values())+ (id,)
            query = f"UPDATE product SET{fields} where id=%s"
            self.mycursor.execute(query,values)
            self.mydb.commit()
            print("product updated successfully")
        else:
            print("not found")
    #delete product
    def delete(self,id):
        data=self.get_object(id)

        if data:
            self.mycursor.execute(
                "DELETE FROM product where id=%s",(id,)
            )
            self.mydb.commit()
            print("product deleted successfully")
        else:
            print("not found")



obj=ProductManager()

# obj.get()

# obj.retrieve(1)

# obj.post(name="laptop",category="electronics",price=45000,quantity=5,manufacturer="lenovo")

# obj.put(1,price=42000,quantity=8)
# obj.delete(1)


