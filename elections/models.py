from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.CharField(verbose_name="Country Name", max_length=80, blank=False, null=False)

    class Meta:
        verbose_name = ("Country")
        verbose_name_plural = ("Countries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Country_detail", kwargs={"pk": self.pk})


class ElectoralProfile(models.Model):

    numberOfVoters = models.IntegerField(verbose_name="Number of Voters", blank=False, null=False)
    abstentionLevel = models.IntegerField(verbose_name="Abstention Level", blank=False, null=False)
    ideologicalTrend = models.CharField(verbose_name="Ideological Trend", max_length=250, blank=False, null=False)
    electoralCenters = models.IntegerField(verbose_name="Electoral Centers", blank=False, null=False)
    countryID = models.ForeignKey(verbose_name="Country", to=Country, on_delete=models.CASCADE, blank=False, null=False)
    # lastThreeResultID = models.ForeignKey(verbose_name="Electoral Profile", to=, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = ("ElectoralProfile")
        verbose_name_plural = ("ElectoralProfiles")

    def get_absolute_url(self):
        return reversed("ElectoralProfile_detail", kwargs={"pk": self.pk})


class Election(models.Model):

    electoralProfileID = models.ForeignKey(verbose_name="Electoral Profile", to=ElectoralProfile, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = ("Election")
        verbose_name_plural = ("Elections")

    def __str__(self):
        return self.countryName

    def get_absolute_url(self):
        return reversed("Election_detail", kwargs={"pk": self.pk})


class MediaOutlet(models.Model):

    name = models.CharField(verbose_name="Name", max_length=150, blank=False, null=False)
    eletionID = models.ForeignKey(verbose_name="ElectionID", to=Election, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = ("MediaOutlet")
        verbose_name_plural = ("MediaOutlets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("MediaOutlet_detail", kwargs={"pk": self.pk})