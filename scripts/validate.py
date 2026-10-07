from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parents[1]


def main() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
