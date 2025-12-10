from sql import get_sql
from mysql.connector import Error
from fastapi import FastAPI

app = FastAPI()



@app.post("/create/user")

def create_user(name,email,password):
    db=get_sql()
    cursor = db.cursor(dictionary=True) # cursor is used to run sql commands in commands
    query = "Insert into tbluser(name,email,password) values(%s,%s,%s)"
    cursor.execute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"Values entered!!"}

# results = create_user("Laukik", "laukikbelsare@gmail.com","Laukik@54321")
# print(results)

def get_user_by_id(user_id):
    try:
        db=get_sql()
        cursor = db.cursor(dictionary=True)
        query= "select id, name, email,password from tbluser where id=%s"
        cursor.execute(query,(user_id,))
        user = cursor.fetchone()
        return {"message":"User fetched succesfully!!","data":user}
    except Error as e:
        return {"Error:":str(e)}
    finally:
        cursor.close()
        db.close()

# result2 = get_user_by_id(1)
# print(result2)

#write the function to update and delete the user

def update_values(user_id,name,password,email):
    try:
        db=get_sql()
        cursor=db.cursor(dictionary=True)
        query="update tbluser set name = %s, email= %s, password= %s where id=%s "
        cursor.execute(query,(name,email,password,user_id))
        db.commit()
        return {"message":"User updated succesfully!!"}
    except Error as e:
        return {"Error":str(e)}
    finally:
        db.close()
        cursor.close()

# result3=update_values(1,"Abhijeet","Abhijeet@54321","abhijeetmaurya@gmail.com")
# print(result3)


def delete_values(user_id):
    try:
        db=get_sql()
        cursor=db.cursor(dictionary=True)
        query= "delete from tbluser where id=%s "
        cursor.execute(query,(user_id,))
        db.commit()
        return {f"message":"row with id: {usere_id} deleted!! "}
    except Error as e:
        return {"Error":str(e)}
    finally:
        db.close()
        cursor.close()

result4=delete_values(1)
print(result4)

