def normalizeEmail(email):
    parts = email.split('@')
    local = parts[0].split('+')[0]
    newLocal = ''
    for c in local:
        if c != '.':
            newLocal += c
    return newLocal + '@' + parts[1]

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalizedEmails = set({})
        for email in emails:
            normalized = normalizeEmail(email)
            if normalized not in normalizedEmails:
                normalizedEmails.add(normalized)
        return len(normalizedEmails)