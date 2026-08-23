// Like Synchronized in Java, C++ has Mutex for thread safety

#include <bits/stdc++.h>
#include <mutex>
using namespace std;

class Singleton
{
private:
    static Singleton *instance;
    static mutex mtx;

    Singleton() {}

public:
    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;

    static Singleton *getInstance()
    {
        if (instance == nullptr)
        {
            lock_guard<mutex> lock(mtx);
            if (instance == nullptr)
            {
                instance = new Singleton();
            }
        }
        return instance;
    }
};

Singleton *Singleton::instance = nullptr;
mutex Singleton::mtx;

int main()
{

    Singleton *obj1 = Singleton::getInstance();
    Singleton *obj2 = Singleton::getInstance();

    cout << obj1 << " " << obj2 << endl;
}