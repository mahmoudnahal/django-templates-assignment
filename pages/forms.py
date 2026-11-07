from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'university_id', 'id_number', 'mobile',
                  'address', 'date_of_birth', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'university_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# طريقة أسرع لإضافة form-control: بتلف على كل الحقول وبتضيف الكلاس مرة وحدة،
# و *args, **kwargs بتمرر معامل الفورم (مثل request.POST) للكلاس الأب
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'