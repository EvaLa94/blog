from django.template.defaultfilters import slugify
from django.db.models import Q


def slugify_instance_title(instance):
    slug = slugify(instance.title)
    conditions = Q(slug__regex=r'{}-[0-9]+'.format(slug)) | Q(slug=slug)
    Klass = instance.__class__
    articles = Klass.objects.filter(conditions)
    nums = []
    for article in articles:
        slug_ending = article.slug.split('-')[-1]
        if slug_ending.isdigit():
            nums.append(int(slug_ending))
    increment_num = 0 if not nums else max(nums)
    return f'{slug}-{increment_num + 1}'
