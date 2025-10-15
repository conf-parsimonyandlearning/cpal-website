# PR instructions
- When preparing a PR, always make your changes in a new feature branch. This
  will allow the changes to easily be built locally to verify the website works
  correctly.
- README.md in _db describes basic workflows for preparing and updating the
  website's raw data.
- The flow for updating the website is always to make any edits that can be made
  to the database to the database, then regenerate website .yaml files from
  there. Never directly edit derivative files.
- Unless otherwise specified, always make your updates to the most recent
  version of the website. E.g., if it is 2026, update the 2026 database, and
  only that database (not older years).
- The website should be built with `bundle exec jekyll build`.

