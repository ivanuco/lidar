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
                            'X': inFile.X[p].tolist(),
                            'Y': inFile.Y[p].tolist(),
                            'Z': inFile.Z[p].tolist(),
                            'x': inFile.x[p].tolist(),
                            'y': inFile.y[p].tolist(),
                            'z': inFile.z[p].tolist(),
                            'intensity': inFile.intensity[p].tolist(),
                            'flag_byte': {
                                          'return_num': inFile.return_num[p].tolist(),
                                          'num_returns': inFile.num_returns[p].tolist(),
                                          'scan_dir_flag': bool(inFile.scan_dir_flag[p]),
                                          'edge_flight_line': bool(inFile.edge_flight_line[p])
                                          },
                            'raw_classification': {
                                                   'classification': inFile.classification[p].tolist(),
                                                   'synthetic': bool(inFile.synthetic[p]),
                                                   'key_point': bool(inFile.key_point[p]),
                                                   'withheld': bool(inFile.withheld[p])
                                                   },
                            'scan_angle_rank': inFile.scan_angle_rank[p].tolist(),
                            'user_data': inFile.user_data[p].tolist(),
                            'pt_src': inFile.pt_src_id[p].tolist(),
                            'gps_time': inFile.gps_time[p],
                            'red': inFile.red[p].tolist(),
                            'green': inFile.green[p].tolist(),
                            'blue': inFile.blue[p].tolist()
                            }
                    collection.insert_one(punto)
                    print(punto)
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