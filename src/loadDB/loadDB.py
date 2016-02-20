#!/usr/bin/env python
'''
Created on 20 de feb. de 2016

@author: ivanuco
'''

import argparse
import laspy
from copy import copy
from pymongo import MongoClient
import bson

class loadDB():
    def __init__(self):
        self.parse_args()
        self.setup()

    def parse_args(self):
        parser =argparse.ArgumentParser(description = """Load a file in read mode and
                                        charge at DataBase.""")
        parser.add_argument("in_file", metavar = "in_file", 
                            type=str,nargs="+",help = "LAS file to plot")
        parser.add_argument("--mode",metavar="viewer_mode", type=str,default="default", 
                help = "Color Mode. Values to specify with a dimension: greyscale, heatmap.  Values which include a dimension: elevation, intensity, rgb")
        parser.add_argument("--dimension", metavar = "dim", type=str, default="intensity",
                help = "Color Dimension. Can be any single LAS dimension, default is intensity. Using color mode rgb, elevation, and intensity overrides this field.")

        self.args = parser.parse_args()
     
    def setup(self):
    # Check mode
        self.mode = self.args.mode
        self.dim = self.args.dimension
        try:
            client = MongoClient("0.0.0.0", 27017)
            db = client.lidar
            collection = db.zona            
            self.inFile = self.args.in_file
            for i in range(len(self.inFile)):
                inFile = laspy.file.File(self.inFile[i], mode = "r")
                print("Reading: " + inFile.filename)
                self.header=copy(inFile.header)
                self.vlrs = inFile.header.vlrs
                for p in range(len(inFile.points)): 
                    punto = {
                            'X': bson.Int64(inFile.X[p]),
                            'Y': bson.Int64(inFile.Y[p]),
                            'Z': bson.Int64(inFile.Z[p]),
                            'intensity': int(inFile.intensity[p]),
                            'flag_byte': int(inFile.flag_byte[p]),
                            'raw_classification': int(inFile.raw_classification[p]),
                            'scan_angle_rank': int(inFile.scan_angle_rank[p]),
                            'user_data':str(inFile.user_data[p]),
                            'pt_src': str(inFile.pt_src_id[p]),
                            'gps_time': inFile.gps_time[p],
                            'red': int(inFile.red[p]),
                            'green': int(inFile.green[p]),
                            'blue': int(inFile.blue[p])
                            }
                    collection.insert_one(punto)
                    #print(punto)
                inFile.close()                   
        except Exception, error:
            print("Error while reading file:")
            print(error)
            quit()
        
    def view(self):
        self.out.visualize(self.mode, self.dim)

def main():
    expl = loadDB()
    #expl.view()

if __name__ == '__main__':
    main()