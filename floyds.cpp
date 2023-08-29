#include <iostream>
using namespace std;

class ShortestPathCalculator {
private:
    int a[10][10];
    int n;

    int min(int x, int y) {
        if (x < y) {
            return x;
        } else {
            return y;
        }
    }

public:
    ShortestPathCalculator() {
        n = 0;
    }

    void inputMatrix() {
        cout << "Enter the no. of vertices:\t";
        cin >> n;

        cout << "Enter the cost matrix:\n";
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> a[i][j];
            }
        }
    }

    void floyds() {
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
                }
            }
        }
    }

    void displayMatrix() {
        cout << "\nAll pair shortest path matrix is:\n";
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << a[i][j] << "\t";
            }
            cout << "\n\n";
        }
    }
};

int main() {
    ShortestPathCalculator calculator;
    calculator.inputMatrix();
    calculator.floyds();
    calculator.displayMatrix();

    return 0;
}
