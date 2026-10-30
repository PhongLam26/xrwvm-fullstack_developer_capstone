# Test report

Django tests (mocked service boundaries):

Found 6 test(s).
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, djangoapp, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying djangoapp.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

test_authenticated_review_uses_session_name (djangoapp.tests.AuthenticationTests.test_authenticated_review_uses_session_name) ... ok
test_catalog_seed_idempotent (djangoapp.tests.AuthenticationTests.test_catalog_seed_idempotent) ... ok
test_csrf_enforced (djangoapp.tests.AuthenticationTests.test_csrf_enforced) ... ok
test_dealer_proxy_and_state (djangoapp.tests.AuthenticationTests.test_dealer_proxy_and_state) ... ok
test_login_failure_logout_and_revoked_session (djangoapp.tests.AuthenticationTests.test_login_failure_logout_and_revoked_session) ... ok
test_registration_duplicate_and_password_hash (djangoapp.tests.AuthenticationTests.test_registration_duplicate_and_password_hash) ... ok

----------------------------------------------------------------------
Ran 6 tests in 3.118s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...



React production build: passed. Docker API and sentiment images built; MongoDB seeded 50 dealers and 51 reviews. Curl evidence is in evidence/text. Browser review and admin flows are now verified below. Cloud deployment omitted at user request.


## Final verification — 2026-10-30, Asia/Saigon

- Django system check: passed. `python manage.py check`.
- Live integration: **15 checks passed** against the running services, including all seven page routes, all dealers, Kansas, missing dealer, catalog, sentiment, saved review, anonymous review rejection and admin protection. Actual responses: `evidence/text/live_integration.json`.
- Latest Django suite: **9 tests passed** with `python manage.py test --verbosity 2`. Actual output: `evidence/text/django_tests.txt`. Includes admin username/root display and logout protection, authentication, CSRF, registration duplicates/password hashing, catalog, dealer filtering, missing dealer 404, service failure 502 and authenticated review attribution. Service boundaries in unit tests are mocked.
- Real browser: Chrome window captured through Computer Use, including its actual address bar. All eight requested local screenshots exist and were visually inspected.
- Admin: logged in with existing root credentials; dashboard shows ROOT. Logged out through the POST form; reopening /admin/ shows the login page. No password is committed.
- Real review flow: entered review/date/car/year in React form, saved the pre-submit screenshot, submitted through Django/Express, then reloaded the detail page. Review ID 52 is persisted for dealer 8, attributed to Demo Driver and classified positive. Backend GET independently confirms it: `evidence/text/added_review_backend`.
- Previously captured Q17/Q18 screenshots were visually verified: signed-in user and Review Dealer links are visible; Kansas filter shows dealer 8 and the correct URL.
- GitHub repository is PUBLIC on main. Required README/About/Contact/Register files verified through GitHub contents API.
- CI: real successful runner output and all job steps saved in `evidence/text/CICD`, `CICD-run.json` and `CICD-full.txt`. Latest source commit `ff1e55641e0488e6821fc91040e42f95ee6e23b6` passed: https://github.com/PhongLam26/xrwvm-fullstack_developer_capstone/actions/runs/41077796961. Evidence-only commits do not trigger redundant builds.
- IBM deployment: excluded at user request; no production result is claimed.

## IBM and grading-feedback update

10 Django tests passed, including CSRF-protected legacy GET logout. Python flake8 and JavaScript JSHint passed in separate real GitHub Actions jobs in run 41084078460; checks and Docker images also passed. Source commit bb49408. Both lint job steps and IDs appear in evidence/text/CICD, with full logs in CICD-full.txt.

IBM Code Engine homepage, authentication, APIs and review storage/reload verified. Four deployment screenshots captured from Chrome with genuine browser chrome. See cloud_verification.json. Production durability across container replacement remains incomplete. Previous assessment: 29/50; updated submission not graded.
