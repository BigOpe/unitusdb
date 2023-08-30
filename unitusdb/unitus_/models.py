from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate, get_language_info
from django.http import HttpResponse

def my_view(request):
    activate("it")

    li = get_language_info("it")

    response_content = f"Language: {li['name']} ({li['name_local']}) - Translated: {li['name_translated']} - Bidi: {li['bidi']}"
    return HttpResponse(response_content)

class Profile(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):return self.name


class User(models.Model):
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    CF= models.CharField(max_length=16, unique= True)
    email_p= models.EmailField(unique=True)
    email_u= models.EmailField(unique=True)
    department= models.IntegerField()
    profile= models.IntegerField()
    expired= models.BooleanField()

    def __str__(self):return f"{self.firstname} {self.lastname}"

class Department(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):return self.name

class Test(models.Model):
    ay=models.IntegerField()
    date=models.DateField()
    online=models.BooleanField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

class Macroaree(models.Model):
    name=models.CharField(max_length= 50)


    def __str__(self):return self.name

class Macroaree_test(models.Model):
    id_test = models.ForeignKey(Test, on_delete=models.CASCADE, default=1)  # Replace '1' with the desired default value
    id_macroaree = models.ForeignKey(Macroaree, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_macroaree)


class Availability(models.Model):
    id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    involved = models.BooleanField()
    rate = models.IntegerField()

    def __str__(self):
        return str(self.id_test)  # Return the string representation of id_test









# Create your models here.
