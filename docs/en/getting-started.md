# Getting started

A short guide to working with the documentation portal locally.

## Run the local server

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000> in your browser. Changes to `.md` files reload automatically.

## Add a new page

1. Create a file, e.g. `docs/en/my-section/article.md`.
2. Register it in `nav` inside `mkdocs.yml`.

## Build the static site

```bash
mkdocs build
```

The result is generated into the `site/` folder.
