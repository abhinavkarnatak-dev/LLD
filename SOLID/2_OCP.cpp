#include <bits/stdc++.h>
using namespace std;

// Without OCP
// You add taxes for ever country inside the same class

class TaxCalculatorNoOCP
{
public:
    double amountAfterTax(double amount, string region)
    {
        if (region == "India")
            return (amount + 0.18 * amount);
        else if (region == "USA")
            return (amount + 0.10 * amount);
        return amount;
    }
};

class InvoiceServiceNoOCP
{
public:
    double calculate(double amount, string region)
    {
        TaxCalculatorNoOCP taxcalculator;
        return taxcalculator.amountAfterTax(amount, region);
    }
};

// With OCP
// You extend the class to add the country taxes

class TaxCalculator
{
public:
    virtual double amountAfterTax(double amount) = 0;
};

class IndianTax : public TaxCalculator
{
public:
    double amountAfterTax(double amount)
    {
        return amount + 0.18 * amount;
    }
};

class USATax : public TaxCalculator
{
public:
    double amountAfterTax(double amount)
    {
        return amount + 0.10 * amount;
    }
};

class InvoiceService
{
private:
    TaxCalculator *tax;

public:
    InvoiceService(TaxCalculator *tax)
    {
        this->tax = tax;
    }

    double calculate(double amount)
    {
        return tax->amountAfterTax(amount);
    }
};

int main()
{
    cout << "----- WITHOUT OCP -----" << endl;

    InvoiceServiceNoOCP invoiceservice;
    cout << invoiceservice.calculate(100, "India") << endl;

    cout << "----- WITH OCP -----" << endl;

    USATax usatax;
    InvoiceService invoice(&usatax);

    cout << invoice.calculate(100);
}