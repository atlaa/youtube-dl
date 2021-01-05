#python -m youtube_dl https://www.france.tv/france-5/silence-ca-pousse/ --match-filter 'duration < 600'
#python -m youtube_dl https://www.france.tv/france-2/envoye-special/

#python -m youtube_dl --add-metadata --write-all-thumbnails --embed-thumbnail -o "%(title)s.%(ext)s" --audio-format mp3 --audio-quality 0 https://www.francemusique.fr/emissions/le-cri-du-patchwork/cri-4-un-besoin-de-cri-73036
#python -m youtube_dl --add-metadata --embed-thumbnail --extract-audio --audio-format mp3  https://www.youtube.com/watch?v=jzsYk49yowU


#youtube-dl https://www.youtube.com/watch?v=jzsYk49yowU  -x --audio-format mp3 --add-metadata --xattrs --embed-thumbnail --prefer-ffmpeg --postprocessor-args "-metadata description='my comment'"  --verbose
#python -m youtube_dl https://www.francemusique.fr/emissions/le-cri-du-patchwork/cri-4-un-besoin-de-cri-73036  -o "%(album)s - %(title)s.%(ext)s" -x --audio-format mp3 --add-metadata --embed-thumbnail --prefer-ffmpeg


#python -m youtube_dl https://www.francemusique.fr/emissions/le-cri-du-patchwork  --max-downloads 4 -o "%(album)s - %(title)s.%(ext)s" -x --audio-format mp3 --add-metadata --embed-thumbnail --prefer-ffmpeg
#python -m youtube_dl https://www.francemusique.fr/emissions/le-cri-du-patchwork/cri-4-un-besoin-de-cri-73036  -o "%(album)s - %(title)s.%(ext)s" -x --audio-format mp3 --add-metadata --embed-thumbnail --prefer-ffmpeg
#python -m youtube_dl https://www.francemusique.fr/emissions/le-cri-du-patchwork/cri-5-un-dernier-cri-73209  -o "%(album)s - %(title)s.%(ext)s" -x --audio-format mp3 --add-metadata --embed-thumbnail --prefer-ffmpeg

python -m youtube_dl https://www.france.tv/france-5/la-maison-france-5/