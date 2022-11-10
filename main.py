import argparse

from app.application import Application

parser = argparse.ArgumentParser(description='Toy robot simulator')
parser.add_argument('-f', '--file', help='Use file as the source of commands instead of reading from command line')

application = Application()

def main():
    args = parser.parse_args()
    if not args.file:
        application.start_using_command_line()
    else:
        application.start_using_file(args.file)

if __name__ == '__main__':
    main()