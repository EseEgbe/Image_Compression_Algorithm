import configparser
global cwd, image_path

config = configparser.ConfigParser()
config.read('Config.ini')
cwd = config['PATHS']['cwd']
image_path = config['PATHS']['image_path']
compressed_image_path = config['PATHS']['compressed_image_path']