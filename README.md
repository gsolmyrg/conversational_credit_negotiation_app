# Conversational Credit Negotiation — Simulation App

Streamlit front end for exercising the [conversational negotiation flow](https://github.com/gsolmyrg/conversational_credit_negotiation_flow) against configurable synthetic customer profiles.

> Every persona is generated or hand-entered by the operator. No real customer data is present in this repository.

## What it demonstrates

**Synthetic personas as a testing tool.** Name, age, gender, outstanding debt and yearly income are all adjustable, with a randomizer for quick exploration. Agent behavior in a negotiation depends heavily on the customer's financial position, so being able to sweep that space quickly is how you find the edges — a customer with R$ 0 debt and one with R$ 100,000 should not get the same conversation.

**Deliberate exclusion from randomization.** The phone number is the one field the randomizer never touches, because it is the only field with a real-world side effect: it decides who receives a message. Randomizing it would mean messaging a stranger.

**Validation before dispatch.** The app blocks submission when name or phone number is missing, rather than letting an incomplete payload fail deeper in the stack.

**Explicit session-history control.** A checkbox clears conversation history, making it obvious whether a run starts fresh or continues an existing thread. In stateful agent systems, ambiguity about this is a common source of unreproducible behavior.

**The request payload is displayed before sending.** What the UI shows is exactly what the service receives, which makes the tool useful for debugging the contract and not just the conversation.

## Layout

```
main.py       Streamlit UI, persona configuration, validation
services.py   CreditNegotiationService - calls the middleware
```

## Stack

Python · Streamlit · [uv](https://docs.astral.sh/uv/)

## Running it

```bash
pip install uv
uv sync
cp .env.example .env   # point at the middleware endpoint and API key
uv run streamlit run main.py
```

## Author

**Guilherme Candeloro Padilha** — AI Solutions Architect
[LinkedIn](https://www.linkedin.com/in/guilhermecandeloro) · guilherme@aiveon.com
