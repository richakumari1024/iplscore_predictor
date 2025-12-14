import numpy as np

def advanced_win_probability(
    runs_required,
    balls_remaining,
    wickets_remaining,
    target,
    current_run_rate
):
    # required run rate
    rrr = (runs_required * 6) / balls_remaining

    # phase weight
    if balls_remaining > 84:
        phase_weight = 0.8
    elif balls_remaining > 36:
        phase_weight = 1.0
    else:
        phase_weight = 1.3

    # pressure index
    pressure = (
        (rrr / 12)
        + (1 - wickets_remaining / 10)
        + (1 - balls_remaining / 120)
    )

    # momentum
    momentum = current_run_rate / rrr

    # win score (human logic)
    win_score = (
        (wickets_remaining / 10)
        + (balls_remaining / 120)
        + (momentum - 1)
        - pressure
    )

    # apply phase weight
    win_score *= phase_weight

    # probability
    probability = np.clip(0.5 + win_score, 0, 1)

    # interpretation
    if probability > 0.7:
        state = "Strongly Favourable"
    elif probability > 0.55:
        state = "Slightly Favourable"
    elif probability > 0.45:
        state = "Balanced"
    else:
        state = "Under Pressure"

    return {
        "Win Probability (%)": round(probability * 100, 2),
        "Match State": state,
        "Pressure Index": round(pressure, 2),
        "Phase Weight": phase_weight
    }