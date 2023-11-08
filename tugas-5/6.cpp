#include <iostream>

using namespace std;

// Find shortest route to 1
int find_route(int n, int t = 0)
{
    if (n == 1)
        return t;
    if (n % 3 == 0)
        return find_route(n / 3, t + 1);
    if (n % 2 == 0)
        return find_route(n / 2, t + 1);
    return find_route(n - 1, t + 1);
}

int main()
{
    int n;
    cin >> n;
    cout << find_route(n) << "\n";
    return 0;
}