from django.db import models


class Operation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, help_text="Name of the operation")

    def __str__(self):
        return self.name


class Reason(models.Model):
    class Type(models.TextChoices):
        SCRAP = 'S', 'scrap'
        REWORK = 'R','rework'

    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=60, help_text="Label that represents this reason")
    type = models.CharField(max_length=1, choices=Type.choices, help_text="What type of reason this is")
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="reasons", blank=True,null=True)

    def __str__(self):
        return self.text

