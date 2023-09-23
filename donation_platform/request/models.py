from django.db import models
from donation_platform.models import MedicalEquipment, Donation, Volunteer, Conversation, Users, Event, Requests, AriclesZones, ArticlesStates, ArticlesType
from django.utils import timezone

class Requests(models.Model):
    req_name = models.CharField(max_length=50)
    zone = models.ForeignKey(ArticlesZones, models.DO_NOTHING, related_name='req_zone')
    req_description = models.TextField()
    accept_terms = models.BooleanField()
    user = models.ForeignKey(Users, models.DO_NOTHING, related_name='req_user')
    eq = models.ForeignKey(MedicalEquipment, models.DO_NOTHING, related_name='req_eq')
    don = models.ForeignKey(Donation, models.DO_NOTHING,  related_name='req_donation')
    vol = models.ForeignKey(Volunteer, models.DO_NOTHING, related_name='req_volunteer')
    req_sent_date = models.DateTimeField()
    has_confirmation = models.BooleanField()
    confirmed_at = models.DateTimeField(blank=True, null=True)
    state = models.ForeignKey(ArticlesStates, models.DO_NOTHING, related_name='req_state')
    type = models.ForeignKey(ArticlesType, models.DO_NOTHING, related_name='req_type')

    class Meta:
        managed = False
        db_table = 'requests'

