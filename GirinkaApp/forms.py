from django import forms

from .models import Announcements

# Create your forms here.
class AnnounceForm(forms.ModelForm):
	class Meta:
		model = Announcements
		fields=('title','published_date','expired_date','location','posted_by','attachment')

