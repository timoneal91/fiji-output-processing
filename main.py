import argparse

# region - Set up description / arguments
from app.app import App

parser = argparse.ArgumentParser(description='Process FIJI output')
parser.add_argument('source',
                    metavar='S',
                    type=str,
                    help='The absolute path to FIJI output file to process')

args = parser.parse_args()

# endregion

# start the app
if __name__ == '__main__':
    App(args.source).run()
