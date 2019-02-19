from django import forms


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    # parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 5}))
