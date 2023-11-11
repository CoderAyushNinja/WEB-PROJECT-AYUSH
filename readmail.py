import imaplib
import email
from email.header import decode_header

# Your email credentials
email_user = "www.mankumar@gmail.com"
email_pass = "jlmjdmljukwdxlxn"

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your email account
mail.login(email_user, email_pass)

# Select the mailbox you want to read emails from (e.g., "inbox")
mail.select("inbox")

# Search for emails based on criteria (in this case, all emails)
status, email_ids = mail.search(None, "ALL")
# Fetch and print emails
for email_id in email_ids[0].split():
    status, email_data = mail.fetch(email_id, "(RFC822)")
    
    raw_email = email_data[0][1]
    msg = email.message_from_bytes(raw_email)
    
    subject, encoding = decode_header(msg["Subject"])[0]
    if encoding:
        subject = subject.decode(encoding)
    
    from_ = msg.get("From")
    
    print(f"From: {from_}\nSubject: {subject}")
    
    # You can also access the email body using msg.get_payload()

# Logout from the email account
mail.logout()
