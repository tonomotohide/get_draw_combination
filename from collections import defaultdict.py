from collections import defaultdict
import itertools

other_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]   # それ以外のカードの選択肢

for i in range(10):
    straight = [1+i,2+i,3+i,4+i,5+i]            # ストレートを構成するカード

    # その他2枚がペアでないとき
    for others in itertools.combinations(other_cards,2):
        cards = straight + list(others)         # ストレート構成分とその他2枚の計7枚

        for flop_flags in itertools.combinations([0,1,2,3,4,5,6],3):
            flop_flags = set(flop_flags)        # cardのうち、何番目(※0始まり)のカードがflopに出ているか
            flop = list()                       # Flopカード
            not_flop = list()                   # 非Flopカード

            # Flop分と非Flop分に分ける
            for j in range(7):
                if j in flop_flags:
                    flop.append(cards[j])
                else:
                    not_flop.append(cards[j])

            # 非Flop分をHandとTurn&River分に分ける
            for hands_flags in itertools.combinations([0,1,2,3],2):
                hands_flags = set(hands_flags)  # not_boardのうち、何番目(※0始まり)のカードがハンドか
                hand = list()                   # handのカード
                turn_river = list()             # TurnとRiverのカード

                for j in range(4):
                    if j in hands_flags:
                        hand.append(not_flop[j])
                    else:
                        turn_river.append(not_flop[j])

                # ここでflop,hand,turn_riverに対して、osdなのかgutなのか判定掛ければ良い
                # 多分重複組み合わせがありそうな気がするのでdictとかで管理すると良いかも。

    # その他2枚がペアのとき
    for others in itertools.combinations(other_cards,1):
        cards = straight + list(others) + list(others)  # ストレート構成分とその他2枚の計7枚

        for flop_flags in itertools.combinations([0,1,2,3,4,5,6],3):
            flop_flags = set(flop_flags)        # cardのうち、何番目(※0始まり)のカードがflopに出ているか
            flop = list()                       # Flopカード
            not_flop = list()                   # 非Flopカード

            # Flop分と非Flop分に分ける
            for j in range(7):
                if j in flop_flags:
                    flop.append(cards[j])
                else:
                    not_flop.append(cards[j])

            # 非Flop分をHandとTurn&River分に分ける
            for hands_flags in itertools.combinations([0,1,2,3],2):
                hands_flags = set(hands_flags)  # not_boardのうち、何番目(※0始まり)のカードがハンドか
                hand = list()                   # handのカード
                turn_river = list()             # TurnとRiverのカード

                for j in range(4):
                    if j in hands_flags:
                        hand.append(not_flop[j])
                    else:
                        turn_river.append(not_flop[j])

                # ここでflop,hand,turn_riverに対して、osdなのかgutなのか判定掛ければ良い
                # 多分重複組み合わせがありそうな気がするのでdictとかで管理すると良いかも。
