#include <bits/stdc++.h>
using namespace std;

// Without SRP
// One class handling data + DB + email

class UserWithoutSRP
{
public:
    string name;
    string email;

    UserWithoutSRP(string name, string email)
    {
        this->name = name;
        this->email = email;
    }

    void saveToDatabase()
    {
        cout << "Saving user " << name << " to database" << endl;
    }

    void sendWelcomeEmail()
    {
        cout << "Sending welcome email to " << email << endl;
    }
};

// With SRP
// Responsibilities separated

class User
{
public:
    string name;
    string email;

    User(string name, string email)
    {
        this->name = name;
        this->email = email;
    }
};

class UserRepository
{
public:
    void save(User user)
    {
        cout << "Saving user " << user.name << " to database" << endl;
    }
};

class EmailService
{
public:
    void sendWelcomeEmail(User user)
    {
        cout << "Sending welcome email to " << user.email << endl;
    }
};

int main()
{

    cout << "----- WITHOUT SRP -----" << endl;

    UserWithoutSRP u1("Abhinav", "abhinav@email.com");
    u1.saveToDatabase();
    u1.sendWelcomeEmail();

    cout << "\n----- WITH SRP -----" << endl;

    User u2("Abhinav", "abhinav@email.com");

    UserRepository repo;
    repo.save(u2);

    EmailService emailService;
    emailService.sendWelcomeEmail(u2);
}