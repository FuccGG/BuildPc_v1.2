from django import forms
from . import functions_1
from .models import *


class CaseForm(forms.ModelForm):

    class Meta:
        model = PlayerAction
        fields = ('video_card', 'cpu', 'ram', 'hdd', 'ssd', 'mother_board', 'cooling', 'power_supply', 'budget','case_level')

    def save(self, commit=True):
        player_action = super(CaseForm, self).save(commit=False)
        if commit:
            player_action.save()
        return player_action

    def is_valid(self):
        return functions_1.general_check_logical(self)

