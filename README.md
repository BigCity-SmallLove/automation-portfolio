# Python Automation Portfolio

[View the live HTTPS portfolio](https://bigcity-smalllove.github.io/automation-portfolio/)

Static English portfolio for BigCity-SmallLove: Python automation, Windows desktop tools and offline security log analysis. Built with HTML, CSS and a small contact configuration script. No build dependencies, backend, analytics, forms or third-party fonts.

## Preview locally

Run `python -m http.server 8080 --directory site --bind 127.0.0.1`, then open http://127.0.0.1:8080. On Windows, `preview_windows.bat` starts the same loopback-only server. Stop it with Ctrl+C.

## Deploy

The Pages workflow validates the site and publishes only `site/`. Enable GitHub Actions in Settings → Pages, then run **Deploy portfolio**. Relative resources support this repository's project subpath. A successful deployment returns the actual Pages URL; do not assume an address is live before checking it.

## Edit

Content lives in `site/index.html`; visual styles in `site/assets/styles.css`. Confirmed contact links are configured in `site/contact-config.js`. Unconfirmed email stays empty. Screenshots show the actual applications with synthetic data and are reused from the reviewed software versions. Public source and Windows downloads are maintained in the independent showcase repositories.

For a business inquiry, use this repository's issue template. GitHub issues are public: never post credentials, customer records, private logs or confidential requirements.

MIT licensed. No customer endorsements, client counts or commercial results are claimed.
