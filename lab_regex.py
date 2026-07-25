'''
Lab: Redacted -- drilling regular expressions for extracting and redacting data.

Fill in the body of each function so that its doctests pass, then run

    python3 -m doctest lab_regex.py

and keep going until the command falls silent. Write every pattern as a raw
string (r'...'), and build it against real text at https://regex101.com before
you paste it in: regex is one of the few things an LLM will get confidently
wrong, so test the pattern, do not trust it.
'''

import re


def has_digit(text):
    '''
    Return True if text contains at least one digit, and False otherwise.

    >>> has_digit('Order #42 shipped')
    True
    >>> has_digit('no numbers here')
    False
    '''
    # TODO: your regex here (re.search returns a match or None -- wrap it in bool)
    pass


def find_numbers(text):
    '''
    Return a list of every run of consecutive digits in text, as strings.

    >>> find_numbers('I have 2 dogs and 10 cats')
    ['2', '10']
    >>> find_numbers('no numbers here')
    []
    '''
    # TODO: your regex here (re.findall with a quantifier)
    pass


def mask_digits(text):
    '''
    Return text with every digit replaced by a capital 'X'.

    >>> mask_digits('call 909-621-8000')
    'call XXX-XXX-XXXX'
    >>> mask_digits('no digits')
    'no digits'
    '''
    # TODO: your regex here (re.sub)
    pass


def find_hashtags(text):
    '''
    Return a list of the hashtags in text, each without its leading '#'.

    >>> find_hashtags('Big rally tonight! #MAGA #America #MAGA')
    ['MAGA', 'America', 'MAGA']
    >>> find_hashtags('no tags in this one')
    []
    '''
    # TODO: your regex here (match the '#', then capture the word after it)
    pass


def find_mentions(text):
    '''
    Return a list of the @-handles in text, each without its leading '@'.

    >>> find_mentions('thank you @FLOTUS and @VP, incredible work @FLOTUS')
    ['FLOTUS', 'VP', 'FLOTUS']
    >>> find_mentions('nobody is mentioned here')
    []
    '''
    # TODO: your regex here (a capture group, like find_hashtags)
    pass


def find_urls(text):
    '''
    Return a list of the http and https URLs in text.

    >>> find_urls('read more at https://kcna.kp today and http://example.com')
    ['https://kcna.kp', 'http://example.com']
    >>> find_urls('no links in this tweet')
    []
    '''
    # TODO: your regex here (make the 's' optional, then grab the non-spaces)
    pass


def find_phone_numbers(text):
    '''
    Return a list of the US phone numbers in text, in XXX-XXX-XXXX form.

    >>> find_phone_numbers('call 909-621-8000 or 213-555-0199 today')
    ['909-621-8000', '213-555-0199']
    >>> find_phone_numbers('no phone number here')
    []
    '''
    # TODO: your regex here (three digits, dash, three digits, dash, four digits)
    pass


def area_code(phone):
    '''
    Return the three-digit area code of a XXX-XXX-XXXX phone number.

    >>> area_code('909-621-8000')
    '909'
    >>> area_code('213-555-0199')
    '213'
    '''
    # TODO: your regex here (capture the first group, then read it with .group)
    pass


def redact_emails(text):
    '''
    Return text with every email address replaced by the string '[REDACTED]'.

    >>> redact_emails('reach me at ada@example.com or grace@navy.mil')
    'reach me at [REDACTED] or [REDACTED]'
    >>> redact_emails('this line has no email')
    'this line has no email'
    '''
    # TODO: your regex here (re.sub the email shape from the reading)
    pass


def redact_ssns(text):
    '''
    Return text with every US Social Security number masked as 'XXX-XX-XXXX'.

    >>> redact_ssns('SSN 123-45-6789 on file')
    'SSN XXX-XX-XXXX on file'
    >>> redact_ssns('no ssn in this record')
    'no ssn in this record'
    '''
    # TODO: your regex here (an SSN is three digits, two digits, four digits)
    pass


def mask_last_four(card):
    '''
    Return a 16-digit card number with all but its last four digits masked by '*'.

    >>> mask_last_four('1234567812345678')
    '************5678'
    >>> mask_last_four('4111111111111111')
    '************1111'
    '''
    # TODO: your regex here (mask each digit that still has four digits after it)
    pass


def is_valid_email(s):
    '''
    Return True if the whole string s is a single valid-looking email address.

    >>> is_valid_email('ada@example.com')
    True
    >>> is_valid_email('not-an-email')
    False
    >>> is_valid_email('ada@example.com and some extra text')
    False
    '''
    # TODO: your regex here (anchor the email shape with ^ and $, then bool it)
    pass
