# MAE598: Multi-Robot Systems
# Final Project: Multi-Robot Path Planning
# Team members: Rikenkumar Patel, Darsh Shah, Devang Kakadiya
import velocity_obstacle.velocity_obstacle as velocity_obstacle
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--mode", help="mode of obstacle avoidance; option: velocity_obstacle")
    parser.add_argument(
        "-f", "--filename", help="filename, in case you want to save the animation")

    args = parser.parse_args()
    if args.mode == "velocity_obstacle":
        velocity_obstacle.simulate(args.filename)
    else:
        print("Please enter mode the desired mode: velocity_obstacle")
