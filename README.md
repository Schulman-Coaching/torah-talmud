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

### Adding Content

- Edit `index.md` for the home page.
- Add new pages in the root or `_pages` directory.
- Use Markdown for content.

### Customization

- Modify `_config.yml` for site settings.
- Update the theme or plugins in `Gemfile` and `_config.yml`.