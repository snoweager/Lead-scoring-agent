def calculate_score(row):
    """
    Calculate a Propensity-to-Buy score (0–100)
    based on weighted commercial and scientific signals.
    """

    score = 0

    # 1. Role Fit (High Weight)
    role_keywords = ["Director", "Head", "VP"]
    if any(keyword in row["Title"] for keyword in role_keywords):
        score += 30

    # 2. Company Intent / Budget Signal
    if row["Funding"] in ["Series A", "Series B"]:
        score += 20

    # 3. Scientific Intent (Very High Weight)
    if row["Recent_Publication"] == "Yes":
        score += 40

    # 4. Geographic Signal (Medium Weight)
    innovation_hubs = ["Boston", "Cambridge", "Basel", "Bay Area", "San Diego"]
    if any(hub in row["Company_HQ"] for hub in innovation_hubs):
        score += 10

    # Cap score at 100
    return min(score, 100)
