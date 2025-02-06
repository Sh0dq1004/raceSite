from django import forms
from .models import Person

class TestForm(forms.Form):
    name = forms.CharField(label='名前')

class BettingForm(forms.Form):
    CHOICE={
        (0,'しょうた'),
        (1,'たいが'),
        (2,'たくみ'),
        (3,'そら')
    }
    select=forms.ChoiceField(label='ターゲット', widget=forms.RadioSelect,choices=CHOICE,initial=0)
    bet_money=forms.IntegerField(label='掛け金を入力してください',)

class AnswerForm(forms.Form):
    CHOICE={
        (0,'しょうた'),
        (1,'たいが'),
        (2,'たくみ'),
        (3,'そら')
    }
    select=forms.ChoiceField(label='答え', widget=forms.RadioSelect,choices=CHOICE,initial=0)