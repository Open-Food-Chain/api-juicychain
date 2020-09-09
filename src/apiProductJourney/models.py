from django.db.models import (
    Model,
    CASCADE,
    CharField,
    # DateField,
    ForeignKey,
    OneToOneField,
    UUIDField
)
import uuid


class Product(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)


class Walletaddress(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55, unique=True)


class Transactionid(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    txid = CharField(max_length=70, unique=True)


class Organization(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Batchdetail(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE)
#  txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Facility(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Certification(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)
