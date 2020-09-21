from django.db.models import (
    Model,
    # AutoField,
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    # OneToOneField,
    # UUIDField
)
# import uuid


class BaseWalletModel(Model):
    # TODO when working come back to test this with drf
    # id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    raddress = CharField(
        editable=False,
        unique=True,
        max_length=34)
    pubkey = CharField(
        editable=False,
        unique=True,
        max_length=66)

    class Meta:
        abstract = True

    def __str__(self):
        return self.raddress


class Organization(BaseWalletModel):
    name = CharField(max_length=255)


class Batch(BaseWalletModel):
    identifier = CharField(max_length=255)
    date_production_start = DateField()
    date_best_before = DateField()
    origin_country = CharField(max_length=255)
    organization = ForeignKey(Organization, on_delete=CASCADE)


class Location(BaseWalletModel):
    name = CharField(max_length=255)
    organization = ForeignKey(
        Organization,
        related_name="location",
        on_delete=CASCADE)


class Certificate(BaseWalletModel):
    name = CharField(max_length=255)
    date_issue = DateField()
    date_expiry = DateField()
    issuer = CharField(max_length=128)
    identifier = CharField(max_length=255)
    organization = ForeignKey(
        Organization,
        related_name="certificate",
        on_delete=CASCADE)


class CertificateRule(BaseWalletModel):
    name = CharField(max_length=255)
    rule = CharField(max_length=255)
    certificate = ForeignKey(
        Certificate,
        related_name="rules",
        on_delete=CASCADE)


class PoolPurchaseOrder(BaseWalletModel):
    organization = ForeignKey(Organization, on_delete=CASCADE)


class PoolBatch(BaseWalletModel):
    organization = ForeignKey(Organization, on_delete=CASCADE)
