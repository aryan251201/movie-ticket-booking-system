from django.db import models

# Create your models here.
class Movie(models.Model):
    name= models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.theater.name} - {self.name}"
    
class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    row= models.CharField(max_length=5)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.screen.name} - Row {self.row} Seat {self.number}"
    
class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.name} at {self.start_time} in {self.screen.name}"
    

class ShowSeat(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('locked', 'Locked'),
    ]
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    locked_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('show', 'seat')
    def __str__(self):
        return f"{self.show} - {self.seat} ({self.status})"