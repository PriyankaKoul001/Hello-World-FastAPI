from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def main():
    return "Hello, World!"

@app.get('/owner')
def owner_name():
    return "Build and Maintained by Priyanka koul!!!"