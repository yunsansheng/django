from django.db import models

# Create your models here.
class Artical(models.Model):
	title = models.CharField(max_length=200)
	sourcefrom=models.CharField(max_length=60)
	source_topic=models.CharField(max_length=60)

	topic_no= models.IntegerField(default=0)
	question_no= models.IntegerField(default=0)
	best_answer_no=models.IntegerField(default=0)
	answerCount=models.IntegerField(default=0)
	vote=models.IntegerField(default=0)

	lable=models.TextField(null=True)
	def com_url(self):
		if self.sourcefrom=="知乎话题":
			return "https://www.zhihu.com/question/{question_no}/answer/{best_answer_no}".format(question_no=self.question_no,best_answer_no=self.best_answer_no)
		else:
			return "404"