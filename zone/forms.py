# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class UploadForm (forms.Form):
  file = forms.FileField(label='Select photo to upload')

