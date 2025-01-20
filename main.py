from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from authentication import get_current_user
from schemas import Created_User, Show_User, Token, User
from token_gen import create_access_token

app = FastAPI()


@app.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):

    # Query the user from the database
    # user = db.query(models.User).filter(models.User.email == request.username).first()

    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail="User Not Found..!")

    # # Verify password using the hashing utility
    # if not Hash.verify(request.password, user.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail="Wrong Password Try Again..!")

    print(request)
    # Generate JWT token for the authenticated user
    access_token = create_access_token(data={"sub": request.username})
    return Token(access_token=access_token, token_type="bearer")


# POST route to create a new user
@app.post('/User/create' , response_model=Created_User)
def create(request: User):

    print(request.name)
    print(request.email)
    
    # Response message
    result = {"name": request.name, "email": request.email}
    
    return result


@app.get('/User/getuser',  response_model=Show_User)
def getuser(id:int , get_current_user:User = Depends(get_current_user)):
    userlist= [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "securepassword123"
        },
        {
            "id": 2,
            "name": "Alice Smith",
            "email": "alice.smith@example.com",
            "password": "password456"
        },
        {
            "id": 3,
            "name": "Bob Johnson",
            "email": "bob.johnson@example.com",
            "password": "mypassword789"
        },
        {
            "id": 4,
            "name": "Charlie Brown",
            "email": "charlie.brown@example.com",
            "password": "charlie123"
        },
        {
            "id": 5,
            "name": "Diana Prince",
            "email": "diana.prince@example.com",
            "password": "wonderwoman456"
        }
    ]


    # Simplified search for the user by ID
    for user in userlist:
        if user["id"] == id:
            return {"id": user["id"], "name": user["name"], "email": user["email"]}
    
    # If user is not found, raise a 404 error
    raise HTTPException(status_code=404, detail="User not found")



# run the app :
# uvicorn main:app --host 127.0.0.1 --port 8081 --reload