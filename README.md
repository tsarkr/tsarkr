# tsarkr — Project Index

A collection of personal and research projects focused on Korean cultural heritage, text mining, and data collection/analysis.

Main repositories

- [shortener_11e](https://github.com/tsarkr/shortener_11e) — PHP-based URL shortener (11e.kr)
- [k-heritage](https://github.com/tsarkr/k-heritage) — YouTube comment text mining and analysis for K-Heritage
- [redditgo](https://github.com/tsarkr/redditgo) — Multilingual (Korean/Chinese/Japanese) Reddit collection and sentiment analysis
- [kci_scrape](https://github.com/tsarkr/kci_scrape) — KCI paper scraping and co-authorship network visualization
- [K-D-H](https://github.com/tsarkr/K-D-H) — K-pop related analysis and data projects
- [docent](https://github.com/tsarkr/docent) — Research tools and utilities
 - [darkstar](https://github.com/tsarkr/darkstar) — Rust-based ontology management tool (Protégé alternative)

Project details

- shortener_11e (PHP)
	- Purpose: Provide a lightweight URL shortening service for internal use and public demo at 11e.kr.
	- Tech: PHP, MySQL (or SQLite), simple routing and redirect logic.
	- Status: Production/demo available; accepts improvements for analytics and security.
	- Quick start: See repository `README.md` for installation and configuration.

- k-heritage (Python)
	- Purpose: Collect and analyze YouTube comments from the K-Heritage channel to study audience feedback and themes.
	- Tech: Python, pandas, scikit-learn / transformers (optional), NLTK / KoNLPy for Korean text processing, Jupyter notebooks for exploration.
	- Status: Research code and notebooks; includes data collection and basic topic/sentiment analysis pipelines.
	- Quick start: Clone the repo, create a Python virtualenv, install requirements, and run the notebooks in `notebooks/`.

- redditgo (Python)
	- Purpose: Crawl Reddit communities in Korean, Chinese, and Japanese to analyze sentiment shifts over time (COVID-19 case study).
	- Tech: Python, PRAW or Pushshift API clients, lang-specific tokenizers, sentiment lexicons or transformer models for classification.
	- Status: Data collection scripts and analysis notebooks present; extensible for new subreddits and languages.
	- Quick start: Configure API credentials, run `scripts/collect.py` to gather posts and comments, then run analysis notebooks.

- kci_scrape (Python)
	- Purpose: Scrape KCI (Korean Citation Index) metadata and papers to map research trends and co-authorship networks in cultural heritage curation.
	- Tech: Python, requests/BeautifulSoup (or Scrapy), NetworkX / Gephi exports for network visualization, pandas for processing.
	- Status: Scrapers and visualization scripts available; may require updates for site changes and rate-limiting handling.
	- Quick start: Inspect `scrapers/` for available scripts; run with caution and respect robots.txt and site terms.

- K-D-H (Python)
	- Purpose: K-pop related data analysis (lyrics, fandom activity, network metrics) and experimental models.
	- Tech: Python, NLP toolchains, data visualization libraries.
	- Status: Experimental analyses and dataset prep scripts.
	- Quick start: See `README.md` in the repository for dataset sources and preprocessing steps.

- docent (Python / tools)
	- Purpose: Utility tools and helper libraries used across research projects (data loaders, annotation helpers, small services).
	- Tech: Python packages, CLI scripts.
	- Status: Active development; used as internal dependency for other repos.
	- Quick start: Install as a Python package in editable mode (if used locally) and read module docs.

 - darkstar (Rust)
	- Purpose: A Rust-based alternative to Protégé for ontology creation, editing, validation, and lightweight reasoning. Targets scripted and web workflows for ontology management and automated pipelines.
	- Tech: Rust, Cargo, RDF/OWL libraries (e.g. Oxigraph/Sophia), SPARQL support; optional WASM/web frontend for UI.
	- Status: Prototype; early-stage but usable for scripted ontology workflows and integrations.
	- Quick start: Clone the repo and run `cargo build` / `cargo run`; see the repository `README.md` for example workflows and usage.

Project summary

- Purpose: Develop reproducible analysis pipelines and tooling for cultural heritage and content analysis, including data collection and processing.
- Key technologies: Python, PHP, Rust, text mining, network analysis.

Quick start

- Each project has its own repository with installation and usage instructions. Open the repository you are interested in and read its `README.md` for details.

Contributing and usage

- Most projects are intended for research and learning purposes. Contributions are welcome; please open an issue first to discuss major changes.

License

- If an individual repository does not specify a license, `MIT` is recommended by default. See the `LICENSE` file in each repository for specifics.

Contact

- Personal site: https://gyungmin.tsar.kr/
- GitHub profile: https://github.com/tsarkr

Repository organization suggestions

- Monorepo (optional): Projects can be consolidated under a `packages/` directory and share common CI workflows if desired.
- Topics and descriptions: Improve discoverability by updating each repository's GitHub `description` and `topics` (e.g. `text-mining`, `heritage`, `data-scraping`).

---
_Last updated: 2026-05-15_
