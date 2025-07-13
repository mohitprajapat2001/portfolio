from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cities_light.models import City, Region, Country
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


def _profile_picture(self, filename):
    """
    Returns a string representing the file path where the
    profile picture is to be uploaded.

    :param self: The Profile object
    :param filename: The filename of the profile picture
    :return: The file path where the profile picture is to be
             uploaded
    """
    return "profile_pictures/%s/%s" % (self.full_name, filename)


def _upload_resumes(self, filename):
    """
    Returns a string representing the file path where the
    resume is to be uploaded.

    :param self: The Profile object
    :param filename: The filename of the resume
    :return: The file path where the resume is to be
             uploaded
    """
    return "resumes/%s/%s" % (self.profile.full_name, filename)


class Profile(TimeStampedModel):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = PhoneNumberField(region="IN", verbose_name="Phone Number")
    profile_picture = models.ImageField(
        upload_to=_profile_picture, verbose_name="Profile Picture"
    )

    @property
    def full_name(self):
        """
        Returns the full name of the profile.

        Returns:
            str: The full name of the profile.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Returns the full name of the profile as the string representation of the object.

        Returns:
            str: The full name of the profile.
        """
        return self.full_name


class Address(TimeStampedModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="addresses"
    )
    street_address = models.CharField(max_length=100, verbose_name="Street Address")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="addresses")
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, related_name="addresses"
    )
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="addresses"
    )
    postal_code = models.IntegerField(verbose_name="Postal Code", blank=True, null=True)

    def __str__(self):
        """
        Returns the street address of the address as the string representation of the object.

        Returns:
            str: The street address of the address.
        """
        return self.street_address


class Resume(TitleDescriptionModel, TimeStampedModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="resumes"
    )
    file = models.FileField(upload_to=_upload_resumes, verbose_name="Resume File")
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns the title of the resume as the string representation of the object.

        Returns:
            str: The title of the resume.
        """
        return self.title


class Skills(TimeStampedModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="skills"
    )
    name = models.CharField(max_length=100, verbose_name="Skill")

    def __str__(self):
        """
        Returns the skill as the string representation of the object.

        Returns:
            str: The skill.
        """
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self):
        """
        Returns the name of the technology as the string representation of the object.

        Returns:
            str: The name of the technology.
        """
        return self.name


class Project(TitleDescriptionModel, TimeStampedModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="projects"
    )
    image = models.ImageField(upload_to="projects", verbose_name="Image")
    live_url = models.URLField(verbose_name="Live URL")
    source_url = models.URLField(verbose_name="Source URL")
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        """
        Returns the title of the project as the string representation of the object.

        Returns:
            str: The title of the project.
        """
        return self.title


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(verbose_name="Description")
    is_current = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns the role of the experience as the string representation of the object.

        Returns:
            str: The role of the experience.
        """
        return self.role


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        """
        Returns the name of the contact message as the string representation of the object.

        Returns:
            str: The name of the contact message.
        """
        return self.name

    class Meta:
        ordering = ["-created"]
