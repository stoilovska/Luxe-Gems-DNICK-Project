from django import forms

from LuxeGems.models import Jewelry, Payment, Registry, Login


class JewelryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JewelryForm,self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Jewelry
        exclude = ("user",)

class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm,self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Payment
        exclude = ("sum_price",)

class RegistryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegistryForm,self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Registry
        exclude = ("user",)

class LoginForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Login
        exclude = ("user",)

