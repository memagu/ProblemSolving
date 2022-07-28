// # https://open.kattis.com/problems/fluortanten
//
// def evaluate(arr):
//     result = 0
//     for i, item in enumerate(arr):
//         result += (i+1) * item
//
//     return result
//
//
// n = int(input())
// children = list(map(int, input().split()))
// children.remove(0)
//
// highest = evaluate(children)
//
// for i in range(n):
//     temp = children.copy()
//     temp.insert(i, 0)
//     highest = max(highest, evaluate(temp))
//
// print(highest)


#include <iostream>


int evaluate(int arr[], int size)
{
    int result = 0;
    for (int i = 0; i < size; i++)
    {
        result += (i + 1) * arr[i];
    }
    return result;
}


int main()
{
    int n;
    std::cin >> n;
    int *children = new int[n];

    int i = 0;
    while (i < n-1)
    {
        int temp;
        std::cin >> temp;
        if (temp)
        {
            children[i] = temp;
            i++;
        }
    }

    int maximum = evaluate(children, n);

    for (int i = n-1; i > 0; i--)
    {
        int temp = children[i];
        children[i] = children[i - 1];
        children[i - 1] = temp;

        maximum = std::max(maximum, evaluate(children, n));
    }

    std::cout << maximum;

    delete[] children;
    return 0;
}