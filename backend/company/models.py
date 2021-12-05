from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    logo = models.ImageField(upload_to='company_logo/',
                             blank=True, null=True, default='default.jpg')
    admin = models.ForeignKey("user.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('user.Profile', blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class JoinRequest(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    position = models.ForeignKey(
        'company.Position', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.company.name}-{self.user.username}'
