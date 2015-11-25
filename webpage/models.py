# coding=utf-8
import json

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Ressort(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Ressort, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    ressort = models.ForeignKey(Ressort)
    author = models.CharField(max_length=50, null=True)

    title = models.CharField('Titel', max_length=100)
    subtitle = models.TextField('Untertitel', null=True, blank=True)

    specialwords = models.TextField('Spezialwörter', null=True, blank=True)
    raw_body = models.TextField()
    body = models.TextField('Inhalt', editable=False)
    created = models.DateTimeField(editable=False)

    slug = models.SlugField(max_length=80, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        super(Article, self).save(*args, **kwargs)

        pars = []
        specwords = []
        for par_index, par in enumerate(self.raw_body.split("\r\n\r\n")):
            for word in par.split(" "):
                if len(word) > 4:
                    if word[-2:] == "$$" and word[:2] == "$$":
                        word = word[2:-2]
                        specwords.append(word.strip())
                pars.append(word.strip())

            if par_index != len(self.raw_body.split("\r\n\r\n")):
                pars.append("<br>")

        title = []
        for word in self.title.split(" "):
            if len(word) > 4:
                if word[-2:] == "$$" and word[:2] == "$$":
                    word = word[2:-2]
                    specwords.append(word)
            title.append(word)

        self.body = json.dumps(pars)
        self.specialwords = json.dumps(specwords)

        self.title = " ".join(title)

        self.slug = "{}/{}".format(self.id, slugify(self.title))
        return super(Article, self).save(*args, **kwargs)

    def get_body(self):
        return json.loads(self.body)

    def get_specwords(self):
        return json.loads(self.specialwords)

    def __unicode__(self):
        return self.title


class Description(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Description, self).save(*args, **kwargs)
