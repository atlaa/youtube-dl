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
import re
import itertools


class PorntubeclubVideosIE(InfoExtractor):
    _VALID_URL = r'https://porn-tube-club.com/a[0-9]*/$'

    def _real_extract(self, url):
        display_id = 'Hypnotube'
        entries = []

        for page_num in itertools.count(1):
            webpage = self._download_webpage(
                url, display_id, 'Downloading page %d' % page_num,
                query={'page': page_num})

            print(webpage)
            container = self._search_regex(
                r'(?s)<div[^>]+class=["\']video_thumb_content[^>]*>(.*)', webpage,
                'Porntubeclub_extractor', default=webpage)

            ttt = orderedSet(re.findall(
                r'(https://porn-tube-club.com/v[0-9]*/[0-9]*/)',
                container))

            entries = entries + [
                self.url_result("%s" % ii)
                for ii in ttt
            ]

            next_url = self._search_regex(r'<a\s+rel=(["\'])next',
                                          webpage, 'list_next_url', default=None)
            if not next_url:
                break
            break  # only first page

        return self.playlist_result(
            entries)
