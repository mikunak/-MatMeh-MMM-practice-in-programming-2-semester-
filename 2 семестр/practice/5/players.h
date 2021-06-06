#include <algorithm>

class Player
{
private:
    int counter = 0;
public:
    Player()
    {
        counter += select_random_card().value + select_random_card().value;
    }
    Card select_random_card()
    {
        auto r = rand() % cards.size();
        auto it = std::begin(cards);
        std::advance(it,r);
        Card n = *it;
        erase(it);
        return n;
    }
    void add_card()
    {
        counter += select_random_card().value;
    }
};
