# coding=utf-8
import json

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, editable=False)

    parent = models.ForeignKey('self', null=True, default=None, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Category.objects.filter(parent=self):
            r = r + c.get_all_children(include_self=True)
        return r

    def has_descs(self):
        if len(self.description_set.all()) != 0:
            return True
        else:
            return False

    def get_parents(self):
        r = [self]
        if self.parent:
            r += self.parent.get_parents()
        return r

    def __unicode__(self):
        return self.name


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
    category = models.ForeignKey(Category, blank=True, null=True)
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
                        if word not in specwords:
                            specwords.append(word)
                pars.append(word.strip())

            if par_index != len(self.raw_body.split("\r\n\r\n")):
                pars.append("<br>")

        title = []
        for word in self.title.split(" "):
            if len(word) > 4:
                if word[-2:] == "$$" and word[:2] == "$$":
                    word = word[2:-2]
                    if word not in specwords:
                        specwords.append(word)
            title.append(word)

        self.body = json.dumps(pars)
        self.specialwords = json.dumps(specwords)

        self.title = " ".join(title)

        self.slug = "{}/{}".format(self.id, slugify(self.title))
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

    def get_body(self):
        return json.loads(self.body)

    def get_specwords(self):
        return json.loads(self.specialwords)

    def get_teaser(self):
        return json.loads(self.body)[0:30] + ["..."]

    def get_descs(self):
        sluglist = [slugify(word) for word in self.get_specwords()]
        for slug in self.get_specwords():
            print{slug}
        return Description.objects.filter(slug__in=sluglist)

    def __unicode__(self):
        return self.title


class Description(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=50, editable=False)

    category = models.ForeignKey(Category, null=True, default=None)
    articles = models.ManyToManyField(Article, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Description, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
