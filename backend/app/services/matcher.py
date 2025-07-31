def find_matches(user, all_profiles):
    matches = []
    for other in all_profiles:
        if user == other:
            continue
        score = 0
        if set(user["zip_codes"]).intersection(other["zip_codes"]):
            score += 1
        if user["budget_min"] <= other["budget_max"] and user["budget_max"] >= other["budget_min"]:
            score += 1
        if user["sleep_schedule"] == other["sleep_schedule"]:
            score += 1
        if user["gender_pref"] == other["gender_identity"]:
            score += 1
        matches.append({"match": other, "score": score})
    return sorted(matches, key=lambda x: -x["score"])
