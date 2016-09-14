from django import forms
from polls.models import Question


class QuestionCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionCreateForm, self).__init__(*args, **kwargs)

        self.fields["question_text"].required = True
        self.fields["pub_date"].required = True

    def save(self, *args, **kwargs):
        super(QuestionCreateForm, self).save(*args, **kwargs)

    class Meta:
        model = Question
        fields = ("question_text", "pub_date", )


class QuestionUpdateForm(QuestionCreateForm):
    pass
