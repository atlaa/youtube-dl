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


class FranceMusiqueIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?francemusique\.fr/emissions/[^/]+/(?P<id>[\w|-]+)$'

    _TEST = {
        'url': 'https://www.francemusique.fr/emissions/le-cri-du-patchwork/cri-5-un-dernier-cri-73209',
        'info_dict': {
            'id': 'cri-5-un-dernier-cri-73209',
            'display_id': 'cri-5-un-dernier-cri-73209',
            'ext': 'mp3',
            'title': 'CRI 5 : Un dernier cri',
            'thumbnail': r're:^https?://.*\.jpg$',
            'upload_date': '20140301',
            'timestamp': 1393642916,
            'vcodec': 'none',
        }
    }

    def _real_extract(self, url):
        display_id = self._match_id(url)

        webpage = self._download_webpage(url, display_id)

        container = self._search_regex(
            r'(?s)<div[^>]+class=["\']cover-diffusion-main-info-replay-button+[^>]*>(.*?)</div>', webpage,
            'Francemusique_extractor', default="webpage")

        video_data = extract_attributes(self._search_regex(
            r'''(<button[^>]+replay-button+[^>]+>)''',
            container, 'video data'))

        video_url = video_data['data-url']

        description = self._html_search_regex(
            r'(?s)<p[^>]+class="content-body-chapo"[^>]*>(.*?)</p>',
            webpage, 'description', default=None)

        thumbnail = self._search_regex(
            r'(?s)<figure[^>]+class="rich-visual"[^>]*>.*?<img[^>].*src="([^"]+)"(?s).*content-body-article',
            webpage, 'thumbnail', fatal=False)

        upload_date = self._html_search_regex(
            r'(?s)<div[^>]+class="cover-diffusion-text-date"[^>]*>(.*?)</div>',
            webpage, 'upload_date', default=None)

        # Mardi 18 juin 2019
        saveLocale = locale.getlocale()
        locale.setlocale(locale.LC_TIME, "fr_FR")
        upload_date = date_time_obj = datetime.datetime.strptime(upload_date, '%A %d %B %Y').date()
        #locale.setlocale(saveLocale[0], saveLocale[1])

        ext = determine_ext(video_url.lower())

        return {
            'id': display_id,
            'display_id': display_id,
            'url': video_url,
            'title': video_data.get('data-diffusion-title'),
            'album': video_data.get('data-emission-title'),
            'comment': description,
            'description': description,
            'thumbnail': thumbnail,
            'ext': ext,
            'vcodec': 'none' if ext == 'mp3' else None,
            'uploader': video_data.get('data-diffusion-description').replace("Par ", ""),
            'upload_date': upload_date,
            'timestamp': int_or_none(video_data.get('data-asset-created-date')),
            'duration': int_or_none(video_data.get('data-duration')),
        }


class FranceMusiqueEmissionIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?francemusique\.fr/emissions/([\w|-]*)$'

    # https://www.francemusique.fr/emissions/le-cri-du-patchwork

    def _real_extract(self, url):
        display_id = 'FranceMusique'
        entries = []

        for page_num in itertools.count(1):
            webpage = self._download_webpage(
                url, display_id, 'Downloading page %d' % page_num,
                query={'p': page_num})

            container = self._search_regex(
                r'(?s)<section[^>]+class=["\']emission-diffusions-list[^>]*>(.*?)</section>', webpage,
                'FranceMusique_extractor', default=webpage)

            ttt = orderedSet(re.findall(
                r'(/emissions/[a-zA-Z-0-9-_]+/[a-zA-Z-0-9-_]+)',
                container))

            entries = entries + [
                self.url_result("https://www.francemusique.fr%s" % ii)
                for ii in ttt
            ]

            next_url = self._search_regex(r'<a\s+rel=(["\'])next',
                                          webpage, 'list_next_url', default=None)
            if not next_url:
                break

        return self.playlist_result(
            entries)
