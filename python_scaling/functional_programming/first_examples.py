"""
The third-party "first" package provides a convenient way to return the
first item that matches a condition.

This file includes a local fallback so the examples still run even if the
package is not installed in the current environment.
"""

try:
    from first import first as package_first
except ImportError:
    package_first = None


def first(items, key=None, default=None):
    predicate = key or bool
    return next((item for item in items if predicate(item)), default)


# Return the first truthy value.
print(first([0, False, None, '', 42]))

# Use key=... to define a condition.
print(first([-1, 0, 1, 2], key=lambda x: x > 0))

# A more realistic example using dictionaries.
tickets = [
    {'id': 1, 'priority': 'low', 'resolved': True},
    {'id': 2, 'priority': 'medium', 'resolved': False},
    {'id': 3, 'priority': 'high', 'resolved': False},
]
print(
    first(
        tickets,
        key=lambda ticket: ticket['priority'] == 'high' and not ticket['resolved'],
        default='No urgent open ticket',
    )
)

# If the package exists, show the external implementation too.
if package_first is not None:
    print(package_first([-1, 0, 1, 2], key=lambda x: x > 0))
else:
    print('Install "first" to try the third-party package version.')
