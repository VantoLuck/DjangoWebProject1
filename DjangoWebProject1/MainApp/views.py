from django.shortcuts import render

def index(request):
    return render(request,'MainApp/homepage.html')

def contact(request):
    return render(request,'MainApp/basic.html', {'values': ['Если у вас остались вопросы, то можете их не задавать по этому номеру','8-(916)-901-20-30','example@mail.ru','Chlen']})
