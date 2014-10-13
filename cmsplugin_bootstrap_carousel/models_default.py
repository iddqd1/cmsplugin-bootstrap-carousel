# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin
from PIL import Image
from cStringIO import StringIO
from filebrowser.fields import FileBrowseField

DEF_SIZE = (800, 600)
        
class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    interval = models.IntegerField(default=5000)
    
    def copy_relations(self, oldinstance):
        for item in oldinstance.carouselitem_set.all():
            item.pk = None
            item.carousel = self
            item.save()
    
    def __unicode__(self):
        return self.domid

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    image = FileBrowseField("Picture", max_length=200, directory="uploads/", extensions=[".jpg", ".png"], blank=True, null=True)

