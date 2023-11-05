from django import forms

from .models import Order,Materials,Purpose
from department.models import Department,Course


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        options = (
            ('male', 'male'),
            ('female', 'female')
        )
        fields = ['name', 'dob', 'age', 'gender', 'phonenumber', 'mailid', 'address', 'deptname', 'course', 'purpose',
                  'materials']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['course'].queryset = Course.objects.none()

            if 'deptname' in self.data:
                try:
                    deptname_id = int(self.data.get('deptname'))
                    self.fields['course'].queryset = Course.objects.filter(deptname_id=deptname_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['course'].queryset = self.instance.deptname.course_set.order_by('name')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={"class":"form-control","type":"date"}),
            'age':forms.TextInput(attrs={"class":"form-control"}),
            'gender':forms.RadioSelect(attrs={"class":"form-control form-radioselect form-check-inline'"}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'mailid':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            # 'deptname':forms.Select(attrs={'class':'form-control'}),
            # 'cname':forms.Select(attrs={'class':'form-control'}),
            'purpose':forms.Select(attrs={'class':'form-control'}),
            'materials':forms.CheckboxSelectMultiple(attrs={'class':'form-check-input '})
        }




