class Game
{
private:
   Player player = Player();
   Player NPC = Player();
public:
    void play_game()
    {
        while(true)
        {
            char n;
            std::cout << "�������� �����?" << std::endl;
            cin >> n;
            if(n = 'y') player.add_card();
            else break;
        }
        while(NPC.counter <= 16)
        {
            NPC.add_card();
        }
        if(player.counter == 21) std::cout << "����";
        if(player.counter > NPC.counter && player.counter <= 21) std::cout << "������";
        if(player.counter < NPC.counter && NPC.counter <= 21) std::cout << "�� ���������";
        if(player.counter > 21 || NPC.counter > 21 || player.counter == NPC.counter) std::cout << "�����";
    }
};
