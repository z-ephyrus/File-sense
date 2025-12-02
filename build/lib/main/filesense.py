import argparse
import json
import os
from .scanner import scanfile, scandirectory


def main():
    parser = argparse.ArgumentParser(
        description="Detect file types using magic bytes (powered by fleep)"
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--recursive", action="store_true", help="Recursively scan directories")

    args = parser.parse_args()
    results = []

    for path in args.paths:
        if os.path.isdir(path):
            if args.recursive:
                results.extend(scandirectory(path))
            else:
                print(f"Skipping directory (use --recursive)")
        else:
            results.append(scanfile(path))

    if args.json:
        print(json.dumps(results, indent=4))
    else:
        for r in results:
            print(f"\nFILE: {r['file']}")
            if "error" in r:
                print(f"  ERROR: {r['error']}")
            else:
                print(f"  Type: {r['type']}")
                print(f"  Extension: {r['extension']}")
                print(f"  MIME: {r['mime']}")
        print()
