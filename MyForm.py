from django import forms


# creating a form
class InputForm(forms.Form):  # form class must be inherited from 'Form' class
    # 'form' is a key to your class 'InputForm'

    name = forms.CharField(max_length=200)
    python_marks = forms.IntegerField()
    java_marks = forms.IntegerField()
    sql_marks = forms.IntegerField()
