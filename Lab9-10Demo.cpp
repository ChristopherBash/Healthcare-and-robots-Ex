// Lab9-10Demo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;
int main()
{
    //Deglaire Variables 
    string firstName = "";
    string lastName = "";
    string ssn = "";
    string phone = "";
    string fullName = "";


    //Input 
    cout << "Enter your first name: ";
    cin >> firstName;
    cout << "enter your last name: ";
    cin >> lastName;

    do {
        cout << "Enter your 10 didgit phone number(no dashes or paenthasis: ";
        cin >> phone;
    } while (phone.length() != 10);
    phone.insert(0, "(");
    phone.insert(4, "(");
    phone.insert(8, "-");

    do {
        cout << "Enter 9 didgit ssn(no dashes): ";
        cin >> ssn;

    } while (ssn.length() != 9);
    ssn.insert(3, "-");
    ssn.insert(6, "-");

    fullName = firstName + " " + lastName;

    cout << "Your fullname is: " << fullName << endl;
    cout << "Your reveresed full name is: ";

    for (int i = fullName.length() - 1; i >= 0; i--)
    {
        cout << fullName[i];
    }

    cout << "Your phone number: " << phone << endl;
    cout << "Your ssn: " << ssn << endl;

    cout << "T H A N K  Y O U" << endl;

    return 0;










}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
