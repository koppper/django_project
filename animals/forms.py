from django import forms


class Animals(forms.Form):
    name = forms.CharField(max_length=100, min_length=5, strip=True)
    people = forms.ChoiceField(choices=((1, "Tom"), (2, "Bob"), (3, "Нет хозяина")))
    image = forms.ImageField()
    price = forms.DecimalField(max_value=1000000, min_value=1000, decimal_places=2)


class People(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=2)
    last_name = forms.CharField(max_length=100, min_length=2)
    email = forms.EmailField()
    age = forms.IntegerField()
    animal = forms.ChoiceField(choices=((1, "SD"), (2, "EWQ"), (3, "POP")))
    slug = forms.SlugField()
    pw = forms.CharField(widget=forms.PasswordInput)
    file = forms.FileField()
