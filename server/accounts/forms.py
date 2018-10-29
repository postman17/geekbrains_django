from django import forms


class AccountUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_pass'}
        )
    )