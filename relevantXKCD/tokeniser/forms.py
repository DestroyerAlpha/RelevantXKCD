from django.forms import ModelForm
from .models import Input
from .tokeniser import get_keywords
import json

class InputForm(ModelForm):
    '''
        Landing Page Form
    '''
    class Meta:
        model = Input
        fields = ['input_text']
    
    def save(self, commit=True):
        entry = super(InputForm, self).save(commit=False)
        entry.input_text = self.cleaned_data['input_text']
        entry.tokenised_text = json.dumps(get_keywords(entry.input_text))
        # print(entry.tokenised_text)
        if commit:
            entry.save()
        
        return entry
