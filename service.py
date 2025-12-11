from sql import get_sql
from mysql.connector import Error
from fastapi import FastAPI, APIRouter


router=APIRouter()


@router.post("/create/user") #API endpoint
def create_user(name,email,password):
    db=get_sql()
    cursor = db.cursor(dictionary=True) # cursor is used to run sql commands in commands
    query = "Insert into tbluser(name,email,password) values(%s,%s,%s)"
    cursor.execute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"Values entered!!"}

# results = create_user("Karan ", "karan@gmail.com","karan@54321")
# print(results)

@router.get("/get/user") #API end point
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

@router.put("/update/user") #API end point
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

# result3=update_values(1,"saurabh","Abhijeet@54321","abhijeetmaurya@gmail.com")
# print(result3)

@router.delete("/delete/user") #API endpoint
def delete_values(user_id):
    try:
        db=get_sql()
        cursor=db.cursor(dictionary=True)
        query= "delete from tbluser where id=%s "
        cursor.execute(query,(user_id,))
        db.commit()
        if cursor.rowcount == 0  :
            return {f"message":"user_id is not present in the database"}
        else:
            return {f"message":"row deleted!!"}
    except Error as e:
        return {"Error":str(e)}
    finally:
        db.close()
        cursor.close()

# result4=delete_values(5)
# print(result4)

# http://127.0.0.1:8000/create/user  {{We use this in frontend to connect to the frontend}}
# name,email,password -> payload (Passisng group of data in form of API)
