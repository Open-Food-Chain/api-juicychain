from django.db.models import (
    Model,
    # AutoField,
    CASCADE,
    CharField,
    IntegerField,
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
    jds = IntegerField()
    jde = IntegerField()
    date_production_start = DateField()
    date_best_before = DateField()
    origin_country = CharField(max_length=255)
    organization = ForeignKey(
        Organization,
        related_name="batch",
        on_delete=CASCADE)


class Location(BaseWalletModel):
    name = CharField(max_length=255)
    organization = ForeignKey(
        Organization,
        related_name="location",
        on_delete=CASCADE)


class Certificate(Model):
    name = CharField(max_length=255)
    raddress = CharField(
        editable=True,
        null=True,
        blank=True,
        default='',
        max_length=34)
    pubkey = CharField(
        editable=True,
        null=True,
        blank=True,
        default='',
        max_length=66)
    date_issue = DateField()
    date_expiry = DateField()
    issuer = CharField(max_length=128)
    identifier = CharField(max_length=255)
    txid_funding = CharField(
        max_length=64,
        blank=True,
        null=True,
        editable=True)
    organization = ForeignKey(
        Organization,
        related_name="certificate",
        on_delete=CASCADE)

    def __str__(self):
        return self.name


class CertificateRule(BaseWalletModel):
    name = CharField(max_length=255)
    condition = CharField(max_length=255)
    certificate = ForeignKey(
        Certificate,
        null=True,
        blank=True,
        related_name="rule",
        on_delete=CASCADE)


class PoolPurchaseOrder(BaseWalletModel):
    organization = ForeignKey(Organization, on_delete=CASCADE)


class PoolBatch(BaseWalletModel):
    organization = ForeignKey(Organization, on_delete=CASCADE)
