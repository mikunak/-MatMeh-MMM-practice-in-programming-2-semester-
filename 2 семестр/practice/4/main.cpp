#include <iostream>
#include <cmath>

  using namespace std;

  class Complex
  {
    private:
  double re, im;

  public:
    Complex ();
    Complex (double);
    Complex (double, double);
    Complex (const Complex&);
    ~Complex ();
    double mod (double, double);
    double pairing(double, double);
    Complex& operator = (Complex&);
    Complex operator + (const Complex&);
    Complex operator + (const double);
    Complex operator - (const Complex&);
    Complex operator - (const double);
    Complex operator * (const Complex&);
    Complex operator * (const double);
    Complex operator / (const Complex&);
    Complex operator / (const double);
    ostream& operator<< (const Complex&);
    istream& operator>> (Complex&);
    friend ostream & operator<< (ostream&, const Complex&);
    friend istream & operator>> (istream&, Complex&);
  };
 Complex :: Complex (): re(0), im(0)
 {
 }

 Complex :: Complex (double i)
  {
    re = 0;
    im = i;
  }

 Complex :: Complex (double r, double i=0)
  {
    re = r;
    im = i;
  }

 Complex :: Complex (const Complex &c)
  {
    re = c.re;
    im = c.im;
  }


 Complex :: ~Complex ()
  {
  }


 double mod (double re, double im)
  {
    return sqrt (re * re + im * im);
  }


 Complex &Complex :: operator = (Complex &c)
  {
    re = c.re;
    im = c.im;
    return *this;
  }

 Complex Complex :: operator + (const Complex &c)
  {
    return Complex (re + c.re, im + c.im);
  }
 Complex Complex :: operator + (const double a)
  {
    return Complex (re + a, im + 0);
  }

 Complex Complex :: operator - (const Complex &c)
  {
    return Complex(re - c.re, im - c.im);
  }
  Complex Complex :: operator - (const double a)
  {
    return Complex(re - a, im + 0);
  }

 Complex Complex :: operator * (const Complex &c)
  {
    return Complex(re * c.re - im * c.im, re * c.im + im * c.re);
  }

 Complex Complex :: operator * (const double a)
  {
    return Complex(re * a, im * a);
  }

 Complex Complex :: operator / (const Complex &c)
  {
    double r = c.re * c.re + c.im * c.im;
    if (r==0)
    {
        cout <<"Error";
    }
    else
    {
        Complex temp;
        temp.re = (re * c.re + im * c.im) / r;
        temp.im = (im * c.re - re * c.im) / r;
        return temp;
    }

  }

 Complex Complex :: operator / (const double a)
  {
    if (a==0)
    {
        cout <<"Error! Division by 0!";
    }
    else
    {
        return Complex (re / a, im / a);
    }

  }

std :: ostream& operator<< (std :: ostream &out, const Complex &c)
  {
    out << "(" << c.re << ", " << c.im << ")";
    return out;
  }

 std :: istream& operator>> (std :: istream &in, Complex &c)
  {
    in >> c.re >> c.im;
    return in;
  }

int main()
{
    double a = 2;
    Complex b (-1, 1);
    Complex c (2,-2);
    Complex d;

    cout << b << endl;
    cout <<  b + a << endl;
    cout <<  b + c << endl;
    cout <<  b - a << endl;
    cout <<  b - c << endl;
    cout <<  b * a << endl;
    cout <<  b * c << endl;
    cout <<  b / a << endl;
    cout <<  b / c << endl;
    cout << mod(1, 1) << endl;


    return 0;
}
