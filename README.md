# torah-talmud

A static website for Torah and Talmud studies, built with Jekyll and automated deployment via GitHub Pages.

## Setup

This project uses Jekyll to generate a static website.

### Prerequisites

- Ruby (version 3.1 or later)
- Bundler

### Local Development

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

3. Open http://localhost:4000 in your browser.

### Deployment

The site is automatically built and deployed to GitHub Pages using GitHub Actions when you push to the `main` branch.

- The workflow builds the Jekyll site and deploys it to the `gh-pages` branch.
- GitHub Pages serves the site from the `gh-pages` branch.

To enable GitHub Pages:

1. Go to your repository settings.
2. Under "Pages", select "Deploy from a branch".
3. Choose the `gh-pages` branch and `/ (root)` folder.

### Content Generation

The website content is automatically generated from data files using a Python script with external integrations.

- **Data Source**: `_data/books.yml` contains basic information about Torah books and Talmud tractates.
- **Sefaria Integration**: Fetches sample texts from the Sefaria API (https://www.sefaria.org/api/).
- **AI Integration**: Uses OpenAI API to generate intelligent summaries (requires `OPENAI_API_KEY` secret).
- **Script**: `generate_content.py` creates Markdown pages with fetched data and AI-generated content.
- **Automation**: GitHub Actions runs the script before building the site.

#### Setting up AI Integration

1. Get an OpenAI API key from https://platform.openai.com/
2. Add it as a repository secret named `OPENAI_API_KEY` in GitHub Settings → Secrets and variables → Actions
3. The workflow will use it to generate enhanced summaries

#### Adding More Content

1. Update `_data/books.yml` with new entries.
2. Modify `generate_content.py` to handle additional data sources or API calls.
3. The workflow automatically generates pages on each push.

### Customization

- Modify `_config.yml` for site settings.
- Update the theme or plugins in `Gemfile` and `_config.yml`.