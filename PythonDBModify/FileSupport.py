import sqlite3

tableName = input("Enter a table name: ")
sku = input("Enter item SKU: ")

def GetLocation(boxLocation):
    location = input("Enter item location: ")
    
    x = input("Please input x coordinate of the box: ")
    y = input("Please input y coordinate of the box: ")
    BoxNo = input("Please input the box number: ")

    ShelfLocation = [[0]*x]*y
    print(ShelfLocation)

def CreateATable(tableName):
    conn = sqlite3.connect('OldInventory.db')
    c = conn.cursor()
    
    c.execute("""CREATE TABLE tableName (
        ItemNumber TEXT
        ShelfLocation TEXT
        Logo TEXT
        BoxNumber TEXT
        Gender TEXT
    )""")

    return tableName

    conn.commit()
    conn.close()


def TestForTable(tableName):
    conn = sqlite3.connect('OldInventory.db')
    c = conn.cursor()
    
    c.execute("SELECT name FROM sqlite_master WHERE name = (?)", tableName)

    conn.commit()
    conn.close()


def AddNewItem(ItemNumber, ShelfLocation, Logo, BoxNo, Gender):
    conn = sqlite3.connect('OldInventory.db')
    c = conn.cursor() 
    #spacer
    c.executemany("INSERT INTO tableName VALUES (?,?,?,?,?)", (ItemNumber,ShelfLocation,Logo,BoxNumber,Gender))
    #spacer
    conn.commit()
    conn.close()


def GetAttributes(SKU):
    #query the database for the attributes of the provided SKU
    conn = sqlite3.connect('OldInventory.db')
    c = conn.cursor() 

    #Query the Database
    c.execute("SELECT rowid, * FROM tableName")
    items = c.fetchall()
    
    for item in items:
        print(item)

    #commit the command
    conn.commit()
    #close the connection
    conn.close()

def ShowAll():
    #connect to the databases
    conn = sqlite3.connect('OldInventory.db')
    #create cursor
    c = conn.cursor() 

    #Query the Database
    c.execute("SELECT rowid, * FROM tableName")
    items = c.fetchall()
    
    for item in items:
        print(item)

    #commit the command
    conn.commit()
    #close the connection
    conn.close()
