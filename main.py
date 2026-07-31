"""Start the LLX2026 desktop application from a source checkout."""

from pathlib import Path
import sys


SOURCE_ROOT = Path(__file__).resolve().parent / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from llx2026.gui import main


if __name__ == "__main__":
    main()
