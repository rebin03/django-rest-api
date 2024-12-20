from django.db import models

# Create your models here.


class Lead(models.Model):

    source=models.CharField(max_length=200)
    name=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    course=models.CharField(max_length=200)

    STATUS_OPTONS=(
        ("open","open"),
        ("in-progress","in-progress"),
        ("pending","pending"),
        ("closed","closed")
    )

    status=models.CharField(max_length=100, choices=STATUS_OPTONS, default="open")
    remarks=models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name
