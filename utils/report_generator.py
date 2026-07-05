# ==========================================
# AI Intelligence Report Generator
# ==========================================

def generate_report(

    country,
    incidents,
    fatalities,
    injuries,
    groups

):

    impact = (
        fatalities +
        injuries
    ) / max(
        incidents,
        1
    )

    if impact < 2:

        threat = "LOW"

    elif impact < 5:

        threat = "MEDIUM"

    else:

        threat = "HIGH"

    report = f"""
============================================================
             AI MILITARY INTELLIGENCE REPORT
============================================================

EXECUTIVE SUMMARY

The Global Terrorism Database (GTD) analysis identified
{incidents:,} terrorist incidents across multiple regions.

These incidents resulted in:

• Fatalities : {fatalities:,}

• Injuries   : {injuries:,}

• Active Terrorist Organizations : {groups}

Current Threat Assessment

• Threat Level : {threat}

• Highest Risk Country : {country}


============================================================
SITUATION OVERVIEW
============================================================

Historical GTD records indicate that terrorist activities
remain concentrated in specific geographical regions.

The selected country's historical incident frequency
suggests that continued intelligence monitoring
is necessary.

The current assessment is based on historical attack
patterns, casualties, geographical distribution,
and terrorist activity trends.


============================================================
THREAT ASSESSMENT
============================================================

Overall Risk Level : {threat}

The assessment indicates that security agencies should
continue monitoring emerging attack patterns,
terrorist organizations, and high-risk regions.

Predictive analytics suggest that historical trends
can assist intelligence agencies in resource planning
and strategic decision-making.


============================================================
STRATEGIC RECOMMENDATIONS
============================================================

1. Increase intelligence surveillance in high-risk areas.

2. Improve coordination between intelligence agencies.

3. Strengthen protection of critical infrastructure.

4. Increase monitoring of known terrorist organizations.

5. Continue AI-assisted threat forecasting.

6. Periodically retrain predictive models using
updated GTD records.


============================================================
FUTURE OUTLOOK
============================================================

Machine Learning and Artificial Intelligence can assist
security agencies by identifying historical patterns,
forecasting future trends, and supporting evidence-based
decision making.

The forecasting and prediction modules included in this
dashboard should be considered decision-support tools
rather than replacements for expert intelligence analysis.


============================================================
END OF REPORT
============================================================
"""

    return report