from django.db import models

class Activity(models.Model):
    """GooglePlus activity."""
    objtype = models.CharField("type", max_length=64)
    content = models.TextField("HTML content")
    url = models.CharField("google+ url", max_length=250)
    published = models.DateTimeField("date published")
    
    def __unicode__(self):
        return self.objtype + " activity"
    
    class Meta:
        verbose_name_plural = "activities"


class Attachment(models.Model):
    """Attachments to GooglePlus activities."""
    objtype = models.CharField("type", max_length=64)
    title = models.CharField(max_length=250)
    content = models.TextField("HTML content")
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    activity = models.ForeignKey(Activity)
    
    def __unicode__(self):
        return self.objtype + " attachment"
