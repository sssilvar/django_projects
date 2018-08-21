from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        if len(self.description) > 100:
            return self.description[:100] + '...'
        else:
            return self.description

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
