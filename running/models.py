from django.db import models

class Running(models.Model):
    name = models.CharField(max_length=100)
    picture_url = models.TextField()
    party_affiliation = models.TextField()
    campaign_website = models.TextField()
    social = models.TextField()
    quote = models.TextField()
    position = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.picture_url}, {self.party_affiliation}, {self.campaign_website}, {self.social}, {self.quote}, {self.position}'

class Users(models.Model):
    name= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    running = models.ManyToManyField(Running, related_name="favorited", blank = True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.address}'
