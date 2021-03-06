from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from enumfields import EnumField
from sorl.thumbnail import ImageField

from content.models import Content
from taxonomy.models import Term
from team.models import Team
# Create your models here.
from web import settings


def campaign_image_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s/%s" % (x.year, x.month, x.day, filename)


class CampaignType(Enum):
    WORK_OLD = "WORK"
    MENTORING_OLD = "MENTORING"
    STUDY_OLD = "STUDY"
    SALES_OLD = "SALES"
    WORKSHOP_OLD = "WORKSHOP"
    PRESENTATION_OLD = "PRESENTATION"
    EVENT_OLD = "EVENT"
    MENTORING = "mentoring"
    STUDY = "study"
    SALES = "sales"
    WORKSHOP = "workshop"
    PRESENTATION = "presentation"
    EVENT = "event"


class Campaign(models.Model):  # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=10000)

    type = EnumField(CampaignType, max_length=1000)


    slug = models.SlugField(blank=True, null=True)
    # application = models.ForeignKey(Application, default=1, null=True, on_delete=models.CASCADE)
    image = ImageField(upload_to=campaign_image_upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")

    banner_image = models.ImageField(upload_to=campaign_image_upload_location,
                                     null=True,
                                     blank=True,
                                     width_field="banner_width_field",
                                     height_field="banner_height_field")

    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    banner_width_field = models.IntegerField(default=0)
    banner_height_field = models.IntegerField(default=0)
    description = models.TextField()

    start_time = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    duration_days = models.IntegerField(blank=True, null=True)

    @property
    def name(self):
        return self.title

    def __str__(self):
        return self.name


    class Meta:
        unique_together = ("slug", "type")


class CampaignPartyRelationType(Enum):  # A subclass of Enum
    CREATOR = "CREATOR"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"


class CampaignPartyRelation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    # party
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # type = models.CharField(
    #     max_length=30,
    #     choices=[(tag.value, tag.name) for tag in CampaignPartyRelationType]
    # )

    type = EnumField(CampaignPartyRelationType, max_length=1000)

    def __str__(self):
        return str(self.content_object) + " | " + self.campaign.title


class CampaignContentRelationType(Enum):  # A subclass of Enum
    CREATED_ON = "CREATED_ON"


class CampaignContentRelation(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='rel_campaign', on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='rel_content', on_delete=models.CASCADE)
    type = EnumField(CampaignContentRelationType, default=CampaignContentRelationType.CREATED_ON, max_length=1000)

    def __str__(self):
        return str(self.content) + " | " + self.campaign.title


class CampaignTermRealtionType(Enum):
    SUBJECT = "SUBJECT"


class CampaignTermRelation(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='campaign', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='term', on_delete=models.CASCADE)

    # type = models.CharField(
    #     max_length=30,
    #     choices=[(tag.value, tag.name) for tag in CampaignTermRealtionType]
    # )

    type = EnumField(CampaignTermRealtionType, max_length=1000)


class CampaignEnrollmentRequest(models.Model):
    # TODO: convert to profile
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='request_campaign', on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)


# Sales Campaign

class Product(models.Model):
    seller = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, related_name="seller")
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
