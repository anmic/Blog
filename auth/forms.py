from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span3'}),
        max_length=30, required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}),
        max_length=30, required=False)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}),
        max_length=30, required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'special'}),
        max_length=30, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'special'}),
        label="Password", min_length=6, max_length=32)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'special'}),
        label="Confirm password", min_length=6, max_length=32)

    def __unicode__(self):
        return "<Name: %r, Username: %r, Email: %r,Password : %r.>" % \
            (self.name, self.username, self.email, self.password)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}),
        max_length=30, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'special'}),
        label="Password", min_length=6, max_length=32)

    def __unicode__(self):
        return "<Username: %r, Password : %r.>" % \
            (self.username, self.password)
