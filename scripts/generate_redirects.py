#!/usr/bin/env python3
"""Generate HTML redirect files for legacy URLs after quarto render."""

import argparse
import os

REDIRECTS = {
    "links": "/resources/",
    "about": "/",
}

TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
  <title>Redirecting...</title>
</head>
<body>
  <p>Redirecting to <a href="{target}">{target}</a>...</p>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Generate redirect HTML files")
    parser.add_argument(
        "--output-dir",
        default=os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "src/_site"),
        help="Quarto output directory (default: $QUARTO_PROJECT_OUTPUT_DIR or src/_site)",
    )
    args = parser.parse_args()

    for slug, target in REDIRECTS.items():
        out_dir = os.path.join(args.output_dir, slug)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(TEMPLATE.format(target=target))
        print(f"Created redirect: /{slug}/ -> {target}")


if __name__ == "__main__":
    main()
