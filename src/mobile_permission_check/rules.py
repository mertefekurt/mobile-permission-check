from __future__ import annotations

from mobile_permission_check.models import Rule

PROJECT_NAME = 'mobile-permission-check'
SUMMARY = 'Audit mobile app permission notes for broad access and missing justification.'
SAMPLE_RISK = 'permission location_always justification missing background true'
SAMPLE_CLEAN = (
                   'permission location_when_in_use justification nearby stores background f'
                   'alse'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-justification',
        severity='high',
        pattern='justification\\s+(missing|none|unknown)',
        message='permission justification missing',
        recommendation='state user-facing reason',
    ),
    Rule(
        code='always-location',
        severity='medium',
        pattern='location_always',
        message='always location permission requested',
        recommendation='prefer when-in-use if possible',
    ),
    Rule(
        code='background-enabled',
        severity='low',
        pattern='background\\s+true',
        message='background behavior enabled',
        recommendation='verify need and disclosure',
    ),
)
