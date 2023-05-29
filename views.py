from django.shortcuts import render
from .MyForm import InputForm
from django.http import HttpResponse
import matplotlib.pyplot as plt

import mysql.connector as m

# database creation
mydatabase = m.connect(host="localhost", user="root", password="Aish@123", database="pythondb1")
query = "insert into students(name,python_marks,java_marks,sql_marks) values(%s,%s,%s,%s)"  # must be "s"
cursor = mydatabase.cursor()

query2 = "select * from students;"
query3 = "select max(python_marks) from students;"
query4 = "select max(java_marks) from students;"
query5 = "select max(sql_marks) from students;"


# Create your views here.
def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)


def result(request):
    form = InputForm(request.POST)
    cursor.execute(query, [form['name'].value(), form['python_marks'].value(), form['java_marks'].value(),
                           form['sql_marks'].value()])
    mydatabase.commit()
    print(form['name'].value(), "  ", form['python_marks'].value(), "   ", form['java_marks'].value(), " ",
          form['sql_marks'].value())
    return HttpResponse(form['name'].value() + "   " + form['python_marks'].value() + "    " + str(
        form['java_marks'].value() + "  " + str(form['sql_marks'].value())))
    # return HttpResponse()


def get_result(request):
    cursor.execute(query2)
    mylist = cursor.fetchall()

    cursor.execute(query3)
    maxpython = cursor.fetchall()

    cursor.execute(query4)
    maxjava = cursor.fetchall()

    cursor.execute(query5)
    maxsql = cursor.fetchall()

    return render(request, "studentsData.html",
                  {"records": mylist, "records2": maxpython, "records3": maxjava, "records4": maxsql})


