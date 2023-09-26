# this is for starting fast api on local when u are working on the project and its not dockerised
import uvicorn

if __name__== "__main__":
    uvicorn.run("main:app",host="localhost",port=6942,reload=True)