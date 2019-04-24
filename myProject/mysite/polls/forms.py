from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from .models import Poll, Question, Choice


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s ไม่ใช่เลขคู่', params={'value':value})

class PollForm(forms.Form):
    title = forms.CharField(label="ชื่อโพล",max_length=100, required=True)
    email = forms.CharField(label="อีเมล",validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="จำนวนคำถาม", min_value=0, max_value=10, required=True, validators=[validate_even])
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def clean_title(self):
        data = self.cleaned_data['title']

        if 'IT Panda' not in data:
            raise forms.ValidationError('You forgot IT Panda!')
        return data
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError('โปรดเลือกวันสิ้นสุด')
            self.add_error('end_date', 'โปรดเลือกวันสิ้นสุด')
        elif end and not start:
            # raise forms.ValidationError('โปรดเลือกวันเริ่ม')
            self.add_error('start_date', 'โปรดเลือกวันเริ่ม')

class PollModelForm(forms.ModelForm):

    def clean_title(self):
        data = self.cleaned_data['title']

        if 'IT Panda' not in data:
            raise forms.ValidationError('You forgot IT Panda!')
        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError('โปรดเลือกวันสิ้นสุด')
            self.add_error('end_date', 'โปรดเลือกวันสิ้นสุด')
        elif end and not start:
            # raise forms.ValidationError('โปรดเลือกวันเริ่ม')
            self.add_error('start_date', 'โปรดเลือกวันเริ่ม')
    class Meta:
        model = Poll
        exclude = ['del_flag']


class QuestionForm(forms.Form):
    question_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    text = forms.CharField()
    type = forms.ChoiceField(choices=Question.TYPES, initial='01', required=False)

class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'