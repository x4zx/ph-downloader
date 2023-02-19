import yt_dlp
from colorama import Fore, Style
from core import is_link, ph_url_check, ph_page_check

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
        'skip_unavailable_fragments': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])

        except yt_dlp.DownloadError:
            print(Fore.RED + '!!!: ' + Style.RESET_ALL + \
                'The video could not be downloaded correctly. Try again!')
