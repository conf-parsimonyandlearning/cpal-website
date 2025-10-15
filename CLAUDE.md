# PR instructions
- When preparing a PR, always make your changes in a new feature branch. This
  will allow the changes to easily be built locally to verify the website works
  correctly.
- README.md in _db describes basic workflows for preparing and updating the
  website's raw data.
  - `bundle` permissions are currently not enabled. `uv` permissions are. So you
    should build the website's Jekyll collection files when you edit the
    database (more below), but do not build the website itself. A build will be
    triggered by Github actions when a PR is created, via Cloudflare Pages
    integration. So the changes can be human-tested.
- The flow for updating the website is always to make any edits that can be made
  to the database to the database, then regenerate website .yaml files from
  there. Never directly edit derivative files.
  - When regenerating .yaml files, be aware that old files are not deleted. So
    in cases where a role changes or an organizer is removed, it will be
    necessary to manually delete some files. To do this in a clean way, all
    subdirectory files (e.g. contents of _organizers) can be deleted, as
    rebuilding the database will regenerate all the relevant ones.
- Unless otherwise specified, always make your updates to the most recent
  version of the website. E.g., if it is 2026, update the 2026 database, and
  only that database (not older years).

