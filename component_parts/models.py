from django.db import models
# Create your models here.


class VideoCard(models.Model):
    name = models.CharField(max_length=100)
    clock_frequency = models.IntegerField()
    video_memory = models.IntegerField()
    socket = models.CharField(max_length=100)
    power = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Processor(models.Model):
    name = models.CharField(max_length=100)
    clock_frequency = models.IntegerField()
    socket = models.CharField(max_length=100)
    cores = models.IntegerField()
    tdp = models.IntegerField()
    memory_type = models.CharField(max_length=100)
    power = models.IntegerField()
    max_memory_volume = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=100)
    clock_frequency = models.IntegerField()
    memory_type = models.CharField(max_length=100)
    amount_of_memory = models.IntegerField()
    power = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class HDD(models.Model):
    name = models.CharField(max_length=100)
    amount_of_memory = models.IntegerField()
    cache_size = models.IntegerField()
    power = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class SSD(models.Model):
    name = models.CharField(max_length=100)
    amount_of_memory = models.IntegerField()
    interface = models.CharField(max_length=100)
    power = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class MotherBoard(models.Model):
    name = models.CharField(max_length=100)
    cpu_socket = models.CharField(max_length=100)
    graphics_card_socket = models.CharField(max_length=100)
    # form_factor = models.CharField(max_length=25)
    interface = models.CharField(max_length=100)
    memory_slot_count = models.IntegerField(default=1)
    power = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Cooling(models.Model):
    name = models.CharField(max_length=100)
    supported_socket = models.CharField(max_length=400)
    dissipated_tdp = models.IntegerField()
    power = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class PowerSupply(models.Model):
    name = models.CharField(max_length=100)
    power = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    case_level = models.IntegerField()
    video_card = models.ForeignKey(VideoCard, on_delete=models.CASCADE, blank=True, null=True)
    cpu = models.ForeignKey(Processor, on_delete=models.CASCADE, blank=True, null=True)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, blank=True, null=True)
    hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, blank=True, null=True)
    ssd = models.ForeignKey(SSD, on_delete=models.CASCADE, blank=True, null=True)
    mother_board = models.ForeignKey(MotherBoard, on_delete=models.CASCADE, blank=True, null=True)
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE, blank=True, null=True)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, blank=True, null=True)
    case_text = models.CharField(max_length=1000)
    tips = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


class PlayerAction(models.Model):
    budget = models.IntegerField()
    case_level = models.IntegerField()
    video_card = models.ForeignKey(VideoCard, on_delete=models.CASCADE, blank=True, null=True)
    cpu = models.ForeignKey(Processor, on_delete=models.CASCADE, blank=True, null=True)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, blank=True, null=True)
    hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, blank=True, null=True)
    ssd = models.ForeignKey(SSD, on_delete=models.CASCADE, blank=True, null=True)
    mother_board = models.ForeignKey(MotherBoard, on_delete=models.CASCADE, blank=True, null=True)
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE, blank=True, null=True)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, blank=True, null=True)




