# Playwright QA Automation Portfolio

A UI test automation project built using **Python, Playwright, and Pytest** to demonstrate practical QA automation skills using the SauceDemo demo application.

The project focuses on building a maintainable automation framework using the **Page Object Model (POM)** design pattern, with functional test coverage that will expand as development progresses.

**Demo Application:** [SauceDemo](https://www.saucedemo.com/)

**Project Status:** In Progress — Ongoing Development and Enhancements

## Tech Stack

- **Python** — Programming language
- **Playwright** — Browser automation
- **Pytest** — Test execution and test management
- **Page Object Model (POM)** — Maintainable test architecture
- **Git and GitHub** — Version control and project hosting

## Current Test Coverage

### Login Module

| Test Case | Description | Status |
|---|---|---|
| LOGIN-001 | Verify login with valid credentials | Implemented |
| LOGIN-002 | Verify login with invalid credentials | Implemented |

Additional login scenarios and functional modules will be added as the project evolves.

## Getting Started

### Prerequisites

- Python installed
- Git installed

### 1. Clone the Repository

```bash
git clone https://github.com/oprexter/playwright-qa-automation-portfolio.git
cd playwright-qa-automation-portfolio
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Playwright Browser

```bash
python -m playwright install chromium
```

### 5. Execute the Tests

Run all tests:

```bash
pytest
```

Run the login tests:

```bash
pytest tests/test_login.py -v
```

## Upcoming Enhancements

The project is currently in the enhancement phase. Planned additions include:

- Expanded login validation scenarios
- Inventory and product validation
- Product sorting verification
- Shopping cart functionality
- Checkout workflow testing
- Enhanced test reporting and failure debugging
- CI/CD integration using GitHub Actions

Additional functionality, test scenarios, and framework improvements will be introduced incrementally as development continues.

## Project Scope

This is an independent QA automation portfolio project developed using a publicly accessible demo application. It is intended to demonstrate practical test automation skills and is not affiliated with Sauce Labs.

