from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['astro_sun', 'astro_moon', 'country']
        widgets = {
            'astro_sun': forms.Select(choices=[('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces')]),
            'astro_moon': forms.Select(choices=[('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces')]),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'})
        }