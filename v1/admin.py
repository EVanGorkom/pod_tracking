from django.contrib import admin
from django import forms
from .models.user_model import User
from .models.deck_model import Deck
from .models.card_model import Card
from .enums.color_enum import MtgColor


class CardAdminForm(forms.ModelForm):
    colors = forms.MultipleChoiceField(choices=MtgColor.choices(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Card
        fields = '__all__'

    def clean_colors(self):
        return ','.join(self.cleaned_data['colors'])

class DeckAdminForm(forms.ModelForm):
    colors = forms.MultipleChoiceField(choices=MtgColor.choices(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Deck
        fields = '__all__'

    def clean_colors(self):
        return ','.join(self.cleaned_data['colors'])

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    form = CardAdminForm

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    form = DeckAdminForm

admin.site.register(User)