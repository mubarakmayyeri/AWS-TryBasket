from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Payment,)
admin.site.register(Order,)
admin.site.register(OrderProduct,)
admin.site.register(Address,)
admin.site.register(Coupon)
admin.site.register(UserCoupon)