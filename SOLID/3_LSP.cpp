#include <iostream>
using namespace std;

// Without LSP
// Square breaks the expected behaviour of Rectangle

class RectangleNoLSP
{
protected:
    int width, height;

public:
    virtual void setWidth(int w) { width = w; }
    virtual void setHeight(int h) { height = h; }
    int getArea() { return width * height; }
};

class SquareNoLSP : public RectangleNoLSP
{
public:
    void setWidth(int w) override
    {
        width = w;
        height = w;
    }

    void setHeight(int h) override
    {
        height = h;
        width = h;
    }
};

void printAreaNoLSP(RectangleNoLSP *r)
{
    r->setWidth(5);
    r->setHeight(10);
    cout << r->getArea() << endl; // Expected: 50 but becomes 100
}

// With LSP
// Square is not forced to behave like Rectangle

class Shape
{
public:
    virtual int getArea() = 0;
};

class Rectangle : public Shape
{
private:
    int width, height;

public:
    Rectangle(int w, int h)
    {
        width = w;
        height = h;
    }

    int getArea()
    {
        return width * height;
    }
};

class Square : public Shape
{
private:
    int side;

public:
    Square(int s)
    {
        side = s;
    }

    int getArea()
    {
        return side * side;
    }
};

int main()
{

    cout << "----- WITHOUT LSP -----" << endl;

    RectangleNoLSP *r = new SquareNoLSP();
    printAreaNoLSP(r);

    cout << "----- WITH LSP -----" << endl;

    Shape *shape1 = new Rectangle(5, 10);
    cout << shape1->getArea() << endl;

    Shape *shape2 = new Square(5);
    cout << shape2->getArea() << endl;
}