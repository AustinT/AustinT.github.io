# Development

Notes to myself on why/how I configured this website
and how to change it.

## Checklist for updating the website

1. Edit files as necessary (usually `.md` files or `conf.py`).
2. Check that:
  - Pages render correctly locally.
  - No links are broken accidentally: `nikola check --check-links`
3. Commit changes on a separate branch, then merge to `src`.
4. Deploy using commands below

## How to deploy website

In correct python environment, run:

```bash
nikola check --clean-files  # remove unknown files accidentally added
nikola github_deploy
```

## How to build/serve locally

```bash
nikola auto --browser
```

## python environment with nikola

Dependencies are managed with [uv](https://docs.astral.sh/uv/) via `pyproject.toml`.

```bash
uv sync          # create/update the virtual environment
uv run nikola …  # run any nikola command
```

To add or change dependencies, edit `pyproject.toml` and re-run `uv sync`.

## re-directing old links

<https://getnikola.com/handbook.html#redirections>

## My thoughts on some design choices

(A reminder to my future self)

- KaTeX for math: apparently faster, but does not support all of LaTeX. Decided not to use (2025-01-05)
