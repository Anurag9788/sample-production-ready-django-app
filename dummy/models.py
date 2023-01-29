"""Contains All the models of the app"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


"""Test Model to test functionality"""
class Test (models.Model):
    name = models.CharField(name='tets',max_length=255,unique=False,null=True)
    photo = models.ImageField(_("photo"), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("A time pass model")
        verbose_name_plural = _("Dummy-Model")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Test2(models.Model):
    count = models.IntegerField(_("Count"))
    largecount = models.ForeignKey(Test,related_name='test2',auto_created=True,db_index=True,on_delete=models.PROTECT)

    """ A meta class of the main class"""
    class Meta:
        verbose_name = _("Test2")
        verbose_name_plural = _("Test2s")

    def __str__(self):
        return str(self.count)

    def get_absolute_url(self):
        return reverse("Test2_detail", kwargs={"pk": self.pk})

