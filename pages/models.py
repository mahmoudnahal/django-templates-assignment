from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=20, unique=True)
#عشان عدم ادخال قيمة سالبة وايضا  قيمة صغيرة لانها كافية بالنسبة للعمر ما في داعي استهلا ك مساحة اكبر دون داعي
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.FileField(upload_to='photos/')

    def __str__(self):
        return self.full_name