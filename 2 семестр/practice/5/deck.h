struct Card
{
    int value;
    int color;
};

class Deck
{
private:
    set<Card> cards;
public:
    Deck()
    {
        for( int i = 0; i < 13; i++)
            for( int j = 0; j < 4; j++)
                cards.insert(Card(i, j));
    }


};
