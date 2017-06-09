#!/usr/bin/env python
'''
Created on 27/01/2016

@author: ivanuco
'''

import argparse
import laspy
import numpy as np
from copy import copy

class lasview():
    def __init__(self):
        self.parse_args()
        self.setup()

    def parse_args(self):
        parser =argparse.ArgumentParser(description = """Open a file in read mode and
                                        print a simple description.""")
        parser.add_argument("in_file", metavar = "in_file", 
                            type=str,nargs="+",help = "LAS file to plot")
        parser.add_argument("--mode",metavar="viewer_mode", type=str,default="default", 
                help = "Color Mode. Values to specify with a dimension: greyscale, heatmap.  Values which include a dimension: elevation, intensity, rgb")
        parser.add_argument("--dimension", metavar = "dim", type=str, default="intensity",
                help = "Color Dimension. Can be any single LAS dimension, default is intensity. Using color mode rgb, elevation, and intensity overrides this field.")

        self.args = parser.parse_args()
     
    def setup(self):
    # Check mode
        for f in self.args.in_file:
            print("Reading: " + f)
        self.mode = self.args.mode
        self.dim = self.args.dimension
        try:
            self.inFile = self.args.in_file
            for i in range(len(self.inFile)):
                inFile = laspy.file.File(self.inFile[i], mode = "r")
                if i == 0:
                    self.header=copy(inFile.header)
                    self.vlrs = inFile.header.vlrs
                    #out = laspy.file.File("./output.las",mode= "w",header=copy(inFile.header), vlrs = inFile.header.vlrs)
                    self.points = copy(inFile.points)
                else:
                    self.points = np.concatenate((self.points,inFile.points),axis=0)
                inFile.close()
            self.out = laspy.file.File("./output.las",mode= "w",header=self.header, vlrs = self.vlrs)
            self.out.points = self.points
        except Exception, error:
            print("\nError while reading file:")
            print(error)
            #quit()
        
    def view(self):
        self.out.visualize(self.mode, self.dim)

def main():
    expl = lasview()
    expl.view()

if __name__ == '__main__':
    main()