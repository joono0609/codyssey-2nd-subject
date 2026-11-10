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
                print("\n(종료하려면 메뉴에서 0번을 선택하세요.)")
            except EOFError:
                print("\n(입력이 종료되었습니다. 메뉴에서 0번을 선택하세요.)")

    # ---------- 메뉴 ----------
    def show_menu(self):
        """메뉴를 출력한다."""
        print("\n===== 파이썬 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 점수 확인")
        print("5. 종료")

    # ---------- 실행 루프 ----------
    def run(self):
        """메뉴를 반복 출력하며 선택에 따라 기능을 실행한다."""
        while True:
            self.show_menu()
            choice = self.safe_input("메뉴를 선택하세요: ")

            if choice == "1":
               print("퀴즈풀기")
            elif choice == "2":
               print("퀴즈추가")
            elif choice == "3":
               print("퀴즈목록보기")
            elif choice == "4":
               print("점수확인")
            elif choice == "5":
                print("게임을 종료합니다. 수고하셨어요! 👋")
                break
            else:
                print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()