import FileSupport
import sqlite3

tableName = input("Please enter a table name: ")
ItemNumber = input("Please enter the item's SKU: ")
ShelfLocation = input("Please enter the shelf location of the object: ")
Logo = input("Does the item have a logo?(Y/N): ")
BoxNumber = input("What is the box number: ")
Gender = input("Gender (M/F): ")


FileSupport.CreateATable(tableName)
FileSupport.AddNewItem(ItemNumber,ShelfLocation,Logo,BoxNumber,Gender)
FileSupport.GetLocation(ShelfLocation)
FileSupport.Showall()




