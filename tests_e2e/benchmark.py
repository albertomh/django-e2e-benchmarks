# >>> uv run tests_e2e/benchmark.py -n 3 --target playwright_e2e

import argparse
import json
import re
import statistics
import subprocess
from enum import Enum
from typing import TypedDict


class Target(str, Enum):
    PYDOLL = "pydoll_e2e"
    PLAYWRIGHT = "playwright_e2e"


class Stats(TypedDict):
    runs: int
    min: float
    max: float
    avg: float
    all: list[float]


PYTEST_TIME_PATTERN = re.compile(r"passed in ([0-9]+(?:\.[0-9]+)?)s")


def run_pytest(testdir: Target, n: int = 5, max_attempts: int | None = None) -> Stats:
    times: list[float] = []
    attempts = 0
    max_attempts = max_attempts or (n * 2)

    while len(times) < n and attempts < max_attempts:
        attempts += 1
        try:
            result = subprocess.run(
                ["uv", "run", "pytest", f"tests_e2e/{testdir.value}/"],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError:
            continue

        match = PYTEST_TIME_PATTERN.search(result.stdout + result.stderr)
        if match:
            times.append(float(match.group(1)))

    return {
        "runs": n,
        "min": min(times),
        "max": max(times),
        "avg": statistics.mean(times),
        "all": times,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="benchmark.py",
        description=(
            "Run end-to-end test suites multiple times and report timing statistics.\n\n"
            "Parses pytest's own reported runtime from the summary line "
            "and summarizes the minimum, maximum, and average times."
        ),
        epilog=(
            "Examples:\n"
            "  python benchmark.py --target pydoll_e2e -n 5\n"
            "  python benchmark.py --target playwright_e2e -n 10 --max-attempts 20\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--target",
        type=Target,
        choices=list(Target),
        default=Target.PLAYWRIGHT,
        help="Choose which test directory to run",
    )
    parser.add_argument(
        "-n",
        type=int,
        default=10,
        help="Number of times to run pytest",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        help="Max total attempts before giving up (default: 2x n)",
    )
    args = parser.parse_args()

    result = run_pytest(args.target, args.n, args.max_attempts)
    print(json.dumps(result, indent=4))  # noqa: T201
