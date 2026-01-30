"""
Application Status Distribution Analytics
"""

def compute_application_status_distribution(data):
    """
    Computes count of applications per status.

    Returns:
        dict: status -> count
    """
    applications = data.get("applications", {})
    status_distribution = {}

    for application in applications.values():
        status = application.get("status", "unknown")

        if status not in status_distribution:
            status_distribution[status] = 1
        else:
            status_distribution[status] += 1

    return status_distribution
