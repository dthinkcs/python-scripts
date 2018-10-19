# http://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/00/Slides00.pdf

import wget

for i in range(13):
  wget.download("https://cdn.cs50.net/mobile/2018/spring/lectures/{}/lang/en/lecture{}.srt".format(i, i))
