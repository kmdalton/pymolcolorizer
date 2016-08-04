# pymolcolorizer

## Contents
1. Installation
2. Examples
3. License

## Installing pymolcolorizer

###Prerequisites
1. The PyMOL molecular graphics software can be obtained from one of the following sources:
  * https://sourceforge.net/projects/pymol/
  * https://www.pymol.org/
2. Matplotlib (http://matplotlib.org/)
3. Numpy (http://www.numpy.org/)

###Download pymolcolorizer  
"git clone http://github.com/kmdalton/pymolcolorizer"

###Install within PyMOL GUI  
The easiest way to install pymolcolorizer is through the builtin plugin manager within the PyMOL GUI. To install through the plugin manager do the following:


1. Open the PyMOL software
2. Navigate to the "Plugin --> Plugin Manager" option to launch the plugin manager
3. Click on the "Install New Plugin" tab
4. Under the "Install from local file" header click on "Choose file..."
5. Select the "pymolcolorizer.py" file from the github repository you downloaded

## Usage example  
At the moment, pymolcolorizer provides a parser to color a structure by residue numbers specified in a csv file. Any colormap supported by your current Matplotlib version can be used. See (http://matplotlib.org/examples/color/colormaps_reference.html) for a list of compatible colormaps. 


## License
MIT License

Copyright (c) [2016] [Kevin M Dalton]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
