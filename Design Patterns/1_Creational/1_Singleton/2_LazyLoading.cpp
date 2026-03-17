#include <bits/stdc++.h>
using namespace std;

class LazySingleton
{
private:
    static LazySingleton *instance;

    LazySingleton() {}

public:
    LazySingleton(const LazySingleton &) = delete;
    LazySingleton &operator=(const LazySingleton &) = delete;

    static LazySingleton *getInstance()
    {
        if (instance == nullptr)
        {
            instance = new LazySingleton();
        }

        return instance;
    }
};

LazySingleton *LazySingleton::instance = nullptr;

int main()
{

    LazySingleton *obj1 = LazySingleton::getInstance();
    LazySingleton *obj2 = LazySingleton::getInstance();

    cout << obj1 << " " << obj2 << endl;
}