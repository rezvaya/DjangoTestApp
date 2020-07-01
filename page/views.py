from django.shortcuts import render
from .models import Row
import requests
import json
import datetime

# Функция для проверки данных на сайте налоговой
def check_inn_ogrn(number):
    datas ={
        'query':number
    }
    r = requests.post('https://rmsp.nalog.ru/search-proc.json', data=datas).json()
    
    if (r["data"] == []):
        return False
    else:
        return True


def post_list(request):
    form = ""
    errors = []
    rows =[]    
    answ = ''

    if request.POST:        
        form = request.POST.get('inn')
        rows = Row.objects.all()
    # Проверка введенных данных
        if not form:
            errors.append('Введите ИНН или ОГРН')
        else:            
            if ((len(form) > 15) or (len(form) < 10)): 
                errors.append('Недопустимая длина')   
            if not form.isdigit():
                errors.append('Недопустимые символы')  
    # Работа с базой данных
        if not errors:
            if not (Row.objects.filter(value=form)):
                answ = str(check_inn_ogrn(int(form)))
                row = Row()
                row.value = form
                row.time = datetime.datetime.now()
                row.value_type = answ
                row.save()
            else:
                answ = Row.objects.get(value=form).value_type
                
    return render(request, 'page/page.html', {'errors': errors, 'form':form, 'answ': answ, 'rows':rows})

