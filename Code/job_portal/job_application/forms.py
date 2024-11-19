from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    linkedin_password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        label="Re-enter LinkedIn Password",
        required=True
    )

    class Meta:
        model = JobApplication
        fields = [ ]
        widgets = {
            'linkedin_password_encrypted': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("linkedin_password_encrypted")
        confirm_password = cleaned_data.get("linkedin_password_confirm")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
        return cleaned_data
