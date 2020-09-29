from django.db import models

class Running(models.Model):
    name = models.CharField(max_length=100)
    picture_url = models.TexField()
    party_affiliation = models.TextField()
    campaign_website = models.TextField()
    social = models.TextField()
    quote = models.TextField()
    position = models.TextField()
