# Smart Public Transportation Fare & Sustainability Calculator

## SDG 11 – Sustainable Cities and Communities

The Smart Public Transportation Fare & Sustainability Calculator is a Python-based console application developed to support the Sustainable Development Goal 11 (SDG 11): Sustainable Cities and Communities.

The console based application, written using the Python programming language will be effective in helping users to compare amonmg different options of public transportation that is stated based on fare amount, travel time and the CO2 emmision. Upon comparing these, it then recommends the most suitable transportation option that matches the affordability and sustainability.  
---

## Problem Statement

People may have several public transportation options available but may not know which option provides a good balance between cost, travel time, and environmental impact.

This application provides a simple way for users to compare transportation choices and make more informed and sustainable travel decisions.

---

## Project Objectives

The main objectives of this project are to:

- Calculate transportation fares based on distance and passenger type.
- Estimate travel time for different transportation options.
- Calculate estimated CO₂ emissions.
- Provide sustainability ratings for transportation options.
- Compare Bus, MRT, LRT, and Train.
- Recommend the most sustainable transportation option.
- Encourage sustainable transportation choices in support of SDG 11.

---

## Transportation Options

The application compares:

| Transport | Fare/km | Speed (km/h) | CO₂ (g/km/passenger) |
|-----------|---------|--------------|----------------------|
| Bus | RM 0.15 | 30 | 40 |
| MRT | RM 0.20 | 60 | 70 |
| LRT | RM 0.18 | 45 | 70 |
| Train | RM 0.25 | 80 | 90 |

---

## Features

### 1. Calculate Trip & Compare Options

Users enter:

- Starting point
- Destination
- Distance
- Number of passengers
- Passenger type
- Trip type

The system calculates and compares all available transportation options.

### 2. View Transport Information

Displays information about:

- Fare per kilometre
- Average speed
- CO₂ emissions
- Sustainability rating

### 3. View Sustainability Guidelines

Provides CO₂ sustainability thresholds and tips for more sustainable travel.

### 4. Recommendation

The application identifies the most sustainable transportation option and provides information about:

- Total fare
- Travel time
- CO₂ emissions
- Sustainability rating

---

## Passenger Types

The application supports:

- Adult
- Student
- Senior
- Child

Different fare multipliers are applied depending on the passenger type.

---

## Trip Types

Users can select:

- One-way
- Return

---

## Sustainability Ratings

Transportation options are classified based on estimated CO₂ emissions:

| CO₂ Emissions | Rating |
|---------------|--------|
| ≤ 30 g/km/passenger | Excellent |
| ≤ 50 g/km/passenger | Good |
| ≤ 80 g/km/passenger | Fair |
| > 80 g/km/passenger | Poor |

---

## Computational Thinking

The project demonstrates the following computational thinking concepts:

### Decomposition

The application is divided into separate Python modules:

- `main.py` – Main program and menu
- `data.py` – Data and Transport class
- `input.py` – Input handling and validation
- `calculation.py` – Calculations and recommendation logic
- `display.py` – Results and output formatting
- `info_views.py` – Transportation and sustainability information

### Abstraction

The `Transport` class represents common information about different transportation options such as fare, speed, and CO₂ emissions.

### Pattern Recognition

The same calculation process is applied to all transportation options, allowing the program to compare Bus, MRT, LRT, and Train using the same rules.

### Algorithmic Thinking

The application follows a sequence of:

1. Collect user information.
2. Validate the input.
3. Calculate transportation results.
4. Compare the available options.
5. Identify the best option.
6. Display the results and recommendation.

---

## Project Structure

```text
transport_calculator/
│
├── main.py
├── data.py
├── input.py
├── calculation.py
├── display.py
├── info_views.py
└── README.md
