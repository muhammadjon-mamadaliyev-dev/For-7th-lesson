from django import forms
from .models import ToDo

class ToDoModelForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description']

# class ToDoForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     description = forms.CharField()

    
# def clean_title(self):
#     title = self.cleaned_data["title"]
#     print("title : ", title)
#     if not title.startswith("a"):
#         raise forms.ValidationError("Ism a bilan boshnishi kere")
#     return title


# def clean(self):
#     cleaned_data = super.clean()
    
#     if cleaned_data["startdate"] > cleaned_data["enddate"]:
#         raise forms.ValidationError("Akam jinnimisz tugedigan kundan boshlanedigan kun kichik boladimi?")
#     return cleaned_data


