# axelrods-iterated-prisoners-dilemma

This repository is a personal exploration of the **Iterated Prisoner's Dilemma (IPD)** tournament with various different strategies, inspired by **Robert Axelrod's** famous experiments. It simulates how different strategies perform in repeated interactions, following the framework of Axelrod's tournament.

## The Prisoner's Dilemma

The **Prisoner's Dilemma** is a well-known problem in game theory that has real-world applications in areas such as international relations, economics, business competition, and even animal behavior.

### Example Scenario:

Imagine a banker presents you and another player with a chest of coins. Each of you has two choices (and neither knows what the other will choose): you can either **cooperate** or **defect**.

- **If both players cooperate**, each gets 3 coins.
- **If one cooperates and the other defects**, the defector gets 5 coins, while the cooperator gets nothing.
- **If both players defect**, both get 1 coin.

The goal is to maximize your own coins. If your opponent cooperates, you could cooperate and get 3 coins, but if you defect, you get 5 coins—so you're better off defecting. However, if your opponent defects, you're left with either 0 coins (if you cooperate) or 1 coin (if you defect). Thus, from a rational perspective, you should always defect because it offers a better outcome in any scenario.

The problem is that if both players adopt this rational strategy and always defect, you’ll end up with 1 coin each in every round, which is a suboptimal outcome compared to mutual cooperation, where you could each get 3 coins.

## The Iterated Prisoner's Dilemma

In the **Iterated Prisoner's Dilemma** (IPD), players face the dilemma repeatedly, allowing them to adapt their strategy based on past interactions. Strategies can evolve over time, leading to cooperation, retaliation, or exploitation, depending on the opponent’s behavior.
