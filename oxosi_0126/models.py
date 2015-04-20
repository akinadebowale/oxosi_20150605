from __future__ import unicode_literals
from future.builtins import str
from future.utils import native

from io import BytesIO
import os
from string import punctuation
from zipfile import ZipFile

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
try:
    from django.utils.encoding import force_text
except ImportError:
    # Django < 1.5
    from django.utils.encoding import force_unicode as force_text
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable, RichText, Displayable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.importing import import_dotted_path
from mezzanine.utils.models import upload_to

class Block(Page, RichText):
    '''
    An individual block item in a grid.
    '''

    BLOCK_TYPE_CHOICES = (
        ('image', 'image'),
        ('video', 'video'),
        ('slider', 'slider'),
        ('text', 'txt'),
        ('html', 'html'),
    )

    BLOCK_RATIO_CHOICES = (
        ('block_ratio_11', '1:1'),
        ('block_ratio_21', '2:1'),
        ('block_ratio_22', '2:2'),
        ('block_ratio_23', '2:3'),
        ('block_ratio_41', '4:1'),
        ('block_ratio_42', '4:2'),
        ('block_ratio_43', '4:3'),
        ('block_ratio_44', '4:4'),
        ('block_ratio_45', '4:5'),
        ('block_ratio_46', '4:6'),
        ('block_ratio_63', '6:3'),
        ('block_ratio_64', '6:4'),
        ('block_ratio_66', '6:6'),
    )

    BLOCK_SLIDER_TRANSITION_TYPE_CHOICES = (
        ('cover', 'cover'),
        ('fade', 'fade'),
        ('fadeZoom', 'fadeZoom'),
        ('none', 'none'),
        ('scrollUp', 'scrollUp'),
        ('scrollDown', 'scrollDown'),
        ('scrollLeft', 'scrollLeft'),
        ('scrollRight', 'scrollRight'),
        ('uncover', 'uncover'),
    )

    BLOCK_VIDEO_AUTOSTART_CHOICES = (
        ('yes', 'yes'),
        ('no', 'no'),
    )

    BLOCK_HOVER_STAY_CHOICES = (
        ('yes', 'yes'),
        ('no', 'no'),
    )

    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("oxosi_0126.Block.featured_image", "blocks"),
        format="Image", max_length=255, null=True, blank=True)

    # block_slug = models.slug (use default slug)
    block_subtext = models.CharField(max_length=30, default="some subtext goes here")
    block_link = models.URLField()
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPE_CHOICES, default="image")
    block_ratio = models.CharField(max_length=15, choices=BLOCK_RATIO_CHOICES, default="block_ratio_22")
    block_slider_transition_type = models.CharField(max_length=20, choices=BLOCK_SLIDER_TRANSITION_TYPE_CHOICES, default="scrollLeft")
    block_slider_transition_speed = models.IntegerField(default="1000", help_text="in milliseconds so 1000 is 1 second")
    block_slider_transition_delay = models.IntegerField(default="2000", help_text="in milliseconds so 1000 is 1 second")
    # block_slider_gallery = gallery (use gallery function inherited from Gallery)
    block_custom_styles = models.CharField(max_length=200, help_text="like so: backround: #00000;")
    block_video_url = models.URLField()
    block_video_autostart = models.CharField(max_length=5, choices=BLOCK_VIDEO_AUTOSTART_CHOICES, default="no")
    block_text_font_styles = models.CharField(max_length=200, help_text="like so: font-size: 50px; line-height: 45px;")
    block_hover_stay = models.CharField(max_length=5, choices=BLOCK_HOVER_STAY_CHOICES, default="no")
    block_html_content = models.TextField(default="<div>HTML goes here</div>")

    categories = models.ManyToManyField("BlockCategory",
                                        verbose_name=_("Block Categories"),
                                        blank=True,
                                        related_name="blocks")

    class Meta:
        verbose_name = _("Block")
        verbose_name_plural = _("Blocks")
        ordering = ("-publish_date",)

class BlockImage(Orderable):
    '''
    An image(s) for a block (slider).
    '''
    block = models.ForeignKey(Block, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("oxosi_0126.BlockImage.file", "blocks"))

    class Meta:
        verbose_name = _("Block (Slider) Image")
        verbose_name_plural = _("Block Slider Images")

class BlockCategory(Slugged):
    """
    A category for grouping blocks into a series.
    """

    class Meta:
        verbose_name = _("Block Category")
        verbose_name_plural = _("Block Categories")
        ordering = ("title",)

