from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

