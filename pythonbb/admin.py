from django.contrib import admin
from pythonbb.models import Forum, Thread, Message

models = [Forum,Thread,Message]

for model in models :
    admin.site.register(model)