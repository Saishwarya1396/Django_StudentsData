import mysql.connector as m
import tkinter as tk
import matplotlib.pyplot as plt  #for matplotlib

# database connectivity
mydatabase=m.connect(host="localhost",user="root",password="Aish@123",database="pythondb1")
cursor=mydatabase.cursor()

# create the GUI
root = tk.Tk()
root.title("Students Result")
root.geometry('400x400')

# Configure GUI styles
root.configure(bg="#ADD8E6")  # Set background color

# Define custom colors
bg_color = "#FFC0CB"  # Background color for components
button_color = "#90EE90"  # Color for buttons

# Define fonts
button_font = ("Arial", 12, "bold")

def show_details():
    query = "SELECT * FROM students;"
    cursor.execute(query)
    details = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Fetch column names from cursor

    # Print column names
    print("\t ".join(columns))

    for detail in details:
        print("\t\t\t".join(str(d) for d in detail))

def max_Python_marks():
    queryP=" select name ,python_marks from students where python_marks = (select max(python_marks) from students);"
    cursor.execute(queryP)
    max_p=cursor.fetchall()
    print(max_p)
def max_java_marks():
    queryP=" select name ,java_marks from students where java_marks = (select max(java_marks) from students);"
    cursor.execute(queryP)
    max_j=cursor.fetchall()
    print(max_j)
def max_sql_marks():
    queryP=" select name ,sql_marks from students where sql_marks = (select max(sql_marks) from students);"
    cursor.execute(queryP)
    max_s=cursor.fetchall()
    print(max_s)


def graph():
    query1= "select (python_marks+java_marks+sql_marks) as Total from students;"
    cursor.execute(query1)
    total_marks = cursor.fetchall()
    print(total_marks)

    query2 = "SELECT name from students;"
    cursor.execute(query2)
    name = cursor.fetchall()
    print(name)

    l1=[]
    for i in total_marks:
        l1.append(i[0])

    l2=[]
    for i in name:
        l2.append(i[0])

    plt.bar(l2, l1)
    plt.ylabel("Total Marks")
    plt.xlabel("Name")
    plt.title("RESULT")
    plt.show()

def open_max_window():
    max_window = tk.Toplevel(root)
    max_window.title("Max Marks")
    max_window.geometry('200x200')
    max_window.configure(bg=bg_color)

    max_button = tk.Button(max_window, text="Max Python marks", command=max_Python_marks, font=button_font, bg=button_color, fg="black")
    max_button.pack(pady=10)
    max_button = tk.Button(max_window, text="Max Java marks", command=max_java_marks, font=button_font, bg=button_color, fg="black")
    max_button.pack(pady=10)
    max_button = tk.Button(max_window, text="Max Sql marks", command=max_sql_marks, font=button_font, bg=button_color, fg="black")
    max_button.pack(pady=10)

# Buttons in the main window
graph_button = tk.Button(root, text="Graph", command=graph, font=button_font, bg=button_color, fg="black")
graph_button.pack(pady=10)
details_button = tk.Button(root, text="Show Details", command=show_details, font=button_font, bg=button_color, fg="black")
details_button.pack(pady=10)

# Button to open the Max window
max_window_button = tk.Button(root, text="Max marks", command=open_max_window, font=button_font, bg=button_color, fg="black")
max_window_button.pack(pady=10)

root.mainloop()

