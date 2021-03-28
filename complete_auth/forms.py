from django.contrib.auth import get_user_model
from django import forms

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password(self):
        password1 = self.cleaned_data('password1')
        password2 = self.cleaned_data('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return password2

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.set_password(self.cleaned_data)
            customer = self.cleaned_data('username')