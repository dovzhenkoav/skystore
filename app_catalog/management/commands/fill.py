from django.core.management import BaseCommand
from app_catalog.models import Category, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        for i in range(100):
            category = Category.objects.create(name=f'Cat{i}', description='Sample text')

            product = Product.objects.create(
            id=i,
            name=f'Product{i}',
            description='Sample text',
            image="products/wallhaven-rdqxqq_aeSBagY.png",
            category=category,
            price=i
            )

            category.save()
            product.save()
