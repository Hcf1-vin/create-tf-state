import os
import argparse

def get_attribute(att_location):
    cwd = os.getcwd()

    return cwd.split("/")[int(att_location)]

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--type', help='name of aws profile',default="project")

    args=parser.parse_args()

    if args.type == "project" or args.type == "Project" or args.type == "PROJECT":
        att_location = "-3"

    if args.type == "env" or args.type == "Env" or args.type == "ENV":
        att_location = "-2"

    if args.type == "region" or args.type == "Region" or args.type == "REGION":
        att_location = "-1"

    r = get_attribute(att_location)
    print(r)