#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import logging
from django.utils import six
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.utils.functional import cached_property

from bs4 import BeautifulSoup

from .settings import PREVIEW_SPLITTERS
from .settings import PREVIEW_MAX_WORDS
from .settings import PREVIEW_MORE_STRING

logger = logging.getLogger('online')


class HTMLPreview(object):
    """
    Build an HTML preview of an HTML content.
    """

    def __init__(self, content, excerpt='',
                 splitters=PREVIEW_SPLITTERS,
                 max_words=PREVIEW_MAX_WORDS,
                 more_string=PREVIEW_MORE_STRING):
        self._preview = None

        self.excerpt = excerpt
        self.content = content
        self.splitters = splitters
        self.max_words = max_words
        self.more_string = more_string

    @property
    def preview(self):
        """
        The preview is a cached property.
        """
        if self._preview is None:
            self._preview = self.build_preview()
        return self._preview

    def __str__(self):
        """
        Method used to render the preview in templates.
        """
        return six.text_type(self.preview)

    def build_preview(self):
        """
        Build the preview.
        """
        # if self.excerpt:
            # return self.excerpt
        for splitter in self.splitters:
            if splitter in self.content:
                return self.split(splitter)
        return self.truncate()

    def truncate(self):
        """
        Truncate the content with the Truncator object.
        """
        return Truncator(self.content).words(
            self.max_words, self.more_string, html=True)

    def split(self, splitter):
        """
        Split the HTML content with a marker
        without breaking closing markups.
        """
        soup = BeautifulSoup(self.content.split(splitter)[0],
                             'html.parser')
        last_string = soup.find_all(text=True)[-1]
        last_string.replace_with(last_string.string + self.more_string)
        return soup
