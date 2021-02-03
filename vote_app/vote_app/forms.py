from django import forms

CHOICES = [
    ('Apple', 'Apple'), ('Mango', 'Mango')
]

class VoteForm(forms.Form):
    
    fruit = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def validate_input(self, fruit):
        for fruits in CHOICES:
            if fruit == fruits[0]:
                return True
        return False
