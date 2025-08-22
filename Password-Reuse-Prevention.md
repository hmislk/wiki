# Password Reuse Prevention

## Overview

To enhance security, HMIS includes functionality to prevent users from reusing old passwords. This feature is configurable, allowing system administrators to enable or disable it based on organisational policy.

## Configuration

The behaviour is controlled via an **Application Config Option**:

* **Key:** `Prevent Password Reuse`
* **Type:** Boolean
* **Default:** `true`

When set to `true`, users are **not allowed** to reuse any of their previously used passwords.
When set to `false`, the system allows users to reset to an old password.

The option can be managed through the **ConfigOptionApplicationController** or directly via the administration interface.

## How It Works

1. **Password History Tracking**
   Each time a user successfully changes their password, the system stores a hash of the old password in the database, linked to that user.

2. **Validation During Password Change**
   When a user attempts to change their password:

   * The new password is hashed.
   * If `Prevent Password Reuse` is enabled, the hash is checked against the stored history.
   * If a match is found, the system rejects the change with a clear error message.

3. **Last Password Reset Timestamp**
   Along with history, the system updates the field `lastPasswordResetAt` for audit and expiration logic.
   This ensures that monthly expiration checks remain in sync with the new security rule.

4. **System Feedback**
   If a disallowed password is attempted:

   * The system informs the user that the new password matches a previously used one and cannot be set.

## Example Workflow

* **Prevent Password Reuse = true**

  * User changes password from `Pass@123` → `Pass@456` → `Pass@789`.
  * Later, attempting to reuse `Pass@123` will be blocked.

* **Prevent Password Reuse = false**

  * Same sequence as above, but reusing `Pass@123` is allowed.

## Related Features

* **Username Check**: Passwords cannot be the same as the username.
* **Complexity Rules**: Uppercase, lowercase, number, and special character are mandatory.
* **Expiration**: Passwords expire after 30 days and require renewal.

## References

* [[Issue #14441 – Users Must NOT be able to reuse old passwords](https://github.com/hmislk/hmis/issues/14441)](https://github.com/hmislk/hmis/issues/14441)
* [[Pull Request #14484 – Prevent Password Reuse](https://github.com/hmislk/hmis/pull/14484)](https://github.com/hmislk/hmis/pull/14484)


[Back](https://github.com/hmislk/hmis/wiki/System-Administration)