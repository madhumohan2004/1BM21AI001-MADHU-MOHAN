#include <iostream>
using namespace std;

class BinomialCalculator {
private:
    int n, k;

public:
    BinomialCalculator(int numN, int numK) {
        n = numN;
        k = numK;
    }

    int calculateCoefficient() {
        int c[10][10];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                if (j == 0 || i == j)
                    c[i][j] = 1;
                else
                    c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
            }
        }
        return c[n][k];
    }
};

int main() {
    int n, k;
    cout << "Enter the value of n & k such that n > k" << endl;
    cin >> n >> k;

    BinomialCalculator calculator(n, k);
    int coefficient = calculator.calculateCoefficient();

    cout << "C(" << n << "," << k << ") = " << coefficient << endl;

    return 0;
}
