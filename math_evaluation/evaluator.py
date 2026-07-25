from dataclasses import dataclass


@dataclass
class MathEvaluation:
    correctness: int
    reasoning: int
    clarity: int

    def total_score(self):
        return self.correctness + self.reasoning + self.clarity

    def passed(self):
        return self.total_score() >= 12


def evaluate_solution(correctness, reasoning, clarity):
    if not all(0 <= score <= 5 for score in (correctness, reasoning, clarity)):
        raise ValueError("Scores must be between 0 and 5.")

    return MathEvaluation(correctness, reasoning, clarity)


if __name__ == "__main__":
    result = evaluate_solution(5, 4, 4)
    print(f"Total Score: {result.total_score()}")
    print(f"Passed: {result.passed()}")
