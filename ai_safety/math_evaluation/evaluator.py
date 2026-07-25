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
    return MathEvaluation(correctness, reasoning, clarity)


if __name__ == "__main__":
    result = evaluate_solution(5, 4, 4)
    print("Score:", result.total_score())
