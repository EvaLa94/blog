from django.template.defaultfilters import slugify
from django.db.models import Q


def slugify_instance_title(instance):
    slug = slugify(instance.title)
    conditions = Q(slug__regex=r'{}-[0-9]+'.format(slug)) | Q(slug=slug)
    Klass = instance.__class__
    articles = Klass.objects.filter(conditions)
    nums = [int(article.slug.split('-')[-1])
            for article in articles if article.slug.split('-')[-1].isdigit()]
    increment_num = 0 if not nums else max(nums)
    return f'{slug}-{increment_num + 1}'
