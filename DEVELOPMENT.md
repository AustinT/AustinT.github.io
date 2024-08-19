# Development

Notes to myself on why/how I configured this website
and how to change it.

## Checklist for updating the website

1. Edit files as necessary (usually `.md` files or `conf.py`).
2. Check that:
  - Pages render correctly locally.
  - No links are broken accidentally.
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

I just used conda:

```bash
conda create --name nikola
conda activate nikola
pip install "Nikola[extras]"
```

## re-directing old links

<https://getnikola.com/handbook.html#redirections>
