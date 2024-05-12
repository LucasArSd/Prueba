from django.db import models

#acá es donde creo los modelos de las bases de datos, si eso

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


#pruebas

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self): #Por si quiero hacer un print a una instancia Usuario
        return self.nombre