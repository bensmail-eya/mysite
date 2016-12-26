from django.db import models

# Create your models here.

class Question(models.Model):
      def _str_(self):
         return self.question_text
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')


class choice(models.Model):
      question = models.ForeignKey(Question)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
      def _str_(self):
        return self.choice_text
