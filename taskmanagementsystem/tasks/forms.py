from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
  title = forms.CharField(
    label="Título",
    required=True,
    widget=forms.TextInput(attrs={"placeholder": "Título da Tarefa", "class": "form-control"})
  )
  description = forms.CharField(
    label="Descrição",
    required=False,
    widget=forms.Textarea(attrs={"placeholder": "Descrição da Tarefa", "class": "form-control"})
  )
  priority = forms.ChoiceField(
    label="Prioridade",
    choices=Task.Priority.choices,
    widget=forms.Select(attrs={"class": "form-select"})
  )
  due_date = forms.DateField(
    label="Data Limite",
    required=False,
    widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
  )

  is_completed = forms.BooleanField(
    label="Tarefa Concluída?",
    required=False,
    widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
  )

  class Meta:
    model = Task
    fields = ['title', 'description', 'priority', 'due_date', 'is_completed']

class RegisterForm(UserCreationForm):
  email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Endereço de Email"}))

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

  def __init__(self, *args, **kwargs):
    super(RegisterForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'Nome de Utilizador'
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório.</small></span>'
    self.fields['username'].label = ''

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>A palavra-passe tem de conter pelo menos 8 caracteres.</li><li>A password não pode ser de só números.</li><li>A password não pode ser parecida com o nome de utilizador.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Insira novamente a password.</small></span>'