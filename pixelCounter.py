#!/usr/bin/env python
import os, sys
from PIL import Image

def topColors(imgfile, limit):
    im = Image.open(imgfile)
    im_rgb = im.convert("RGB")
    pData = im_rgb.getdata()
    img_size = len(pData) * 1.0
    colorList = {}
    for p in pData:
        if p not in colorList:
            colorList[p] = 1
        else:
            colorList[p] += 1

    csorted = {k: ( v/img_size ) for k, v in sorted(colorList.items(), key=lambda item: item[1], reverse=True)[0:limit]}
    return csorted

def colorSimilarity(c1, c2):
    dR = abs(c1[0] - c2[0])
    dG = abs(c1[1] - c2[1])
    dB = abs(c1[2] - c2[2])
    return max(dR, dG, dB)

def calcSimilarity(f1, f2):
    s = 1
    for idx in range(len(f1.keys())):
        c1 = list(f1.keys())[idx]
        c2 = list(f2.keys())[idx]
        cs = colorSimilarity(c1, c2)
        if cs > 2:
            return 0
        fs = abs(f1[c1] - f2[c2])
        s -= fs
    return max(s, 0)

def compareRefs(f, refs):
    best_score = 0
    best_match = None
    for key in refs.keys():
        rs = calcSimilarity(f, refs[key])
        if rs > best_score:
            best_score = rs
            best_match = key

    return (best_match, best_score)

ref_dir = 'flags/'
ref_files = os.listdir(ref_dir)
refs = {}

print('Building reference dictionary')
for rf in ref_files:
    if 'flag' in rf and rf.endswith('gif'):
        colors = topColors(os.path.join(ref_dir, rf), 3)
        refs[rf] = colors

print('Characterizing test item')
infile = sys.argv[1]
infile_colors = topColors(infile, 3)

print('Comparing to reference items')
(bestMatch, bestScore) = compareRefs(infile_colors, refs)

print('Best match is...')
print(bestMatch, bestScore)
