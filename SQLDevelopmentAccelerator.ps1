# Adam Lewis
# This app is made in order to accelerate the startup in development time
# it is starting as a Python SQL development tool, but can be upgraded to do more later!
# 
# The Future
# add project search by name. make a function that scans through all file names
# 
# 

$appLocation = "C:\Users\adama\Desktop\InventoryApp\PythonDBModify"
$file = "$appLocation\Instructions.txt"

function Get-Menu(){
    #$menuOption = Read-Host ""
}

function Get-ProjectName{
    #take the users input of the project name
    #scan through the project folder
    
    #$projectName = Read-Host "Please enter the project file name: " (add it to the parameters of Get-OpenDevApps($projectName))
}

function Get-OpenDevApps(){
    invoke-item "C:\Program Files\DB Browser for SQLite\DB Browser for SQLite.exe"
    # Start-Process "C:\Program Files\DB Browser for SQLite\DB Browser for SQLite.exe" "$projectName"
    write-output "Opening DB Browser for SQLite"
    invoke-item "C:\Program Files\Git\git-bash.exe"
    # Start-Process "C:\Program Files\DB Browser for SQLite\git-bash.exe" "$projectName"
    write-output "Opening git-bash"
    invoke-item "C:\Program Files\Sublime Text\sublime_text.exe"
    # Start-Process "C:\Program Files\DB Browser for SQLite\sublime_text.exe" "$projectName"
    write-output "Opening sublime_text"
}

function Get-TextFileWithInfo(){
    New-Item "$appLocation\Instructions.txt"
    "Development app information"| Out-File -FilePath "$appLocation\Instructions.txt" -Append
    "DB Browser for SQLite - Check the database(s) with a GUI "| Out-File -FilePath "$appLocation\Instructions.txt" -Append
    "git-bash - user friendly terminal"| Out-File -FilePath "$appLocation\Instructions.txt" -Append
    "sublime_text - text editor for the SQL Python combo"| Out-File -FilePath "$appLocation\Instructions.txt" -Append
    Invoke-Item "$appLocation\Instructions.txt"
}

#run all of the functions that we've built in order to develop sql databases
Get-Menu
Get-OpenDevApps
if (-not(Test-Path -Path $file -PathType Leaf)){
    Get-TextFileWithInfo
    Write-Host "Created an Instructions file"
} else {
    Write-Host "Opening the Instructions file"
    Invoke-Item "$appLocation\Instructions.txt"
}





