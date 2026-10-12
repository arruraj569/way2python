import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--workers", type=int, default=1)
args = parser.parse_args(["--workers", "0"])
print(args.workers)
print(args.workers > 0)
