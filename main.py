import sys
import asyncio
from core import download

async def main():

    value = input('Enter video/playlist link: ')
    if not value:
        sys.exit()
    
    else:
        await download(value)

if __name__ ==  '__main__':
    asyncio.run(main())
