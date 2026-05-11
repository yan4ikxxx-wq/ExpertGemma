![Gemma 4 Configurator](carbon.jpg)

# Gemma 4 26B-A4B Configuration & Logic Orchestrator

This repository provides a specialized configuration layer for **Gemma 4**, focusing on the **26B-A4B (Mixture of Experts)** architecture.

## Technical Parameter Overview

To maximize the performance of Gemma 4, this toolkit manages the following inference settings:

*   **Temperature**: Calibrates the response's determinism. Set to `0.7` by default to balance creative fluidity with logical consistency.
*   **Top-P (Nucleus Sampling)**: Set to `0.95` to ensure the model selects from the most probable 95% of the token pool, preventing irrelevant "tail" distribution words.
*   **Top-K**: Filters the top 40 most likely tokens, significantly reducing hallucinations in technical tasks.
*   **RPM (Requests Per Minute)**: Integrated rate-limiting logic to ensure stable API performance and prevent `429` errors.
*   **Reasoning Engine**: Implements the `<|thought|>` tag, which is essential for Gemma 4's chain-of-thought capabilities.

## Architecture
The script uses a **MoE-centric approach**. By targeting the **Active 4 Billion (A4B)** parameters of the 26B model, we achieve high-speed inference without sacrificing the depth of knowledge typically found in larger models.

## Usage
1. Clone the repository.
2. Integrate `Gemma4Config` into your inference pipeline.
3. Use the `generate_structured_payload` method to wrap your queries.
