import wget

for i in range(10):
  wget.download("https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/0{}/Slides0{}.pdf".format(i, i))

for i in range(11, 23):
  wget.download("https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/{}/Slides{}.pdf".format(i, i))
