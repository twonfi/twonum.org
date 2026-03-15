/*
 * Copyright (C) 2026 twonum
 *
 * twonum.org is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * twonum.org is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this twonum.org.  If not, see <https://www.gnu.org/licenses/>.
 */
const ENCODED_EMAIL_STRING = 'dHdvQHR3b251bS5vcmc=';

function displayEmail() {
  if (!confirm('Click CANCEL or press Esc to get my email.')) {
    const email = atob(ENCODED_EMAIL_STRING);
    console.log(email);
    document.getElementById('email-output')
        .innerHTML = `<a href="mailto:${email}">${email}</a>`;
    document.getElementById('display-email-button').hidden = true;
  } else {
    alert('Try again, but > click Cancel < or press Esc this time.');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('display-email-button')
      .addEventListener('click', displayEmail);
});
