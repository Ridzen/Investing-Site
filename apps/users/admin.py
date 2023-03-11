from django.contrib import admin
from .models import (Investor, BusinessOwner,
                     BlockedUser)

admin.site.register(BusinessOwner)
admin.site.register(Investor)
admin.site.register(BlockedUser)