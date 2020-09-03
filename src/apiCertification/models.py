from django.db.models import (
    CASCADE,
    Model,
    CharField,
    DateField,
    ForeignKey,
    UUIDField
)
import uuid

# Create your models here.


class Certificate(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    certificate_serialnumber = CharField(max_length=255)
    issuer = CharField(max_length=255)
    certificate_type = CharField(max_length=255)
    date_issue = DateField(auto_now=False, auto_now_add=False)
    date_expire = DateField(auto_now=False, auto_now_add=False)


class CertificateConditions(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    certificate_uuid = ForeignKey(Certificate, on_delete=CASCADE)
    object_type = CharField(max_length=255)
    object_attribute = CharField(max_length=255)
    attribute_value = CharField(max_length=255)
