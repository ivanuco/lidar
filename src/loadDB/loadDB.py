#!/usr/bin/env python
'''
Created on 20 de feb. de 2016

@author: ivanuco
'''

import argparse
import laspy
from copy import copy
from pymongo import MongoClient
import datetime


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
                inicio = datetime.datetime.now()
                longitud = len(inFile.points)
                print ("Inicio de carga de datos = %s" % inicio)
                self.header=copy(inFile.header)
                self.vlrs = inFile.header.vlrs
                X = inFile.X
                Y = inFile.Y
                Z = inFile.Z
                x = inFile.x
                y = inFile.y
                z = inFile.z
                intensity = inFile.intensity
                return_num = inFile.return_num
                num_returns = inFile.num_returns
                scan_dir_flag = inFile.scan_dir_flag
                edge_flight_line = inFile.edge_flight_line
                classification = inFile.classification
                synthetic = inFile.synthetic
                key_point = inFile.key_point
                withheld = inFile.withheld
                scan_angle_rank = inFile.scan_angle_rank
                user_data = inFile.user_data
                pt_src = inFile.pt_src_id
                gps_time = inFile.gps_time
                red = inFile.red
                green = inFile.green
                blue = inFile.blue
                inFile.close()
                for p in range(longitud): 
                    punto = {
                            'X': X[p].tolist(),
                            'Y': Y[p].tolist(),
                            'Z': Z[p].tolist(),
                            'x': x[p].tolist(),
                            'y': y[p].tolist(),
                            'z': z[p].tolist(),
                            'intensity': intensity[p].tolist(),
                            'flag_byte': {
                                          'return_num': return_num[p].tolist(),
                                          'num_returns': num_returns[p].tolist(),
                                          'scan_dir_flag': bool(scan_dir_flag[p]),
                                          'edge_flight_line': bool(edge_flight_line[p])
                                          },
                            'raw_classification': {
                                                   'classification': classification[p].tolist(),
                                                   'synthetic': bool(synthetic[p]),
                                                   'key_point': bool(key_point[p]),
                                                   'withheld': bool(withheld[p])
                                                   },
                            'scan_angle_rank': scan_angle_rank[p].tolist(),
                            'user_data': user_data[p].tolist(),
                            'pt_src': pt_src[p].tolist(),
                            'gps_time': gps_time[p],
                            'red': red[p].tolist(),
                            'green': green[p].tolist(),
                            'blue': blue[p].tolist()
                            }
                    collection.insert_one(punto)
                    print(p,longitud,punto)
                final = datetime.datetime.now()
                total = final - inicio
                print ("Final de carga de datos = %s" % final)
                print ("Tiempo empleado = %s" % total)                   
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