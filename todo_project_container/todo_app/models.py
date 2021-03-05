from django.db import models
from datetime import datetime


class Todos(models.Model):
      title = models.CharField(max_length =100)
      description = models.TextField(blank = True, max_length=2500)
      finished = models.BooleanField(default = False)
      date = models.DateTimeField(default = datetime.now ,blank = True)


      def __str__(self):
            return self.title