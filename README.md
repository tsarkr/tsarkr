# tsarkr — Project Index

A collection of personal and research projects focused on Korean cultural heritage, text mining, and data collection/analysis.

Main repositories

- [D-CENT](https://github.com/tsarkr/docent) — Digital Contextualized Entity & Narrative Technology
- [DarkStar](https://github.com/tsarkr/darkstar) — Rust-based ontology management tool (Protégé alternative)
- [K-D-H](https://github.com/tsarkr/K-D-H) — K-pop related analysis and data projects
- [Hexedit](https://github.com/tsarkr/Hexedit) — Web-based hexadecimal editor built with React, TypeScript, and Vite

Project details

- D-CENT (Python / core engine)
	- Purpose: Foundational utility tools and libraries supporting the D-CENT research framework (data loaders, structural parsers, semantic services).
	- Tech: Python packages, CLI scripts.
	- Status: Active development; serves as the core dependency for the D-CENT research pipeline.
	- Quick start: Install as a Python package in editable mode (if used locally) and read module docs.

- DarkStar (Rust)
	- Purpose: A Rust-based alternative to Protégé for ontology creation, editing, validation, and lightweight reasoning. Targets scripted and web workflows for ontology management and automated pipelines.
	- Tech: Rust, Cargo, RDF/OWL libraries (e.g. Oxigraph/Sophia), SPARQL support; optional WASM/web frontend for UI.
	- Status: Prototype; early-stage but usable for scripted ontology workflows and integrations.
	- Quick start: Clone the repo and run `cargo build` / `cargo run`; see the repository `README.md` for example workflows and usage.

- K-D-H (Python)
	- Purpose: K-pop related data analysis (lyrics, fandom activity, network metrics) and experimental models.
	- Tech: Python, NLP toolchains, data visualization libraries.
	- Status: Experimental analyses and dataset prep scripts.
	- Quick start: See `README.md` in the repository for dataset sources and preprocessing steps.

- Hexedit (React / TypeScript / Vite)
	- Purpose: Provide a fast, interactive web-based hexadecimal editor and binary inspection tool in the browser.
	- Tech: React, TypeScript, Vite.
	- Status: Active development.
	- Quick start: Clone the repo, run `npm install` and `npm run dev` to launch the local development server.

Project summary

- Purpose: Develop reproducible analysis pipelines, ontology/semantic frameworks, and interactive web tools for cultural heritage and data analysis.
- Key technologies: Python, Rust, React, TypeScript, Vite, ontology management, text mining, network analysis.

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
_Last updated: 2026-11-01_
