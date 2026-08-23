#include <bits/stdc++.h>
using namespace std;

// Without ISP
// One large interface forces classes to implement methods they don't need.

class Uber
{
public:
    virtual void bookRide() = 0;
    virtual void acceptRide() = 0;
    virtual void drive() = 0;
    virtual void endRide() = 0;
    virtual void payRide() = 0;
};

class RiderNoISP : public Uber
{
public:
    void bookRide() { cout << "Ride Booked" << endl; }

    void acceptRide() { cout << "Not applicable for rider" << endl; }

    void drive() { cout << "Not applicable for rider" << endl; }

    void endRide() { cout << "Not applicable for rider" << endl; }

    void payRide() { cout << "Payment Successful" << endl; }
};

// With ISP
// Interfaces are split so classes implement only the methods they actually use.

class RiderInterface
{
public:
    virtual void bookRide() = 0;
    virtual void payRide() = 0;
};

class DriverInterface
{
public:
    virtual void acceptRide() = 0;
    virtual void drive() = 0;
    virtual void endRide() = 0;
};

class Rider : public RiderInterface
{
public:
    void bookRide() { cout << "Ride Booked" << endl; }

    void payRide() { cout << "Payment Successful" << endl; }
};

class Driver : public DriverInterface
{
public:
    void acceptRide() { cout << "Ride Accepted" << endl; }

    void drive() { cout << "Driving" << endl; }

    void endRide() { cout << "Ride Ended" << endl; }
};

int main()
{
    cout << "----- WITHOUT ISP -----" << endl;

    RiderNoISP riderNoISP;
    riderNoISP.bookRide();
    riderNoISP.payRide();

    cout << "----- WITH ISP -----" << endl;

    Rider rider;
    rider.bookRide();
    rider.payRide();
}