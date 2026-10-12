import argparse
parser = argparse.ArgumentParser(description="Select a test run")
parser.add_argument("--browser", choices=["chromium", "firefox"], default="chromium")
parser.add_argument("--workers", type=int, default=1)
args = parser.parse_args([])  # Replace [] with no argument for real CLI input.
print(args.browser, args.workers)
