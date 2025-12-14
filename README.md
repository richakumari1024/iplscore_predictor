# 🏏 IPL Win Probability Predictor

### (Human Logic + NumPy | Explainable Analytics Project)

## Overview

This project is a *logic-driven IPL Win Probability Predictor* built using *pure Python and NumPy*, without relying on machine learning libraries.

Instead of treating match prediction as a black-box ML problem, this project models *how humans actually think during a cricket chase* — pressure, momentum, overs left, wickets in hand — and then translates that reasoning into clear mathematical logic.

The goal of this project is *understanding and explainability*, not perfect accuracy.

---

## Why This Project Exists

Most beginner projects:

* Import sklearn
* Train a model
* Cannot explain why the output makes sense

This project intentionally takes the opposite approach.

It focuses on:

* Feature reasoning
* Cricket intuition
* Mathematical clarity
* Explainable outputs

This makes it suitable for:

* Data Analyst roles
* Python logic rounds
* Sports analytics discussions
* Product & strategy interviews

---

## Problem Statement

Given a *20-over IPL chase, estimate the **probability that the batting team will win*, based on the current match situation.

The output is not just a number, but an *interpretable match state*, such as:

* Strongly Favourable
* Slightly Favourable
* Balanced
* Under Pressure

---

## Key Concepts Used

* Feature engineering from real-world context
* Normalization of inputs
* Phase-based reasoning (Powerplay / Middle / Death)
* Pressure modeling
* Momentum adjustment
* NumPy-based mathematical computation

No:

* Machine learning libraries
* Black-box models
* External datasets

---

## Input Features (Chase Situation)

Each match situation is described using:

| Feature           | Description               |
| ----------------- | ------------------------- |
| Runs Required     | Runs needed to win        |
| Balls Remaining   | Balls left in the innings |
| Wickets Remaining | Batting depth available   |
| Required Run Rate | Pressure indicator        |
| Current Run Rate  | Momentum indicator        |

---

## Human Reasoning Behind the Model

Cricket chases behave differently across phases:

* *Powerplay (balls > 84)*
  Early stage, lower pressure

* *Middle Overs (36–84 balls)*
  Match stabilizes, wickets matter more

* *Death Overs (< 36 balls)*
  Pressure amplifies, risk increases

This project *adjusts the impact of variables based on the phase*, instead of using a single flat formula.

---

## Core Logic (Simplified Explanation)

The model computes:

1. *Pressure Index* – how stressful the situation is
2. *Momentum* – whether the current scoring pace matches the requirement
3. *Phase Weight* – how late the match is

These factors are combined into a *win score*, which is then converted into a probability between 0 and 100%.

The probability is intentionally *clamped*, because cricket outcomes are never absolute.

---

## Example Output


{
  'Win Probability (%)': 71.4,
  'Match State': 'Strongly Favourable',
  'Pressure Index': 1.21,
  'Phase Weight': 1.3
}


This output tells a story, not just a number.

---

## Why NumPy Only?

Using NumPy forces:

* Clear data structures
* Explicit math
* No hiding behind libraries

Every line in this project can be *explained in plain English*, which is a critical skill for real-world analytics roles.

---

## Limitations (Honest)

This project:

* Uses synthetic data and logic
* Does not account for player skill
* Does not use real IPL ball-by-ball data
* Is not meant for betting or real predictions

Accuracy is *not the goal*.
Understanding and explainability *are*.

---

## What I Learned From This Project

* How to convert real-world reasoning into code
* Why feature choice matters more than algorithms
* How pressure and momentum affect outcomes
* Why many ML models fail due to poor problem framing
* How to explain technical work clearly

---

## Possible Extensions

* Add team strength ratings
* Include player strike rate effects
* Visualize win probability over balls
* Compare two teams dynamically
* Replace logic with learned weights later

---

## Who This Project Is For

* Students learning NumPy & logic
* Aspiring Data Analysts
* Anyone who wants to think before modeling
* Interviewers looking for clarity, not buzzwords

---

## Final Note

This project is intentionally simple, transparent, and explainable.

In real analytics work, **being able to explain your thinking clearly is more valuable than using
