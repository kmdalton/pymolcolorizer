from pymol import cmd, stored
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib.cm import ScalarMappable
from matplotlib.pyplot import get_cmap
from matplotlib.colors import Normalize
import numpy as np
import re

colors = ['tv_blue', 'tv_red', 'tv_green']

class attributePainter():
    """
    attributePainter(csvFN, **kwargs)
        csvFN: (string) the filename of the csv file containing the attribute you wish to paint on the residues;
               the file format is like 'chainID ('1,2,3,...Z' -- pymol allowed chain ids), residue number (int), value (float)\\n'
        colormap = str: kwarg for specifying colormap. can be any colormap name from matplotlib ('http://matplotlib.org/examples/color/colormaps_reference.html')
    """
    def __init__(self, csvFN = None, **kw):
        self.colormapname = kw.get('colormap', 'viridis')
        self.cmap = get_cmap(self.colormapname)
        self.chains = {}
        self.norms  = None
        self.sm = None
        if csvFN is not None:
            self.loadCSV(csvFN)

    def loadCSV(self, csvFN):
        """
        attributePainter.loadCSV(csvFN) -- populate the class variables with the information in the csv file. in particular, this
            sets self.minval, self.norms
            csvFN: (string) the filename of the csv file containing the attribute you wish to paint on the residues;
                   the file format is like 'chainID ('1,2,3,...Z' -- pymol allowed chain ids), residue number (int), value (float)\\n'
                   lines starting with an octothorpe (#) will be ignored
        """
        chains = {}
        for i,line in enumerate(open(csvFN).readlines(), 1):
            if line[0] != '#':
                cells   = line.strip().split(',')
                chainID = re.sub(r'^\s+', '', cells[0])
                try:
                    resnum  = int(re.sub(r'^\s+', '', cells[1]))
                    value   = float(re.sub(r'^\s+', '', cells[2]))
                    if chainID in self.chains:
                        self.chains[chainID][resnum] = value
                    else:
                        self.chains[chainID] = {resnum: value}
                except ValueError:
                    print "Line number {}  ({}) was rejected -- could not format".format(i, line)
        ranges = {chainID: (min(chain.values()), max(chain.values())) for chainID, chain in self.chains.iteritems()}
        self.norms = {chainID: Normalize(r[0], r[1]) for chainID, r in ranges.iteritems()}
        self.sm    = {chainID: ScalarMappable(norm, self.cmap) for chainID, norm in self.norms.iteritems()}
        self.norms['global'] = Normalize(min([i[0] for i in ranges.values()]), max([i[1] for i in ranges.values()]))
        self.sm['global']    = ScalarMappable(self.norms['global'], self.cmap) 

    def paintChain(self, chainID, **kw):
        colormapname = kw.get('colormapname', self.colormapname) 
        Norm = self.norms[kw.get('norm', 'global')]
        cmap = ScalarMappable(Norm, get_cmap(colormapname))
        for resnum,value in self.chains[chainID].iteritems(): 
            colorname = "chain{}res{}".format(chainID, resnum)
            cmd.set_color(colorname, cmap.to_rgba(value)[:-1])
            cmd.color(colorname, "chain {} and resi {}".format(chainID, resnum))

    def modifyBfactors(self, chainID, **kw):
        cmd.alter("all", "b={}".format(np.median(self.chains[chainID].values())))
        for resnum,value in self.chains[chainID].iteritems(): 
            cmd.alter("chain {} and resi {}".format(chainID, resnum), "b={}".format(value))

def paintStructure(csvFN, colormapname=None):
    """
    Color all the chains in a structure by the parameters in a CSV file using a global colormap including all chains
    """
    if colormapname is None:
        colormapname = 'viridis'
    painter = attributePainter(csvFN)
    for chainID in painter.chains.keys():
        painter.paintChain(chainID, colormapname=colormapname)


def modifyBfactors(csvFN):
    """
    Color all the chains in a structure by the parameters in a CSV file using a global colormap including all chains
    """
    painter = attributePainter(csvFN)
    for chainID in painter.chains.keys():
        painter.modifyBfactors(chainID)

def saveHorizontalColorbar(csvFN, outFN, colormapname=None):
    if colormapname is None:
        colormapname = 'viridis'
    painter = attributePainter(csvFN)
    plt.figure(figsize=(2,10))
    ax = plt.gca()
    plt.colorbar(painter.sm['global'], cax=ax, orientation='horizontal')
    plt.savefig(outFN, fmt=outFN[-3:])

def saveVerticalColorbar(csvFN, outFN, colormapname=None):
    if colormapname is None:
        colormapname = 'viridis'
    painter = attributePainter(csvFN)
    plt.figure(figsize=(10,2))
    ax = plt.gca()
    plt.colorbar(painter.sm['global'], cax=ax, orientation='vertical')
    plt.savefig(outFN, fmt=outFN[-3:])

cmd.extend('colorFromCSV', paintStructure)
cmd.extend('bfacsFromCSV', modifyBfactors)
cmd.extend('saveHorizontalColorbar', saveHorizontalColorbar)
cmd.extend('saveVerticalColorbar', saveVerticalColorbar)
