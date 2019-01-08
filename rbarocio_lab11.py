# !/usr/bin/env python3
# rbarocio_lab11
# using functions and connecting sqlite3 db
import rbarocio_paras
import chinese_paras
import turtle    
import sqlite3
import webbrowser
def fsum(a, b, c):
    # returns the first sum based on users input
    fsum = a + b + c
    return fsum
def appending_to_log_file():
    # Ceates log file
    spacing = "-" * 100
    filename=("birthtest.log\n")
    fhandle=open(filename, 'a')
    fhandle.write(filename)
    fhandle.write('\n')
    fhandle.write(name)
    fhandle.write('\n')
    fhandle.write(str(bmonth))
    fhandle.write(str(bday))
    fhandle.write(str(byear))
    fhandle.write('\n')
    fhandle.write(paragraph)
    fhandle.write('\n')
    fhandle.write(spacing)
    fhandle.write('\n')
    fhandle.write(alert2)
    fhandle.write(chinese_paragraph)
    fhandle.close()
def creating_html_template():
    # Creates HTML Template
    header =("<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://fonts.googleapis.com/css?family=Fredoka+One' rel='stylesheet'></head><body>")
    style = ("<style>body{font-family: Fredoka One, cursive; font-size: 2em;\
background-image:url('images/abstract-geometric-background.png'); background-size:cover; background-repeat: no-repeat;}\
.content{margin: 400px 200px; background-color: #D61F5D; border-radius:5px; padding: 5px; color:#000; box-shadow: 15px 15px 10px #000;}</style>")
    footer=("</pre></body></html>")
    op = ('<p>')
    cp = ('</p>')
    hrule = ('<hr>')
    o_h1_tag = ('<h1>')
    c_h1_tag = ('</h1>')
    odiv = ('<div class="content">')
    cdiv = ('</div>')
    filename2 = ("birthtest.html")
    filehandle2=open(filename2, 'w')
    filehandle2.write(header)
    filehandle2.write(style)
    filehandle2.write(odiv)
    filehandle2.write(o_h1_tag)
    filehandle2.write(alert1)
    filehandle2.write(c_h1_tag)
    filehandle2.write(hrule)
    filehandle2.write('\n')
    filehandle2.write(op)
    filehandle2.write(paragraph)
    filehandle2.write(hrule)
    filehandle2.write(alert2)
    filehandle2.write('\n')
    filehandle2.write(chinese_paragraph)
    filehandle2.write(cp)
    filehandle2.write(cdiv)
    filehandle2.write(footer)
    filehandle2.close()

# connecting to database
conn = sqlite3.connect("extra_credit_db.sqlite")
# Connecting cursor
c = conn.cursor()
# Creates table in db
c.execute("""CREATE TABLE IF NOT EXISTS extra_credit_db (id INTEGER PRIMARY\
         KEY AUTOINCREMENT NOT NULL, datestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,\
         name TEXT, dob TEXT, paragraph TEXT, chinese_paragraph TEXT)""")

wn=turtle.Screen() # Screen for Turtle GUI 
wn.bgcolor("purple") # Sets screen to a specific color
turtle.color("white")# Sets font color to specific color

name = turtle.textinput("Name","Enter name: ")
bmonth = turtle.numinput("Enter month number ","Enter month of birth: ",1,minval=1, maxval=12)
bday = turtle.numinput("Enter day number","Enter day of birth: ",1,minval=1, maxval=31)
byear = turtle.numinput("Enter year digits","Enter year of birth: ",1997, minval=1, maxval=9999)

dob = str(bmonth)+str(bday)+str(byear) #DOB for db
pp = (fsum(bmonth, bday, byear) % 9) 
chp =((byear - 1899) % 12)
paragraph = (rbarocio_paras.pick_paragraph[pp])
chinese_paragraph = (chinese_paras.pick_chp[chp])

alert1 = ("{}, based on your date of birth your personality message is . . .".format(name))
alert2 = ("Your Chinese Zodiac sign is...")
main_para =("Hello welcome to the birth test calculator {}, \nbased on your date of birth your personality message is . . .\n{} \n{} \n {}".format(name,paragraph,alert2,chinese_paragraph))

turtle.write(main_para,False,align='center', font=('sans-serif', 16, 'bold'))
#Inserting data to DB
c.execute("""INSERT INTO extra_credit_db(name, dob, paragraph, chinese_paragraph) VALUES ("{}", "{}", "{}", "{}")""".format(name, dob, paragraph, chinese_paragraph))
# Saves data to  db
conn.commit()
c.execute("""SELECT * FROM extra_credit_db """)
for row in c:
    print(row)
appending_to_log_file()
creating_html_template()
webbrowser.open_new_tab('birthtest.html')
