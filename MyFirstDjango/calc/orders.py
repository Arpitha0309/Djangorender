class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivered','Delivered')
        )
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status=models.CharField(max_length=300, choices=STATUS)