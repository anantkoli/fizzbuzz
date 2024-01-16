

class AppFizzBuzz:
    def __init__(self, kwargs):
        """
        This is classic fizz buzz game.
        Input:
                In the Fizz-Buzz algorithm involves replacing all multiples of 3 (any number) with "fizz",
                all multiples of 5 (any number other than first) with "buzz"
                and all multiples of 15 (above two number) with "fizzbuzz".
        Output example:
                “1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,..."
        """
        self.val_1 = kwargs.get('num1')
        self.val_2 = kwargs.get('num2')
        self.num_range = kwargs.get('num_range')
        self.word_1 = kwargs.get('word1').lower()
        self.word_2 = kwargs.get('word2').lower()

    def run(self):
        out_ = [i for i in range(1, self.num_range + 1)]
        for i in range(1, self.num_range + 1):
            if i % (self.val_1 * self.val_2) == 0:
                out_[i - 1] = self.word_1+self.word_2
            elif i % self.val_1 == 0:
                out_[i - 1] = self.word_1
            elif i % self.val_2 == 0:
                out_[i - 1] = self.word_2
            else:
                pass
        return [str(i) for i in out_]


if __name__ == '__main__':
    num1, num2, num_range = map(int, input().split())
    word1, word2 = map(str, input().split())

    param = {'num1': num1, 'num2': num2, 'num_range': num_range, 'word1': word1, 'word2': word2}
    obj = AppFizzBuzz(param)
    resp = obj.run()
    print(resp)
