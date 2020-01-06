## PixelCounter
### Matching randomized images against a reference set

### Setup:

`pip3 install -r requirements.txt`

### Usage:

`python pixelCounter.py flag_3.png`

### Output:

```Building reference dictionary
Characterizing test item
Comparing to reference items
Best match is...
('WA-flag.gif', 0.969464780117185)
```

## Description

This code will identify the 3 most common colors in a set of reference images and calculate the fraction of each image that is made up of that color.  It will then make the same calculation against a reference image.

To identify the original, unscrambled image the most common colors are compared against each other.  To account for compression artifacts a small difference in value in each RGB color channel is allowed.  If the colors match, then the fractional makeup is compared and the difference is subtracted from the total score, which is initialized with a value of 1.  

For example, if scrambled image A has (223, 12, 220) as it's most common color at 37%, and reference image B has (224, 13, 219) as it's most common color at 38%, the colors are close enough to match, and the matching score will be 0.99 (1% difference).  Exact matches are not expected, again due to compression artifacts. 

This is repeated for all 3 top colors for all reference images and the best match is returned.  

## Riddler Answers

This code was written to answer 538's Weekly Riddler challenge (See here: https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/
).  The 3 flags are

 *  Flag A - France
 *  Flag B - Brazil
 *  Flag C - Namibia

### References 

Reference flags downloaded from CIA World Factbook https://www.cia.gov/library/publications/the-world-factbook/docs/flagsoftheworld.html

