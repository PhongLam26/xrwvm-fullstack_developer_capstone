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



React production build: passed. Docker API and sentiment images built; MongoDB seeded 50 dealers and 51 reviews. Curl evidence is in evidence/text. Full browser flow and cloud verification pending.
