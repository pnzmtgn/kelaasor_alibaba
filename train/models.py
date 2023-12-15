from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=11, )
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name

class Train(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name = "train_station")
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Kelaasor Train"
