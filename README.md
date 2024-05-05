# citadel-server

## endpoints

### auth

- `auth/jwt/create/` login: get jwt access & refresh tokens
- `auth/users/` signup: create user
- `auth/users/me/` get logged in user details
- `auth/o/google-oauth2/?state=<state>&code=<code>` google oauth login
- `auth/jwt/verify/` get access tokens using refresh tokens
- `auth/logout/` logout
- `auth/users/activation/` activate user from email link using { uid, token } in body
- `auth/users/reset_password/` reset password request
- `auth/users/reset_password_confirm/` reset password confirmation

### opinion

- `opinions/` get all opinions (paginated)
- `opinions/<slug>/` get a single opinion
- `opinions/?page=<pagenumber>` pagination
- `opinions/@<username>/` get opinions per username

### tags

- `tags/` get nested tags
- `tags/<slug>` get single tags **unused**
- `tags/opinions/<slug>` get opinions per tag
