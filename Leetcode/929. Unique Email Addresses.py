"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

example:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2

Req:
-Return the number of unique emails following the rules
    -Find the base email
    -Place that email in a set
    -Return length of set

Approach:
-Initiate base_emails = set() to store base emails
-Iterate through the list
    -split the email at '@' to give local and domain name
    -split local name at '+' to remove anything after '+'
    -replace '.' with '' to remove all '.'
    -add local name and domain name into base_emails
-Return len(base_emails)
"""

def unique_email_address(emails):
    base_emails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        base_emails.add(local+'@'+domain)

    return len(base_emails)

# Testing

if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(unique_email_address(emails))