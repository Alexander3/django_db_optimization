from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    updated = models.DateTimeField(editable=False, auto_now=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # append `updated` to update_fields if we save some of the fields in an object
        update_fields = kwargs.get("update_fields")
        if update_fields:
            kwargs.update(update_fields=list(update_fields) + ["updated"])
        super().save(*args, **kwargs)


class Manager(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    address = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    # region random fields
    some_random_field0 = models.CharField(max_length=100)
    some_random_field1 = models.CharField(max_length=100)
    some_random_field2 = models.CharField(max_length=100)
    some_random_field3 = models.CharField(max_length=100)
    some_random_field4 = models.CharField(max_length=100)
    some_random_field5 = models.CharField(max_length=100)
    some_random_field6 = models.CharField(max_length=100)
    some_random_field7 = models.CharField(max_length=100)
    some_random_field8 = models.CharField(max_length=100)
    some_random_field9 = models.CharField(max_length=100)
    some_random_field10 = models.CharField(max_length=100)
    some_random_field11 = models.CharField(max_length=100)
    some_random_field12 = models.CharField(max_length=100)
    some_random_field13 = models.CharField(max_length=100)
    some_random_field14 = models.CharField(max_length=100)
    some_random_field15 = models.CharField(max_length=100)
    some_random_field16 = models.CharField(max_length=100)
    some_random_field17 = models.CharField(max_length=100)
    some_random_field18 = models.CharField(max_length=100)
    some_random_field19 = models.CharField(max_length=100)
    some_random_field20 = models.CharField(max_length=100)
    some_random_field21 = models.CharField(max_length=100)
    some_random_field22 = models.CharField(max_length=100)
    some_random_field23 = models.CharField(max_length=100)
    some_random_field24 = models.CharField(max_length=100)
    some_random_field25 = models.CharField(max_length=100)
    some_random_field26 = models.CharField(max_length=100)
    some_random_field27 = models.CharField(max_length=100)
    some_random_field28 = models.CharField(max_length=100)
    some_random_field29 = models.CharField(max_length=100)
    some_random_field30 = models.CharField(max_length=100)
    some_random_field31 = models.CharField(max_length=100)
    some_random_field32 = models.CharField(max_length=100)
    some_random_field33 = models.CharField(max_length=100)
    some_random_field34 = models.CharField(max_length=100)
    some_random_field35 = models.CharField(max_length=100)
    some_random_field36 = models.CharField(max_length=100)
    some_random_field37 = models.CharField(max_length=100)
    some_random_field38 = models.CharField(max_length=100)
    some_random_field39 = models.CharField(max_length=100)
    some_random_field40 = models.CharField(max_length=100)
    some_random_field41 = models.CharField(max_length=100)
    some_random_field42 = models.CharField(max_length=100)
    some_random_field43 = models.CharField(max_length=100)
    some_random_field44 = models.CharField(max_length=100)
    some_random_field45 = models.CharField(max_length=100)
    some_random_field46 = models.CharField(max_length=100)
    some_random_field47 = models.CharField(max_length=100)
    some_random_field48 = models.CharField(max_length=100)
    some_random_field49 = models.CharField(max_length=100)
    some_random_field50 = models.CharField(max_length=100)
    # endregion

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(BaseModel):
    class Meta:
        pass
        # Added by RunSQL to support case insensitive lookup
        # indexes = [GinIndex(fields=["first_name", "last_name", "phone_number"])]

    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name="customers"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    address = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    # region random fields
    some_random_field0 = models.CharField(max_length=100)
    some_random_field1 = models.CharField(max_length=100)
    some_random_field2 = models.CharField(max_length=100)
    some_random_field3 = models.CharField(max_length=100)
    some_random_field4 = models.CharField(max_length=100)
    some_random_field5 = models.CharField(max_length=100)
    some_random_field6 = models.CharField(max_length=100)
    some_random_field7 = models.CharField(max_length=100)
    some_random_field8 = models.CharField(max_length=100)
    some_random_field9 = models.CharField(max_length=100)
    some_random_field10 = models.CharField(max_length=100)
    some_random_field11 = models.CharField(max_length=100)
    some_random_field12 = models.CharField(max_length=100)
    some_random_field13 = models.CharField(max_length=100)
    some_random_field14 = models.CharField(max_length=100)
    some_random_field15 = models.CharField(max_length=100)
    some_random_field16 = models.CharField(max_length=100)
    some_random_field17 = models.CharField(max_length=100)
    some_random_field18 = models.CharField(max_length=100)
    some_random_field19 = models.CharField(max_length=100)
    some_random_field20 = models.CharField(max_length=100)
    some_random_field21 = models.CharField(max_length=100)
    some_random_field22 = models.CharField(max_length=100)
    some_random_field23 = models.CharField(max_length=100)
    some_random_field24 = models.CharField(max_length=100)
    some_random_field25 = models.CharField(max_length=100)
    some_random_field26 = models.CharField(max_length=100)
    some_random_field27 = models.CharField(max_length=100)
    some_random_field28 = models.CharField(max_length=100)
    some_random_field29 = models.CharField(max_length=100)
    some_random_field30 = models.CharField(max_length=100)
    some_random_field31 = models.CharField(max_length=100)
    some_random_field32 = models.CharField(max_length=100)
    some_random_field33 = models.CharField(max_length=100)
    some_random_field34 = models.CharField(max_length=100)
    some_random_field35 = models.CharField(max_length=100)
    some_random_field36 = models.CharField(max_length=100)
    some_random_field37 = models.CharField(max_length=100)
    some_random_field38 = models.CharField(max_length=100)
    some_random_field39 = models.CharField(max_length=100)
    some_random_field40 = models.CharField(max_length=100)
    some_random_field41 = models.CharField(max_length=100)
    some_random_field42 = models.CharField(max_length=100)
    some_random_field43 = models.CharField(max_length=100)
    some_random_field44 = models.CharField(max_length=100)
    some_random_field45 = models.CharField(max_length=100)
    some_random_field46 = models.CharField(max_length=100)
    some_random_field47 = models.CharField(max_length=100)
    some_random_field48 = models.CharField(max_length=100)
    some_random_field49 = models.CharField(max_length=100)
    some_random_field50 = models.CharField(max_length=100)
    some_random_field51 = models.CharField(max_length=100)
    some_random_field52 = models.CharField(max_length=100)
    some_random_field53 = models.CharField(max_length=100)
    some_random_field54 = models.CharField(max_length=100)
    some_random_field55 = models.CharField(max_length=100)
    some_random_field56 = models.CharField(max_length=100)
    some_random_field57 = models.CharField(max_length=100)
    some_random_field58 = models.CharField(max_length=100)
    some_random_field59 = models.CharField(max_length=100)
    some_random_field60 = models.CharField(max_length=100)
    some_random_field61 = models.CharField(max_length=100)
    some_random_field62 = models.CharField(max_length=100)
    some_random_field63 = models.CharField(max_length=100)
    some_random_field64 = models.CharField(max_length=100)
    some_random_field65 = models.CharField(max_length=100)
    some_random_field66 = models.CharField(max_length=100)
    some_random_field67 = models.CharField(max_length=100)
    some_random_field68 = models.CharField(max_length=100)
    some_random_field69 = models.CharField(max_length=100)
    some_random_field70 = models.CharField(max_length=100)
    some_random_field71 = models.CharField(max_length=100)
    some_random_field72 = models.CharField(max_length=100)
    some_random_field73 = models.CharField(max_length=100)
    some_random_field74 = models.CharField(max_length=100)
    some_random_field75 = models.CharField(max_length=100)
    some_random_field76 = models.CharField(max_length=100)
    some_random_field77 = models.CharField(max_length=100)
    some_random_field78 = models.CharField(max_length=100)
    some_random_field79 = models.CharField(max_length=100)
    some_random_field80 = models.CharField(max_length=100)
    some_random_field81 = models.CharField(max_length=100)
    some_random_field82 = models.CharField(max_length=100)
    some_random_field83 = models.CharField(max_length=100)
    some_random_field84 = models.CharField(max_length=100)
    some_random_field85 = models.CharField(max_length=100)
    some_random_field86 = models.CharField(max_length=100)
    some_random_field87 = models.CharField(max_length=100)
    some_random_field88 = models.CharField(max_length=100)
    some_random_field89 = models.CharField(max_length=100)
    some_random_field90 = models.CharField(max_length=100)
    some_random_field91 = models.CharField(max_length=100)
    some_random_field92 = models.CharField(max_length=100)
    some_random_field93 = models.CharField(max_length=100)
    some_random_field94 = models.CharField(max_length=100)
    some_random_field95 = models.CharField(max_length=100)
    some_random_field96 = models.CharField(max_length=100)
    some_random_field97 = models.CharField(max_length=100)
    some_random_field98 = models.CharField(max_length=100)
    some_random_field99 = models.CharField(max_length=100)
    # endregion
