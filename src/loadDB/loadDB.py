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
import sys as Sys

# Print iterations progress
def printProgress (iteration, total, prefix='', suffix='', decimals=2, barLength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
    filledLength = int(round(barLength * iteration / float(total)))
    percents = round(100.00 * (iteration / float(total)), decimals)
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    Sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    Sys.stdout.flush()
    if iteration == total:
        print("\n")


class loadDB():
    def __init__(self):
        self.parse_args()
        self.setup()

    def parse_args(self):
        parser = argparse.ArgumentParser(description="""Load a file in read mode and
                                        charge at DataBase.""")
        parser.add_argument("--ip", metavar="mongo_server_ip", type=str, default="localhost", help="IP of the MongoDB server to connect. If not informed 'localhost' is used as default.")
        parser.add_argument("--port", metavar="mongo_server_port", type=int, default=27017, help="Port of the MongoDB server to connect. If not informed '27017' is used as default.")
        parser.add_argument("in_file", metavar="in_file",
                            type=str, nargs="+", help="LAS file to plot")
        self.args = parser.parse_args()
     
    def setup(self):
    # Check mode
        self.ip = self.args.ip
        self.port = self.args.port
        try:
            client = MongoClient(self.ip, self.port)
            db = client.lidar
            collection = db.zona            
            self.inFile = self.args.in_file
            inicio = datetime.datetime.now()
            print ("Inicio de carga de datos = %s" % inicio)
            for i in range(len(self.inFile)):
                inFile = laspy.file.File(self.inFile[i], mode="r")
                print("Reading: " + inFile.filename)                
                longitud = len(inFile.points)                
                printProgress(0, longitud - 1, prefix='Progreso:', suffix='Completo', barLength=50)
                self.header = copy(inFile.header)
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
                documents = []
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
                    documents.append(punto)
                    if len(documents) > 999 :
                        collection.insert_many(documents)
                        printProgress(p, longitud - 1, prefix='Progreso:', suffix='Completo', barLength=50)
                        documents = []                    
                if len(documents) > 0 :
                    collection.insert_many(documents)
                    printProgress(p, longitud - 1, prefix='Progreso:', suffix='Completo', barLength=50)
                    documents = []
            final = datetime.datetime.now()
            total = final - inicio
            print ("Final de carga de datos = %s" % final)
            print ("Tiempo empleado = %s" % total)                   
        except Exception, error:
            print("\nError while reading file:")
            print(error)
            #quit()
        
    def view(self):
        self.out.visualize(self.mode, self.dim)

def main():
    loadDB()
    

if __name__ == '__main__':
    main()
