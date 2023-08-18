from typing import List

from hstest import CheckResult, dynamic_test, StageTest, TestCase, TestedProgram

FILENAME = 'forbidden_words.txt'
words = 'awful\natrocious\nharsh\ncrummy\ndreadful\nlousy'

T = True
F = False
MSG_CENS = 'Bad words should be censored, according to their length'
MSG_NO_CENS = 'No need to censor non-obscene words'
WORDS_TO_CHECK = (('awful', T), ('scrumble', F), ('HARSH', T), ('scream', F),
                  ('atrOCIOus', T), ('LOSSLESS', F), ('dreadful', T), ('crumpet', F),
                  ('cRuMmy', T), ('hard', F), ('lousy', T), ('dream', F))


class CheckerStage3Test(StageTest):
    def exemplary_output(self, word, flag):
        if flag:
            cens = '*' * len(word)
            return cens
        else:
            return word

    def generate(self) -> List[TestCase]:
        return [
            TestCase(dynamic_testing=self.test1, files={FILENAME: words})
        ]

    def test1(self):

        pr = TestedProgram()
        pr.start()
        pr.execute(FILENAME)
        for pair in WORDS_TO_CHECK:
            word, flag = pair
            out = pr.execute(word).strip()
            if out != self.exemplary_output(word, flag):
                if flag:
                    return CheckResult.wrong(MSG_CENS)
                else:
                    return CheckResult.wrong(MSG_NO_CENS)
        out = pr.execute('exit')
        if 'bye' not in out.strip().lower():
            return CheckResult.wrong('The program should be polite')
        return CheckResult.correct()


if __name__ == '__main__':
    CheckerStage3Test().run_tests()
