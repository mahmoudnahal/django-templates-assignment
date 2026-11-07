from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator


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



#كان بانكاني اعمل عملية التحقق عن طريق دوال لكن هين الطريقة الي بتوفرها بايثون اسرع وبتغني عن بناء دوال من الصفر

class Student(models.Model):
    # الاسم: بيقبل حروف إنجليزي وعربي ومسافات بس، يعني لو فيه رقم أو رمز بيطلع خطأ
    name = models.CharField(
        "Full Name", max_length=100,
        validators=[RegexValidator(r'^[A-Za-z\u0600-\u06FF ]+$',
                    'Name must contain letters only (no numbers or symbols).')],
    )

    # الرقم الجامعي: لازم يكون 9 أرقام وأولها 1 أو 2، وما بيتكرر (unique) وإذا تكرر بتطلع رسالتك
    university_id = models.IntegerField(
        "University ID", unique=True,
        validators=[RegexValidator(r'^[12]\d{8}$',
                                   'Must be 9 digits and start with 1 or 2.',
                                   code='invalid_university_id')],
        error_messages={'unique': 'This University ID is already registered.'},
    )

    # رقم الهوية: لازم 9 أرقام وأولها 9 أو 8 أو 4
    id_number = models.IntegerField(
        "ID Number",
        validators=[RegexValidator(r'^[984]\d{8}$',
                                   'Must be 9 digits and start with 9, 8, or 4.',
                                   code='invalid_id_number')],
    )

    # الموبايل: لازم 10 أرقام وبيبدأ بـ 059 أو 056
    mobile = models.CharField(
        "Mobile Number", max_length=10,
        validators=[RegexValidator(r'^(059|056)\d{7}$',
                    'Must be 10 digits and start with 059 or 056.')],
    )

    # العنوان: نص عادي ما بيزيد عن 150 حرف (الحد من max_length)
    address = models.CharField("Address", max_length=150)

    # تاريخ الميلاد: تاريخ عادي بدون شروط إضافية
    date_of_birth = models.DateField("Date of Birth")

    # الصورة: بتنرفع لمجلد students، وبتقبل بس امتداد jpg أو png
    image = models.ImageField(
        "Image", upload_to='students/',
        validators=[FileExtensionValidator(['jpg', 'png'],
                    'Only jpg or png images are allowed.')],
    )


    def __str__(self):
        return self.name