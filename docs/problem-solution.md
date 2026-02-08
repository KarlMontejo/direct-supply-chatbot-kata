## Problem and Solution

### Context

The goal of this project is to reduce friction in food procurement by helping users resolve stock-outs, validate compliance, and discover viable alternatives using agentic reasoning across structured data sources.

In healthcare and senior living, food procurement teams operate under pressure to:
- Maintain uninterrupted food service
- Stay compliant with complex contracts and dietary requirements
- Respond quickly to supply-chain volatility

Food procurement is especially challenging because it is:
- **High-frequency** (daily ordering)
- **Constraint-heavy** (contracts, nutrition, suppliers)
- **Operationally fragile** (stock-outs cascade quickly)

---

### Problems

#### Stock-outs Disrupt Operations
- Products frequently become unavailable or partially unavailable
- A single stock-out can impact multiple meals and facilities
- Manual substitution is slow and error-prone

#### Contract Compliance Is Easy to Break
- Contracts specify allowed brands, pack sizes, suppliers, and effective dates
- Small deviations (brand, unit size, distributor) can break compliance
- Non-compliance leads to cost leakage and reporting issues

#### Product Discovery Is Fragmented
- Finding compliant, available alternatives requires checking multiple systems
- Ingredient and nutrition equivalence is difficult to validate quickly
- Staff often rely on tribal knowledge under time pressure

---

### Solution

An **agentic LLM-powered procurement assistant** that acts as a **decision-support tool** for food procurement workflows in healthcare and senior living.

The system:
- Assists with resolving stock-outs
- Validates contract and requirement compliance
- Recommends curated, compliant product alternatives
- Drafts order suggestions (non-executing)

---

### Data Sources

#### Mock Contracts API
- Simulates real-world food procurement contracts and compliance rules

#### Mock Inventory API
- Simulates real-time inventory availability, including hard and partial stock-outs