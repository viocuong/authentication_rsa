from django import forms


class formLogin(forms.Form):
    email =forms.CharField(label = "Email", max_length=40, required=True,error_messages={'required':'khong duoc de trong'})
    passWord = forms.CharField(label= " Mật Khẩu", widget= forms.PasswordInput)
class formRegister(forms.Form):
    email = forms.CharField(label = 'Email',required=True, max_length=100,help_text='Email của bộ quốc phòng')
    #passWord = forms.CharField(label= 'Mật khẩu', widget= forms.PasswordInput,max_length=50)
    name = forms.CharField(label = 'Tên',max_length = 40,required=True)
    phone = forms.IntegerField(label = 'Số điện thoại')

    