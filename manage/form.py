from django.forms import ModelForm, ChoiceField
from models import Notice, UpdateList

national = (
    ('ww','ww'),
    ('ko','ko'),
    ('en','en'),
    ('jp','jp'),
    ('es','es'),
    ('zh','zh'),
    ('fr','fr'),
)

class NoticeForm(ModelForm):
    locale = ChoiceField(choices = national )

    class meta:
        model = Notice

class UpdateForm(ModelForm):
    locale = ChoiceField(choices = national )

    class meta:
        model = UpdateList