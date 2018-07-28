# http://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/00/Slides00.pdf

import wget

for i in range(10):
  wget.download("https://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/0{}/Slides0{}.pdf".format(i, i))

for i in range(11, 28):
  wget.download("https://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/{}/Slides{}.pdf".format(i, i))
