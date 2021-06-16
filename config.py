#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://youtu.be/zcrUCvBD16k")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("1154046238", "")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("1741359", ""))
    CHAT = int(os.environ.get("-1001162918742", ""))
    LOG_GROUP=os.environ.get("-1001162918742", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ARQ_API=os.environ.get("SHGNMV-BYZNJC-CVVDAV-HWRDUC-ARQ", "")
    DURATION_LIMIT=int(os.environ.get("DUR", 15))
    API_HASH = os.environ.get("939eaad9444f8f2954f73346dacf13ad", "")
    BOT_TOKEN = os.environ.get("1859922656:AAE7VesCB9DazEniFvqhlBw4YeKOdXWKoFo", "") 
    SESSION = os.environ.get("AQAS32FXlh1lCdNBXBPhClGuyG7r0-stNWz7HZEzqy-g1Q-Dw3OSCUmpKy1RHJ4mRbAd8vuiQenEBHbWA6qCLWBGDZaq6rSDkXJufCEdWF1z6spNE6_Sa6DVijuMI7n9EHSskaU_RMkxkyFAtxJmoILu6HvpO0mTIb_RXaPQW2zIeHh3tjGQ7X6pRrBlEKq5nvwXkfVGlkniCm8O_0zt3Ri8hzpqAlKu7QCtpKSIrPO6D52EKfeIijLgRgJs38H7NcL8vDoRP4tChd_9AsTDP1T5lPxDRo_fsh2KRQgfBi8ytdKFJQBIDCXH7Wm-Xa_GQ7CMR6v-YRK1Ai7xrlq3hrMeRMlZHgA", "")
    playlist=[]
    msg = {}

