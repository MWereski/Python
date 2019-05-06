import random
import itertools
class Card:
    # słownik symboli unicode
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
       
    def __init__(self, rank, suit):
    # TODO: definicja metody
        self.__rank_ = rank
        self.__suit_ = suit

    def get_value(self):
    # TODO: definicja metody (ma zwracać kartę w takiej reprezentacji, jak dotychczas, tzn. krotka)
        return tuple([self.__suit_, card_rank_values[self.__rank_]])
        
    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty    
        return str(tuple([self.__rank_, Card.unicode_dict[self.__suit_]]))



class Deck():
    
    def __init__(self, *args):
    # TODO: definicja metody, ma tworzyć niepotasowaną talię (jak na poprzednich lab)
        lista1 = list(itertools.product(list(card_rank_values.keys()), list(Card.unicode_dict.keys())))

        self.__lista_ = []
        for z in lista1:
             self.__lista_.append(Card(z[0], z[1]))

    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty
        temp = ""
        for z in self.__lista_:
            temp += str(z)
        return str(temp)

    def shuffle(self):
    # TODO: definicja metody, tasowanie
        random.shuffle(self.__lista_)

    def deal(self, players):
        for p in players:
            for z in range(0, 5):
                p.take_card(self.__lista_.pop())
    # TODO: definicja metody, otrzymuje listę graczy i rozdaje im karty wywołując na nich metodę take_card z Player

class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
    # TODO: definicja metody, zwraca stringa z kartami gracza
        temp = ""
        for k in self.__hand_:
            temp += str(k)
        return str(temp)

def histogram(text):
    d = dict()
    for l in text:
        d[l] = text.count(l)
    return d


# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}


def get_player_hand_rank(hand):
#hand_rank_list = [seq[0] for seq in hand[0]]  # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_rank_list = [seq.get_value()[1] for seq in hand]
    hand_color_list = [seq.get_value()[0] for seq in hand] # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.

    hand_rank_histogram = histogram(hand_rank_list)

    hand_color_histogram = histogram(hand_color_list)

    def is_rank_sequence(hand):
        pomoc = []
        for i in hand_rank_list:
            if(i == 'J'):
                i = 11
                pomoc.append(i)
            elif(i == 'Q'):
                i = 12
                pomoc.append(i)
            elif(i == 'K'):
                i = 13
                pomoc.append(i)
            elif(i == 'A'):
                i = 14
                pomoc.append(i)
            else:
                pomoc.append(int(i))
        pomoc.sort()
        for i in range(1,len(pomoc)-1):
            if( pomoc[i] - pomoc[i-1] != 1):
                return False
        return True
            
        
            
    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0

    if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
    elif( ( 4 in hand_rank_histogram.values())):
        hand_strength =  8
    elif( ( 3 in hand_rank_histogram.values()) and (3 in hand_rank_histogram.values())):
        hand_strength = 7
    elif( ( 5 in hand_color_histogram.values())):
        hand_strength =  6
    elif(is_hand_rank_sequence):
        hand_strength =  5
    elif( ( 3 in hand_rank_histogram.values())):
        hand_strength =  4
    elif( (1 and 2 and 2) in hand_rank_histogram.values()):
        hand_strength =  3
    elif( ( 2 in hand_rank_histogram.values())):
        hand_strength =  2
    else:
        hand_strength = 1

    return(hand_strength)

