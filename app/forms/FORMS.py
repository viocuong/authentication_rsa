from django import forms


class formLogin(forms.Form):
    email =forms.CharField(label = "Email", max_length=40, required=True,error_messages={'required':'khong duoc de trong'})
    passWord = forms.CharField(label= " Mật Khẩu", widget= forms.PasswordInput)
class formRegister(forms.Form):
    email = forms.CharField(label = 'Email',required=True, max_length=40)
    