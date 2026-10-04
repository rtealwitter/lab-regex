"""Rehearse the support-packet workflow using the student's regex helpers.

All supplied records are fictional. This demonstrates the specified patterns;
it is not a tool for removing every possible kind of personal information.
"""

import argparse
import json
from pathlib import Path

import lab_regex


STAGES = ('inspect', 'index', 'validate', 'redact')


def call_helper(name, argument, expected_type):
    """Stop at an unfinished helper instead of printing a misleading report."""
    result = getattr(lab_regex, name)(argument)
    if type(result) is not expected_type:
        raise ValueError(
            f'{name} returned {type(result).__name__}; expected {expected_type.__name__}. '
            f'Complete {name} in lab_regex.py and check its doctests before rerunning this stage.'
        )
    return result


def review(records, stage='all'):
    """Return each requested view without modifying the original records."""
    report = []
    for record in records:
        text = record['message']
        result = {'ticket': record['ticket']}
        if stage in ('inspect', 'all'):
            result['inspection'] = {
                'has_digit': call_helper('has_digit', text, bool),
                'numbers': call_helper('find_numbers', text, list),
                'masked_digits': call_helper('mask_digits', text, str),
            }
        if stage in ('index', 'all'):
            phones = call_helper('find_phone_numbers', text, list)
            result['index'] = {
                'phones': phones,
                'area_codes': [call_helper('area_code', phone, str) for phone in phones],
                'urls': call_helper('find_urls', text, list),
                'hashtags': call_helper('find_hashtags', text, list),
                'mentions': call_helper('find_mentions', text, list),
            }
        if stage in ('validate', 'all'):
            result['contact_is_valid'] = call_helper('is_valid_email', record['contact'], bool)
        if stage in ('redact', 'all'):
            result['edited'] = {
                'message': call_helper('redact_ssns', call_helper('redact_emails', text, str), str),
                'contact': call_helper('redact_emails', record['contact'], str),
                # The card helper receives just the 16-digit field.
                'card': call_helper('mask_last_four', record['card'], str),
            }
        report.append(result)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage', choices=(*STAGES, 'all'), default='all')
    args = parser.parse_args()
    source = Path(__file__).with_name('support_tickets.json')
    records = json.loads(source.read_text(encoding='utf-8'))
    print(json.dumps(review(records, args.stage), indent=2))


if __name__ == '__main__':
    main()
