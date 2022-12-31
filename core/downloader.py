import yt_dlp
from core.checker import (
    is_link, ph_url_check, ph_page_check
)


def download(url: str):
    is_link(url)
    ph_url_check(url)
    ph_page_check(url)


    outtmpl = './pornhub/%(uploader)s' + '/%(id)s.%(ext)s'
    ydl_opts = {
        'nooverwrites': True,
        'ignoreerrors': False,
        'no_warnings': False,
        'outtmpl': outtmpl,
        'format': 'best',
        'playlistreverse': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
