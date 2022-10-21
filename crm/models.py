from django.db import models


# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering = ['status_name']

def get_status_name():
    try:
        return StatusCrm.objects.get_or_create(name='New')
    except Exception:
        return 1

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone Number')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, default=get_status_name, verbose_name='Status')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['order_dt']


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Application')
    comment_dt = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    comment_text = models.TextField(verbose_name='Comment')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['comment_dt']
