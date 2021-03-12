from django.db import models
from django.urls import reverse

STATUS_LIST = [
    ("payment pending", "payment pending"),
    ("searching", "searching"),
    ("printed", "printed"),
    ("stamped", "stamped"),
    ("delivered", "delivered"),
]


class Store(models.Model):
    status = models.CharField(
        max_length=25, choices=STATUS_LIST, default="payment pending"
    )
    number = models.CharField(max_length=3, null=True)
    block = models.CharField(max_length=20, null=True)
    parcel = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["number"]

    def mark_as_paid(self):
        return reverse("store:mark-as-paid", args=[str(self.pk)])

    def mark_as_printed(self):
        return reverse("store:mark-as-printed", args=[str(self.pk)])

    def mark_as_stamped(self):
        return reverse("store:mark-as-stamped", args=[str(self.pk)])

    def mark_as_delivered(self):
        return reverse("store:mark-as-delivered", args=[str(self.pk)])

    def __str__(self):
        return str(self.number)
