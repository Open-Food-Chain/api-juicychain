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
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)


class Walletaddress(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55, unique=True)


class Transactionid(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    txid = CharField(max_length=70, unique=True)


class Organization(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE, primary_key=True)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Batchdetail(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE, primary_key=True)
#  txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Facility(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE, primary_key=True)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)


class Certification(Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
#   wallet = ForeignKey(Walletaddress, on_delete=CASCADE)
    wallet = OneToOneField(Walletaddress, on_delete=CASCADE, primary_key=True)
    txid = ForeignKey(Transactionid, on_delete=CASCADE)


# class Productjourney(Model):
#    product = ForeignKey(Product, on_delete=CASCADE)
#    organization = ForeignKey(Organization, on_delete=CASCADE)
#    batchdetail = ForeignKey(Batchdetail, on_delete=CASCADE)
#    facility = ForeignKey(Facility, on_delete=CASCADE)
#    certification = ForeignKey(Certification, on_delete=CASCADE)
