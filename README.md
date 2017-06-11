usage: lasviewer.exe [-h] [--mode viewer_mode] [--dimension dim]
                     in_file [in_file ...]

Open a file in read mode and print a simple description.

positional arguments:
  in_file             LAS file to plot

optional arguments:
  -h, --help          show this help message and exit
  --mode viewer_mode  Color Mode. Values to specify with a dimension:
                      greyscale, heatmap. Values which include a dimension:
                      elevation, intensity, rgb
  --dimension dim     Color Dimension. Can be any single LAS dimension,
                      default is intensity. Using color mode rgb, elevation,
                      and intensity overrides this field.



usage: loadDB.exe [-h] [--ip mongo_server_ip] [--port mongo_server_port]
                  in_file [in_file ...]

Load a file in read mode and charge at DataBase.

positional arguments:
  in_file               LAS file to plot

optional arguments:
  -h, --help            show this help message and exit
  --ip mongo_server_ip  IP of the MongoDB server to connect. If not informed
                        'localhost' is used as default.
  --port mongo_server_port
                        Port of the MongoDB server to connect. If not informed
                        '27017' is used as default.