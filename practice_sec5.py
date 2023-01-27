###section5-1
##musician = []
##musician.append("Kobukuro")
##musician.append("Yuzu")
##musician.append("Kensi Yonezu")
##musician.append("Mr.Children")
##
##print(musician)
##
##
###section5-2
##hamamatsu = ["34.77", "137.74"]
##kodaira = ["35.73", "139.50"]
##fukuoka = ["33.57", "130.39"]
##
##place = (hamamatsu, kodaira, fukuoka)
##
##print(place)
##
##
###section5-3
##daigo = {"height": "163.5",
##         "weight": "62.0"}
##daigo["color"] = "orange"
##
##print(daigo)
##
###section5-4
##characteristics = input("特徴を入力してください:")
##
##if characteristics in daigo:
##    daigo_char = daigo[characteristics]
##    print(daigo_char)
##else:
##    print("見つかりません。追加しておきます。")
##    ans = input("その特徴の答えを教えてください。:")
##    daigo[characteristics] = ans
##    print(daigo)
##
##
###section5-5
##musician = {}
##musician["Kobukuro"] = ["Yell", "ここにしか咲かない花", "宝島", "愛する人よ"]
##musician["Yuzu"] = ["Yesterday & Tomorrow", "逢いたい", "虹"]
##musician["Mr.Children"] = ["Hanabi", "しるし", "名もなき詩", "水上バス"]
##
##print(musician)
##
##
###section5-6
##set型は要素を追加したり削除したりできるmutableな型。
##set型と同じく集合演算などのメソッドを持っているがimmutableなfrozenset型もある。
