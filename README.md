
stereo_text.py
============

**stereo_text.py** is a proof of concept designed to generate blocks of text with a hidden 3d message in the form of an [autostereogram](https://en.wikipedia.org/wiki/Autostereogram). It takes input from stdin and converts any words wrapped in /forward slashes/ into 3d.

-----

**Usage and examples:**

```
~/stereo_text$ ./stereo_text.py -h
usage: stereo_text.py [-h] [-s] [-p PADDING]

generate blocks of text with a hidden 3dmessage in the form of an
autostereogram

optional arguments:
  -h, --help  show this help message and exit
  -s          Convert single spaces to double spaces. This can help withwith
              formatting.
  -p PADDING  Number ofspaces between the end of the longest line on the first
              panel, andbeginning of the next panel. Default: 10

~/stereo_text$ cat example.txt
The this past /random/ unexplainably contrary
and before hit joyfully /gibberish/ bluebird
fishily and /just/ much ladybug hyena chaste
elephant until far /for/ some since and prior
visually cuckoo magically /example/ goodness that.

~/stereo_text$ cat example.txt | ./stereo_text.py -s -p 5
The  this  past  random  unexplainably  contrary            The  this  past random   unexplainably  contrary
and  before  hit  joyfully  gibberish  bluebird             and  before  hit  joyfully gibberish   bluebird
fishily  and  just  much  ladybug  hyena  chaste            fishily  and just   much  ladybug  hyena  chaste
elephant  until  far  for  some  since  and  prior          elephant  until  far for   some  since  and  prior
visually  cuckoo  magically  example  goodness  that.       visually  cuckoo  magically example   goodness  that.
```

-----

**Known Bugs:**

* two or more separate instances of words/phrases on the same line will result in some slashes not being stripped, and in general this will break the 3d effect

-----

**To do:**

* Add ascii borders around each panel of text
* I would like to allow for command-line arguments to adjust spacing between panels, as well as to modify the number of panels generated with number coding within the slash-wrapped text to designate the panel on which that word will be in 3d, for example /this:3/ would only have that word in 3d on the 3rd panel
* Add option for backslash-wrapped text to be 3d in a way that causes it to fall behind the regular text (as opposed to popping out in front)
