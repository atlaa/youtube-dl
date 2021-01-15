# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import (
    determine_ext,
    extract_attributes,
    int_or_none,
    orderedSet
)

import datetime
import locale
import re
import itertools


class FipVideosIE(InfoExtractor):
    _VALID_URL = r'https://www.fip.fr/theme/production-fip$'

    def _real_extract(self, url):
        display_id = 'Fip'
        entries = []

        for page_num in itertools.count(1):
            webpage = self._download_webpage(
                url, display_id, 'Downloading page %d' % page_num,
                query={'p': page_num})

            container = self._search_regex(
                r'(?s)<div[^>]+class=["\']columned-teasers-container[^>]*>(.*?)<ul>', webpage,
                'FranceMusique_extractor', default=webpage)

            ttt = orderedSet(re.findall(
                r'"((\/[a-z\-]+)+[0-9]+)"',
                container))

            entries = entries + [
                self.url_result("https://www.fip.fr%s" % ii[0])
                for ii in ttt
            ]

            next_url = self._search_regex(r'<li\s+class=(["\'])pagination-item last',
                                          webpage, 'list_next_url', default=None)

            if not next_url:
                break

        return self.playlist_result(
            entries)
