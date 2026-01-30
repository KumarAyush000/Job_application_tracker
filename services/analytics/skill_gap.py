"""
Skill Gap Analysis Module
Analyzes skill match between users and applied roles.
"""

def compute_skill_gap_per_application(data):
    """
    Computes skill gap analytics for each application.

    Returns:
        dict: application_id -> analytics summary
    """
    results = {}

    applications = data.get("applications", {})
    users = data.get("users", {})
    roles = data.get("roles", {})

    for app_id, application in applications.items():
        user_id = application.get("user_id")
        role_id = application.get("role_id")

        user = users.get(user_id)
        role = roles.get(role_id)

        # Defensive checks
        if user is None or role is None:
            continue

        user_skills = set(user.get("skills", []))
        required_skills = set(role.get("required_skills", []))

        matched_skills = user_skills.intersection(required_skills)
        missing_skills = required_skills.difference(user_skills)

        total_required = len(required_skills)
        match_percentage = (
            round((len(matched_skills) / total_required) * 100, 2)
            if total_required > 0 else 0
        )

        results[app_id] = {
            "user_id": user_id,
            "role_id": role_id,
            "matched_skills": list(matched_skills),
            "missing_skills": list(missing_skills),
            "match_percentage": match_percentage
        }

    return results
