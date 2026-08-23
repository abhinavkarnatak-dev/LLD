#include <bits/stdc++.h>
using namespace std;

class Logistics
{
public:
    virtual void send() = 0;
    virtual ~Logistics() {}
};

class Road : public Logistics
{
public:
    void send() override
    {
        cout << "Sending by road logic" << endl;
    }
};

class Air : public Logistics
{
public:
    void send() override
    {
        cout << "Sending by air logic" << endl;
    }
};

// Bad Practice

class LogisticsServiceBad
{
public:
    void send(const string &mode)
    {
        if (mode == "Air")
        {
            Logistics *logistics = new Air();
            logistics->send();
            delete logistics;
        }
        else if (mode == "Road")
        {
            Logistics *logistics = new Road();
            logistics->send();
            delete logistics;
        }
    }
};

// Good Practice

class LogisticsFactory
{
public:
    static Logistics *getLogistics(const string &mode)
    {
        if (mode == "Air")
        {
            return new Air();
        }
        else if (mode == "Road")
        {
            return new Road();
        }
        throw invalid_argument("Unknown logistics mode: " + mode);
    }
};

class LogisticsService
{
public:
    void send(const string &mode)
    {
        Logistics *logistics = LogisticsFactory::getLogistics(mode);
        logistics->send();
        delete logistics;
    }
};

int main()
{
    LogisticsServiceBad badService;
    badService.send("Air");
    badService.send("Road");

    LogisticsService service;
    service.send("Air");
    service.send("Road");

    return 0;
}