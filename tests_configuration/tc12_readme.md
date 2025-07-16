Here's the corrected version in English:

# ⚙️ CentOS Script Repository for UA-1378 TAQC Students

This README provides instructions for setting up a CentOS virtual machine for the `tc12_max_mail_length_test`:
- Verify successful email delivery with 333 characters in the body
- Verify mail rejection with 334 characters in the body  

---

## Setup

Create a file with email body check rules:
```cmd
sudo nano /etc/postfix/body_checks
```

---

Add the following rule:
```cmd
/^.{334,}/ REJECT Message body too long (max 333 characters allowed)
```

---

Compile the file into Postfix DB format:
```cmd
sudo postmap /etc/postfix/body_checks
```
This will create `/etc/postfix/body_checks.db`.

---

Then open `main.cf`:
```cmd
sudo nano /etc/postfix/main.cf
```
and add:
```cmd
body_checks = regexp:/etc/postfix/body_checks
```

---

Restart Postfix:
```cmd
sudo systemctl restart postfix
```

---

This brief tutorial will ensure the `tc12_max_mail_length_test` works correctly.
