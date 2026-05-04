

1. Model Overview

We model football matches using a Bayesian Poisson model with team-specific parameters.

Goal model

Each match is generated as:

Home goals ~ Poisson(λ_home)
Away goals ~ Poisson(λ_away)

with:

λ_home = exp(attack_home − defense_away + γ)
λ_away = exp(attack_away − defense_home)

Components

* attack_i: offensive strength of team i
* defense_i: defensive weakness (higher = worse defense)
* γ: home advantage (log-scale)

⸻

2. Why exp(...) is used

We model:

log(λ) = linear combination

and transform via:

λ = exp(...)

Reasons

* Ensures λ > 0 (required for Poisson)
* Turns additive effects into multiplicative goal effects
* Standard Poisson regression (log-link)

Interpretation

+0.2 attack → exp(0.2) ≈ +22% expected goals

⸻

3. Match Outcome Probabilities

Define goal difference:

D = Home goals − Away goals

Then:

* Home win ⇔ D > 0
* Draw ⇔ D = 0
* Away win ⇔ D < 0

We use:

D ~ Skellam(λ_home, λ_away)

Probabilities

P(home win) = P(D > 0)
P(draw)     = P(D = 0)
P(away win) = P(D < 0)

⸻

4. Scoreline Distribution (Heatmap)

We compute full joint probabilities:

P(i, j) = Poisson(i | λ_home) × Poisson(j | λ_away)

This gives:

* Full score distribution
* Heatmap visualization

Outcome probabilities are:

* sum(i > j) → home win
* sum(i = j) → draw
* sum(i < j) → away win

⸻

5. Bayesian Inference

Parameters are not fixed — we use posterior samples:

attack^(s), defense^(s), γ^(s)

For each draw:

* compute λ_home^(s), λ_away^(s)
* compute probabilities

Final probabilities:

average over posterior draws

This incorporates parameter uncertainty.

⸻

6. Unknown Teams Handling

If a team is not present in training data:

attack = 0
defense = 0

This corresponds to a league-average team.

Flags added

{
  "unknown_team": true,
  "unknown_home": true/false,
  "unknown_away": true/false
}

Interpretation

* Model falls back to baseline assumptions
* Prediction is structurally less reliable

⸻

7. Competition Formats

League matches

Output:

p_home_win
p_draw
p_away_win

Knockout matches

Draws are resolved:

p_home_advance = p_home_win + 0.5 * p_draw
p_away_advance = p_away_win + 0.5 * p_draw

⸻

8. Frontend Representation

Each match shows:

* Expected goals (λ_home, λ_away)
* Outcome probabilities
* Most likely score
* Score heatmap

Additional UI signals

* Knockout / League tag
* Unknown team warning

⸻

9. Key Insights

Model intuition

Each team generates goals independently,
and the result depends on the distribution of their difference.

⸻

λ interpretation

* λ is expected goals, not actual goals
* λ ∈ (0, ∞), can be very small

Example:

λ = 0.5 → ~60% chance of scoring 0 goals

⸻

Attack / Defense interpretation

* Attack ↑ → more goals scored
* Defense ↑ → more goals conceded

For visualization:

display_defense = -defense

so that “higher = better” for users.

⸻

10. Model Limitations

* Assumes independence between teams
* Does not model game state dynamics
* No overdispersion handling
* No explicit extra-time modeling

⸻

11. Pipeline Overview

Stan fit
  ↓
Generate predictions
  ↓
Export JSON (predictions, performance)
  ↓
Publish to /docs (GitHub Pages)
  ↓
Frontend consumes predictions.json

⸻

12. Next Steps (Planned)

* Visualize:
    * Attack distributions
    * Defense distributions
    * Home advantage
* Filter to current Allsvenskan teams
* Possibly expose via README or frontend

⸻

One-line summary

A Bayesian Poisson model estimates team strengths, converts them into expected goals, and derives match outcome probabilities via the distribution of goal differences.