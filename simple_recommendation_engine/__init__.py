import sys
import os

# Ensure the repo root is in sys.path so that weights_config,
# projects_data, etc. are importable from anywhere that imports
# this package — including on Streamlit Cloud where the CWD is
# not guaranteed to be the repo root.
_PKG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PKG_ROOT not in sys.path:
    sys.path.insert(0, _PKG_ROOT)
