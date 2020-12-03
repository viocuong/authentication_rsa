from django import forms


class formLogin(forms.Form):
    key = forms.CharField(label = "Key", max_length=500,required=True)
class formRegister(forms.Form):
    email = forms.CharField(label = 'Email',required=True, max_length=100,help_text='Email của bộ quốc phòng')
    #passWord = forms.CharField(label= 'Mật khẩu', widget= forms.PasswordInput,max_length=50)
    name = forms.CharField(label = 'Tên',max_length = 40,required=True)
    phone = forms.IntegerField(label = 'Số điện thoại')

    