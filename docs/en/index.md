# Demo Documentation Portal

A learning portal built with the **Doc-as-Code** approach: all documentation lives in Markdown files, is previewed locally, and is published automatically. All content is fictional sample data.

[Getting started](getting-started.md){ .md-button .md-button--primary }

## Publishing workflow

```mermaid
graph TD
    A[Write Markdown] --> B{Git Commit}
    B --> C[GitHub Actions]
    C --> D[Deploy to GitHub Pages]
```

The platform is built on MkDocs with the Material for MkDocs theme. Build and deploy are automated via CI/CD following DocOps principles.
