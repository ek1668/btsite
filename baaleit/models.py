from django.db import models
from datetime import datetime, date
from django.template.defaultfilters import slugify




# Create your models here.
# class Big5name(models.Model):
#   name = models.CharField(max_length=60)

# class Thebig5(models.Model):

#   name = models.CharField(max_length=60, default=None)
#   big5 = models.ManyToManyField(Big5name, through='Big5s')
#   # shabbat = models.CharField(max_length=60
#   # davening = models.CharField(max_length=60)
#   # kashrus = models.CharField(max_length=60)
#   # tefillin = models.CharField(max_length=60)
#   # taharas = models.CharField(max_length=60)

# class Big5s(models.Model):
#   big5thing = models.ForeignKey(Big5name, on_delete=models.CASCADE)
#   thebig5 = models.ForeignKey(Thebig5, on_delete=models.CASCADE)

class Thebig5(models.Model):
  nameChoices = (('Shabbat', 'shabbat'), ('Davening', 'davening'), ('Kashrus', 'kashrus'), ('Tefillin', 'tefillin'), ('Taharas Mishpacha', 'taharas mishpacha'))
  name = models.CharField(max_length=60, choices=nameChoices)
  namesub = models.CharField(max_length=60, default='Empty')
  link = models.URLField(max_length = 200, default='No Link')
  submenu = models.BooleanField(default=False)

  class Meta:
    verbose_name_plural = 'The Big 5'

  def __str__(self):
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
        return self.namesub

class Sublink(models.Model):
    nameChoices = (('Shabbat', 'shabbat'), ('Davening', 'davening'), ('Kashrus', 'kashrus'), ('Tefillin', 'tefillin'), ('Taharas Mishpacha', 'taharas mishpacha'))
    name = models.ForeignKey(Thebig5, on_delete=models.CASCADE)
    subItems = models.CharField(max_length=60, default='Empty')
    link = models.URLField(max_length = 200, default='No Link')

    class Meta:
      verbose_name_plural = 'Sub-link'

    def __str__(self):
        # return 'Sub-link: {} - {}'.format(self.name, self.subItems)
        return str(self.name)

class Community(models.Model):
  nameChoices = (('Kiruv', 'kiruv'), ('Synagogues', 'synagogues'), ('Calendars', 'calendars'), ('Campus Life', 'campus life'), ('Death and Bereavment', 'death and bereavment'))
  name = models.CharField(max_length=60, choices=nameChoices)
  namesub = models.CharField(max_length=60, default='Empty')
  link = models.URLField(max_length = 200, default='No Link')
  submenu = models.BooleanField(default=False)
  
  class Meta:
    verbose_name_plural = 'Community'

  def __str__(self):
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
        return self.namesub

class SublinkCommunity(models.Model):
    nameChoices = (('Kiruv', 'kiruv'), ('Synagogues', 'synagogues'), ('Calendars', 'calendars'), ('Campus Life', 'campus life'), ('Death and Bereavment', 'death and bereavment'))
    name = models.ForeignKey(Community, on_delete=models.CASCADE)
    subItems = models.CharField(max_length=60, default='Empty')
    link = models.URLField(max_length = 200, default='No Link')

    class Meta:
      verbose_name_plural = 'Sub-link Community'

    def __str__(self):
        # return 'Sub-link: {} - {}'.format(self.name, self.subItems)
        return str(self.name)

class Learning(models.Model):
  nameChoices = (('Shiurim', 'shiurim'), ('1-on-1 Connections', '1-on-1 connections'), ('Mailing List', 'mailing list'))
  name = models.CharField(max_length=60, choices=nameChoices)
  namesub = models.CharField(max_length=60, default='Empty')
  link = models.URLField(max_length = 200, default='No Link')
  submenu = models.BooleanField(default=False)
  
  class Meta:
    verbose_name_plural = 'Learning'

  def __str__(self):
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
        return self.namesub

class SublinkLearning(models.Model):
    nameChoices = (('Shiurim', 'shiurim'), ('1-on-1 Connections', '1-on-1 connections'), ('Mailing List', 'mailing list'))
    name = models.ForeignKey(Learning, on_delete=models.CASCADE)
    subItems = models.CharField(max_length=60, default='Empty')
    link = models.URLField(max_length = 200, default='No Link')

    class Meta:
      verbose_name_plural = 'Sub-link Learning'

    def __str__(self):
        # return 'Sub-link: {} - {}'.format(self.name, self.subItems)
        return str(self.name)

# class Learning(models.Model):
#   nameChoices = (('Shiurim', 'shiurim'), ('1-on-1 Connections', '1-on-1 connections'), ('Mailing List', 'mailing list'))
#   name = models.CharField(max_length=60, choices=nameChoices)
#   namesub = models.CharField(max_length=60, default='Empty')
#   link = models.URLField(max_length = 200, default='No Link')
#   submenu = models.BooleanField(default=False)
  
#   class Meta:
#     verbose_name_plural = 'Learning'

#   def __str__(self):
#         # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
#         return self.namesub

class Technology(models.Model):
  nameChoices = (('Useful Phone Apps', 'useful phone apps'), ('Connect With Family', 'connect with family'), ('Blogs', 'blogs'))
  name = models.CharField(max_length=60, choices=nameChoices)
  namesub = models.CharField(max_length=60, default='Empty')
  link = models.URLField(max_length = 200, default='No Link')
  submenu = models.BooleanField(default=False)
  
  class Meta:
    verbose_name_plural = 'Technology'

  def __str__(self):
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
        return self.namesub

class SublinkTechnology(models.Model):
    nameChoices = (('Useful Phone Apps', 'useful phone apps'), ('Connect With Family', 'connect with family'), ('Blogs', 'blogs'))
    name = models.ForeignKey(Technology, on_delete=models.CASCADE)
    subItems = models.CharField(max_length=60, default='Empty')
    link = models.URLField(max_length = 200, default='No Link')

    class Meta:
      verbose_name_plural = 'Sub-link Technology'

    def __str__(self):
        # return 'Sub-link: {} - {}'.format(self.name, self.subItems)
        return str(self.name)


class BT(models.Model):
  firstname = models.CharField(max_length=60)
  lastname = models.CharField(max_length=60)
  age = models.CharField(max_length=60, default='')
  email = models.EmailField(max_length = 254)
  phone_number = models.CharField(max_length=12)
  rstatus = models.CharField(max_length=60, default='')
  rbackground = models.CharField(max_length=60)
  location= models.CharField(max_length=60) 
  # age = models.CharField(max_length=60)

  
  class Meta:
      verbose_name_plural = 'BT Info(Personal Rabbi)'

  def __str__(self):
      #  dicts = dict()
      #  dicts = {'firstname':self.firstname, 'lastname': self.lastname}
  
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
       return "{} {}".format(self.firstname, self.lastname)

class BTone(models.Model):
  img = models.ImageField(upload_to='pics/')
  job = models.CharField(max_length=60)
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=300, null=True)

  class Meta:
      verbose_name_plural = 'BT One'

  def __str__(self):
      #  dicts = dict()
      #  dicts = {'firstname':self.firstname, 'lastname': self.lastname}
  
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
    return self.name

  def slug(self):
    return slugify(self.name)

class BTtwo(models.Model):
  img = models.ImageField(upload_to='pics/')
  job = models.CharField(max_length=60)
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=300, null=True)

  class Meta:
      verbose_name_plural = 'BT Two'

  def __str__(self):
      #  dicts = dict()
      #  dicts = {'firstname':self.firstname, 'lastname': self.lastname}
  
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
    return self.name

  def slug(self):
    return slugify(self.name)

class BTthree(models.Model):
  img = models.ImageField(upload_to='pics/')
  job = models.CharField(max_length=60)
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=300, null=True)

  class Meta:
      verbose_name_plural = 'BT Three'

  def __str__(self):
      #  dicts = dict()
      #  dicts = {'firstname':self.firstname, 'lastname': self.lastname}
  
        # return 'The Big 5: {} - {}'.format(self.name, self.namesub)
    return self.name

  def slug(self):
    return slugify(self.name)

class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=100000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

class BTOnePost(models.Model):
  img = models.ImageField(upload_to='pics/', default="C:\DjangoStuff\baaleiteshuva\baaleit\static\assets\img\reading.png")
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=1000000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  class Meta:
      verbose_name_plural = 'BT One Posts'

  def __str__(self):
    return self.title

class BTTwoPost(models.Model):
  img = models.ImageField(upload_to='pics/', default="C:\DjangoStuff\baaleiteshuva\baaleit\static\assets\img\reading.png")
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=1000000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  class Meta:
      verbose_name_plural = 'BT Two Posts'

  def __str__(self):
    return self.title

class BTThreePost(models.Model):
  img = models.ImageField(upload_to='pics/', default="C:\DjangoStuff\baaleiteshuva\baaleit\static\assets\img\reading.png")
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=1000000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  class Meta:
      verbose_name_plural = 'BT Three Posts'

  def __str__(self):
    return self.title