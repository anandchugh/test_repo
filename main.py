import os



def sum(a,b):
    return (a+b)

def hello():
    name =  os.environ.get("name","test")
    print (f"name : {name}")

if __name__ =="__main__":
    hello()