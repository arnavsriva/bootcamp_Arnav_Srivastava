# bootcamp_Arnav_Srivastava

A clean, git-first scaffold for my bootcamp coursework and capstone project.

## Layout
```text
bootcamp_Arnav_Srivastava/
├── homework/
│   ├── stage01_problem-framing-and-scoping/
│   ├── stage02_tooling-setup_slides-outline/
│   ├── stage03_python-fundamentals/
│   ├── stage04_data-acquisition-and-ingestion/
│   ├── stage05_data-storage/
│   ├── stage06_data-preprocessing/
│   └── stage07_outliers-risk-assumptions/
├── project/
│   ├── data/
│   │   ├── raw/         # (gitignored; .gitkeep tracked)
│   │   └── processed/   # (gitignored; .gitkeep tracked)
│   ├── docs/
│   ├── notebooks/
│   └── src/
└── class_materials/
```

## Getting Started
1. Create a Python virtualenv: `python -m venv .venv && source .venv/bin/activate`
2. Install common tooling (optional): `pip install jupyter numpy pandas matplotlib`
3. Keep large/raw data out of git; place raw files in `project/data/raw/`.

## Contributing (to self)
- Branch off `main`; open PRs if collaborating.
- Write clear commit messages (e.g., Conventional Commits).

