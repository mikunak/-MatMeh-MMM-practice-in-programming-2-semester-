#include <iostream>
#include <vector>
#include <stack>

int calculate(int a, int b, const std::string &operation)
{
    if (operation == "+")
        return a + b;
    if (operation == "-")
        return a - b;
    if (operation == "*")
        return a * b;
    if (operation == "/")
        return a / b;
    return -1;
}

bool isOperation(const std::string& op)
{
    return op == "+" || op == "-" || op == "*" || op == "/";
}

int RPN(std::vector<std::string> &notation) {

    std::stack<int> numbers;
    for (const auto& str : notation)
    {
        if (isOperation(str))
        {
            int n2 = numbers.top(); numbers.pop();
            int n1 = numbers.top(); numbers.pop();

            numbers.push(calculate(n1, n2, str));
        }
        else
            numbers.push(std::stoi(str));
    }

    return numbers.top();
}

std::vector<std::string> parse(const std::string& input)
{
    std::vector<std::string> vec;

    std::string current;

    for (char c : input)
    {
        if (isdigit(c))
            current += c;
        else if (c)
        {
            if (!current.empty())
            {
                vec.emplace_back(std::move(current));
                current = "";
            }

            if (c != ' ')
                vec.emplace_back(1, c);
        }
    }

    if (!current.empty())
        vec.push_back(std::move(current));

    return vec;
}

int main() {
    std::string s = "5 5 +";
    std::vector<std::string> notation = parse(s);
    std::cout << RPN(notation) << std::endl;
    std::string a = "2 4 *";
    std::vector<std::string> notation2 = parse(a);
    std::cout << RPN(notation2) << std::endl;
}
