from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Program(models.Model):
    class Structure(models.TextChoices):
        parent = "parent", _("Parent")
        standalone = "standalone", _("Standalone")
        child = "child", _("Child")


    structure = models.CharField(max_length=16, choices=Structure.choices, default=Structure.standalone)
    description = models.TextField()
    title = models.CharField(max_length=128)
    slug = models.SlugField(allow_unicode=True, unique=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")