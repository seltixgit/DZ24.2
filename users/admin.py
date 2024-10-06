from django.contrib import admin

from users.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'payment_course', 'payment_lesson', 'cost', 'payment_method')
    list_filter = ('user', 'payment_date', 'payment_course', 'payment_lesson', 'cost', 'payment_method')
    search_fields = ('payment_method',)
