# MAE598: Multi-Robot Systems
# Final Project: Multi-Robot Path Planning
# Team members: Rikenkumar Patel, Darsh Shah, Devang Kakadiya
# This code is the extension for sipp for multi-agent scenario.
import argparse
import yaml
from math import fabs
from graph_generation import SippGraph, State
from sipp import SippPlanner

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("map", help="input file containing map and dynamic obstacles")
    parser.add_argument("output", help="output file with the schedule")
    
    args = parser.parse_args()
    
    # Read Map
    with open(args.map, 'r') as map_file:
        try:
            map = yaml.load(map_file, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)

    # Output file
    output = dict()
    output["schedule"] = dict()

    for i in range(len(map["agents"])):
        sipp_planner = SippPlanner(map,i)
    
        if sipp_planner.compute_plan():
            plan = sipp_planner.get_plan()
            output["schedule"].update(plan)
            map["dynamic_obstacles"].update(plan)

            with open(args.output, 'w') as output_yaml:
                yaml.safe_dump(output, output_yaml)  
        else: 
            print("Plan not found")


if __name__ == "__main__":
    main()
