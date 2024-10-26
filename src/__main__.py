from app import Yggdia
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='yggdia', description='A CLI based dialogue tree editor.')
    parser.add_argument("filename", help="filename of the JSON file with the dialogue tree you want to edit")
    args = parser.parse_args()
 
    app = Yggdia(args.filename)
    app.run()