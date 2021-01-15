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


class HypnotubeVideosIE(InfoExtractor):
    _VALID_URL = r'https://hypnotube.com/videos/$'

    def _real_extract(self, url):
        display_id = 'Hypnotube'
        entries = []

        for page_num in itertools.count(1):
            webpage = self._download_webpage(
                url, display_id, 'Downloading page %d' % page_num,
                query={'page': page_num})

            container = self._search_regex(
                r'(?s)<div[^>]+class=["\']box-container[^>]*>(.*)', webpage,
                'Hypnotube_extractor', default=webpage)

            ttt = orderedSet(re.findall(
                r'(https://hypnotube.com/video/[a-zA-Z-0-9-_]+-[0-9]+.html)',
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


class HypnotubeIE(InfoExtractor):
    _VALID_URL = r'https://hypnotube.com/video/[a-zA-Z0-9-]+-(?P<id>[0-9]+)\.html$'

    # https://hypnotube.com/video/safe-porn-for-good-sissies-11288.html

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(url, video_id)

        print('VIDEO')

        video_data = extract_attributes(self._search_regex(
            r'''(<source[^>]+>)''',
            webpage, 'video data'))

        video_url = video_data['src']

        title = self._search_regex(
            (r'<h1>([^<]+)</h1>', r'<title>([^<]+) - VidLii<'), webpage,
            'title')

        uploader_data = extract_attributes(self._search_regex(
            r'''(<a[^>]+href="https://hypnotube.com/user[^>]+>)''',
            webpage, 'video data'))

        uploader = uploader_data['title']

        return {
            'yo': 'hello',
            'id': video_id,
            'title': title,
            'uploader': uploader,
            'formats': [{
                'url': video_url,
                'vcodec': 'none',
            }],

        }
