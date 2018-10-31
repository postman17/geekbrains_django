from django import forms


class AccountUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_pass'}
        )
    )

class RegisterUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(
        label='Password',
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_pass'}
        )
    )