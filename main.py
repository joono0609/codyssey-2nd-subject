import json
import os

# state.json을 프로젝트 루트(이 파일이 있는 위치)에 저장하기 위한 경로
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")

class Quiz:
    """
    하나의 퀴즈 문제를 표현하는 클래스.
    속성: 문제(question), 선택지(choices, 기본 4개), 정답(answer)
    """

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices          # 리스트, 기본 4개
        self.answer = answer            # 정답 번호(1~4)

    def show(self):
        """문제와 선택지를 화면에 출력한다."""
        print(f"\nQ. {self.question}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"  {idx}. {choice}")

    def check(self, user_answer):
        """사용자 입력(번호)이 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리로부터 Quiz 객체를 생성한다."""
        return Quiz(data["question"], data["choices"], data["answer"])


class QuizGame:
    """
    게임 전체를 관리하는 클래스.
    속성: quizzes(퀴즈 목록), best_score(최고 점수)
    """
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()   # 시작 시 파일 불러오기

    # ---------- 기본 데이터 ----------
    def default_quizzes(self):
        """파일이 없을 때 사용할 기본 퀴즈 5문제."""
        return [
            Quiz("리스트를 생성하는 올바른 문법은?",
                 ["list = ()", "list = []", "list = {}", "list = <>"], 2),
            Quiz("문자열 길이를 구하는 함수는?",
                 ["size()", "count()", "len()", "length()"], 3),
            Quiz("딕셔너리를 나타내는 기호는?",
                 ["[]", "()", "<>", "{}"], 4),
            Quiz("반복을 멈추는 키워드는?",
                 ["stop", "break", "exit", "end"], 2),
            Quiz("주석을 작성할 때 사용하는 기호는?",
                 ["//", "#", "/* */", "--"], 2),
        ]
  
    # ---------- 파일 저장/불러오기 ----------
    def save(self):
        """quizzes와 best_score를 state.json에 UTF-8로 저장한다."""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"저장 중 오류가 발생했습니다: {e}")

    def load(self):
        """state.json을 불러온다. 없거나 손상되면 기본 데이터를 사용한다."""
        if not os.path.exists(STATE_FILE):
            # 파일이 없는 첫 실행 → 기본 퀴즈 사용
            self.quizzes = self.default_quizzes()
            self.best_score = 0
            self.save()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data.get("best_score", 0)
        except (json.JSONDecodeError, KeyError, TypeError):
            # 파일이 손상된 경우
            print("저장 파일이 손상되어 기본 퀴즈로 시작합니다.")
            self.quizzes = self.default_quizzes()
            self.best_score = 0
            self.save()

    # ---------- 안전한 입력 ----------
    def safe_input(self, prompt):
        """
        Ctrl+C(KeyboardInterrupt)나 입력 종료(EOFError)가 발생해도
        프로그램이 종료되지 않도록 처리하는 입력 함수.
        """
        while True:
            try:
                return input(prompt)
            except KeyboardInterrupt:
                print("\n(종료하려면 메뉴에서 5번을 선택하세요.)")
            except EOFError:
                print("\n(입력이 종료되었습니다. 메뉴에서 5번을 선택하세요.)")

    # ---------- 메뉴 ----------
    def show_menu(self):
        """메뉴를 출력한다."""
        print("\n===== 파이썬 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 점수 확인")
        print("5. 종료")

    # ---------- 퀴즈 풀기 ----------
    def play(self):
        """모든 퀴즈를 순서대로 풀고 점수를 계산한다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct = 0  # 맞힌 개수
        for quiz in self.quizzes:
            quiz.show()
            user = self.safe_input("정답 번호를 입력하세요(1~4): ")
            if not user.isdigit():
                print("숫자를 입력해야 합니다. 오답 처리됩니다.")
                continue
            if quiz.check(int(user)):
                print("정답입니다! ⭕")
                correct += 1
            else:
                print(f"오답입니다. ❌ 정답은 {quiz.answer}번입니다.")

        # 맞힌 개수 → 100점 만점 백분율로 변환
        score = round(correct / len(self.quizzes) * 100)
        print(f"\n이번 점수: {score}점 (맞힌 개수: {correct} / {len(self.quizzes)})")

        # 최고 점수 갱신
        if score > self.best_score:
            self.best_score = score
            print("🎉 최고 점수를 경신했습니다!")
        self.last_score = score
        self.save()

    # ---------- 퀴즈 추가 ----------
    def add_quiz(self):
        """사용자로부터 새 퀴즈를 입력받아 추가한다."""
        question = self.safe_input("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            c = self.safe_input(f"{i}번 선택지: ")
            choices.append(c)

        answer = self.safe_input("정답 번호(1~4): ")
        if not answer.isdigit() or not (1 <= int(answer) <= 4):
            print("정답은 1~4 사이 숫자여야 합니다. 추가를 취소합니다.")
            return

        self.quizzes.append(Quiz(question, choices, int(answer)))
        self.save()
        print("퀴즈가 추가되었습니다! ✅")
    
    # ---------- 목록 보기 ----------
    def show_list(self):
        """등록된 퀴즈 목록을 보여준다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n총 {len(self.quizzes)}개의 퀴즈가 있습니다.")
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"{idx}. {quiz.question}")

    # ---------- 실행 루프 ----------
    def run(self):
        """메뉴를 반복 출력하며 선택에 따라 기능을 실행한다."""
        while True:
            self.show_menu()
            choice = self.safe_input("메뉴를 선택하세요: ")

            if choice == "1":
                self.play()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_list()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                print("게임을 종료합니다. 수고하셨어요! 👋")
                break
            else:
                print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()