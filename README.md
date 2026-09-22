[![Django CI](https://github.com/twonfi/twonum.org/actions/workflows/django.yml/badge.svg)](https://github.com/twonfi/twonum.org/actions/workflows/django.yml)
[![license | AGPLv3](https://img.shields.io/badge/license-AGPLv3-purple)](https://www.gnu.org/licenses/agpl-3.0.html)

# twonum.org: My long-overdue personal website
This is my personal website. [See it for yourself.](https://www.twonum.org)

The codebase is a mess, so I'm not explaining it, but do email me if you dig around the code and find some interesting things.

## Cookies
- A `csrftoken` is set for every user using twonum.org for security purposes (to prevent cross-site request forgery attacks). This is set by the Django security middleware.
- Time-zone detection may set a non-tracking cookie used to automatically change time zones.
- Session tokens and other cookies are only set when logged in, which only Cadence (the admin) has access to.
- Login attempts are logged by allauth and IP addresses may be collected. Again, login is admin-only, so you shouldn't be digging around the auth anyway.

## Contributions and AI
**twonum.org is 100% Cadence-written code and no generative "artificial intelligence" was used.** In fact, the twonum.org software attempts to block obvious AI crawler attempts and robots.txt is enforced.

Due to the nature of the project, unless the fix is a serious security issue, please do not try to contribute any code. If you have something, please [contact me](https://www.twonum.org/contact/) (does not include any guest blog posts).

## License
twonum.org uses <abbr title="Affero General Purpose License version 3">AGPLv3</abbr>
and <abbr title="Creative Commons Attribution-ShareAlike 4.0 International">CC BY-SA 4.0</abbr>.
See [COPYING](./COPYING) for how these licenses are applied.

The reason for AGPLv3 is that twonum.org is my personal website, which is much more different than, say,
[ClubFeed](//github.com/twonfi/clubfeed), a general-purpose application.
