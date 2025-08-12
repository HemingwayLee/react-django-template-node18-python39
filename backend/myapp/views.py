import uuid
import random
import decimal
from time import sleep
from django.http import JsonResponse
from django.db import connection
from .models import Person

def insert(request):
    for i in range(random.randint(10, 50)):
        sleep(decimal.Decimal(random.randrange(50, 300))/1000)

        p = Person(
            fname=uuid.uuid4().hex[:16], 
            lname=uuid.uuid4().hex[:16], 
            age=random.randint(10, 60))
        p.save()

    return JsonResponse({"result": "created!"})


def show(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM myapp_person;")
        data = cursor.fetchall()

    output = ""
    for p in data:
      output += str(p[0]) + " " + p[1] + " " + p[2] + "<br>"

    return JsonResponse({"result": output})
