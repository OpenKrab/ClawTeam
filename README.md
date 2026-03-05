# ClawTeam

ClawTeam — Hierarchical AI Organization Simulator for OpenKrab/Krab. Build your AI company with CEO, CTO, CFO, departments, and teams 🦞🏢

## Features

- Define org chart จาก YAML (CEO, CTO, CFO...)
- Delegate tasks ตาม hierarchy
- Integrate ClawTeam, ClawGraph, ClawSandbox
- Visualize org chart (Mermaid/NetworkX)

## Installation

```bash
pip install -r requirements.txt
```

Or via ClawFlow:

```bash
clawflow install openkrab/claw-team
```

## Usage

```python
from src.org.organization import ClawTeam

org = ClawTeam()
result = org.run_task("Develop ClawGraph v2")
org.visualize_org()
```

## Configuration

Edit `config.yaml` to define your organizational structure.

## Roadmap

- v0.2: Integrate ClawGraph for shared knowledge
- v0.3: Auto-delegate with LLM
- v0.4: ClawSandbox integration
- v0.5: Dashboard UI
- v0.6: Reward system