from django.db import models
from datetime import datetime

class Artiste(models.Model):
   
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField(default=1)
    song=models.ForeignKey('Song', null=True, blank=True,on_delete =models.CASCADE )
    def __str__(self):
        return f'{self.first_name}{self.last_name}'
class Song(models.Model):
    artiste_id=models.CharField(max_length=20)
    title = models.CharField(max_length=400)
    date_released = models.DateTimeField(auto_now_add=True)
    likes =models.PositiveIntegerField(default=0)
    lyric = models.ForeignKey('Lyric', null=True, blank=True,on_delete =models.SET_NULL )
                                
    def __str__(self):
        return self.title                         
class Lyric(models.Model):
    song_id = models.CharField(max_length=20)
    content =models.CharField(max_length=400)
        
    def __str__(self):
            return self.content



