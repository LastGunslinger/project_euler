'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Things to keep in mind:
1) Numerator and denominator are 2 digits
2) Fraction is < 1
3) Multiples of 10 are considered trivial
'''
import fractions
import time
import pytest


class NaiveFraction(fractions.Fraction):

    def __new__(cls, numerator, denominator):
        gcd = None
        for num in str(numerator):
            if num in str(denominator) and num != '0':
                gcd = num

        if gcd:
            numerator = str(numerator).replace(gcd, '', 1)
            denominator = str(denominator).replace(gcd, '', 1)

        self = super().__new__(cls, int(numerator), int(denominator))
        return self


class Fraction(fractions.Fraction):

    def naive_reduce(self):
        num_set = set(str(self.numerator))
        denom_set = set(str(self.denominator))
        if num_set.intersection(denom_set) and num_set.intersection(denom_set) != {'0'}:
            common = list(num_set.intersection(denom_set))[0]

            num_str = str(self.numerator)
            num_str = num_str.replace(common, '', 1)
            denom_str = str(self.denominator)
            # print(denom_str)
            denom_str = denom_str.replace(common, '', 1)
            if denom_str == '0':
                return self

            # print(Fraction(int(num_str), int(denom_str)))
            return Fraction(int(num_str), int(denom_str))
        else:
            return self

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'


def generate_fractions():
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            yield numerator, denominator


def main():
    weird_fractions = []
    for num, denom in generate_fractions():
        try:
            fract = Fraction(num, denom)
            naive_fract = NaiveFraction(num, denom)
            # print(f'{fract} : {naive_fract}')
            if (num, denom) == (naive_fract.numerator, naive_fract.denominator):
                continue
            if fract != naive_fract:
                continue
            if naive_fract > 1:
                continue
            
            print(f'{fract} : {naive_fract}')
            weird_fractions.append(fract)
        except ZeroDivisionError:
            continue


def test_main():
    for fract in generate_fractions():
        print(fract)


if __name__ == '__main__':
    start = time.time()
    print(f'Result: {main()}')
    print('--- {} seconds ---'.format(time.time() - start))