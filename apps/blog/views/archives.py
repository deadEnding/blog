#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.dates import BaseArchiveIndexView
from django.views.generic.dates import BaseYearArchiveView
from django.views.generic.dates import BaseMonthArchiveView
from django.views.generic.dates import BaseDayArchiveView
from django.views.generic.dates import BaseTodayArchiveView
from django.core.urlresolvers import reverse

from .mixins.archives import EntryArchiveMixin
from ..models import Entry, Category
from ..breadcrumbs import Link
from ..utils import valid_month


class EntryIndex(EntryArchiveMixin, BaseArchiveIndexView):
    """
    Mixin index.
    """

    @property
    def private_context_data(self):
        """
        Private context data: title, breadcrumbs, direct subdirectories.
        """
        ttl = u'首页'
        categories = Category.objects.filter(parent=None)
        labels = [Link(cg.title, cg.get_absolute_url()) for cg in categories]
        return {'ttl': ttl, 'breadcrumbs': [Link('Index')], 'labels': labels}


class EntryYear(EntryArchiveMixin, BaseYearArchiveView):
    """
    Mixin year.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        year = self.kwargs['year']
        ttl = '%s年' % year
        labels = [Link('%02d月' % m, reverse('blog:archives:month', args=[year, '%02d' % m])) 
            for m in valid_month(year)]
        return {'ttl': ttl, 'breadcrumbs': [Link('%s年' % year)], 'labels': labels}


class EntryMonth(EntryArchiveMixin, BaseMonthArchiveView):
    """
    Mixin month.
    """
    
    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs, direct subdirectories.
        """
        year = self.kwargs['year']
        month = self.kwargs['month']
        ttl = '%s年%s月' % (year, month)
        breadcrumbs = [Link('%s年' % year, reverse('blog:archives:year', args=[year])), Link('%s月' % month)]
        return {'ttl': ttl, 'breadcrumbs': breadcrumbs, 'labels': []}
