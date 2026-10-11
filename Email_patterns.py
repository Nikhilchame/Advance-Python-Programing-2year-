import re

# Email pattern
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

# Function to find emails in text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)

# Function to validate an email
def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# Input text
text = input("Enter text containing email addresses: ")

# Find emails
emails = find_emails(text)

print("\nEmail addresses found:")
for email in emails:
    print(email)

print("Total emails found:", len(emails))

# Validate a single email
email = input("\nEnter an email to validate: ")

if is_valid_email(email):
    print("VALID EMAIL")
else:
    print("INVALID EMAIL")