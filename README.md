# Discord Email Validator

Give roles based on the domain of a verified email address.

- DM it your .edu email
- It sends you an email with a token
- DM it the token it tells you to, and you get the role


Config
-------

`.env`:
- DISCORD_TOKEN - token from discord developer menu
- EMAIL_USER - needs to be gmail or you should change the server to connect to in bot.py. also used as `from` addr
- EMAIL_PASS - password for smtp authentication

`schools.json`: Map from email domain to role name. These are resolved to actual roles when bot starts
