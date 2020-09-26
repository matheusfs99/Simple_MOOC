from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

    def send_mail(self, course):
        subject = '{} Contato'.format(course)
        message = 'Nome: {}; E-mail: {}; {}'.format(self.cleaned_data['name'],
                                                    self.cleaned_data['email'],
                                                    self.cleaned_data['message'])
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])