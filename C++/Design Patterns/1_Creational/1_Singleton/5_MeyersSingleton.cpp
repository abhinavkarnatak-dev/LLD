// Meyers Singleton in C++ = Bill Pugh in Java

#include <bits/stdc++.h>
using namespace std;

class Singleton
{
private:
    Singleton() {}

public:
    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;

    static Singleton &getInstance()
    {
        // The static local variable behaves like the Java Holder class:
        // - It's not initialized until this method is called
        // - Initialization is thread-safe (in C++11 and later)
        // - No need for manual synchronization
        static Singleton instance;
        return instance;
    }
};

int main()
{
    Singleton &obj1 = Singleton::getInstance();
    Singleton &obj2 = Singleton::getInstance();

    cout << &obj1 << " " << &obj2 << endl;
}