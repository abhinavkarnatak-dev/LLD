#include <bits/stdc++.h>
using namespace std;

class EagerSingleton
{
private:
    static EagerSingleton instance;

    EagerSingleton() {}

public:
    EagerSingleton(const EagerSingleton &) = delete;
    EagerSingleton &operator=(const EagerSingleton &) = delete;

    static EagerSingleton &getInstance()
    {
        return instance;
    }
};

EagerSingleton EagerSingleton::instance;

int main()
{

    EagerSingleton &obj1 = EagerSingleton::getInstance();
    EagerSingleton &obj2 = EagerSingleton::getInstance();

    cout << &obj1 << " " << &obj2 << endl;
}