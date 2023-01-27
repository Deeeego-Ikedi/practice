###section6-1
##camus = "カミュ"
##print(camus[0])
##print(camus[1])
##print(camus[2])
##
##
###section6-2
##what = input("何を書く？:")
##who = input("誰に送る？:")
##
##sentence = "私は昨日{}を書いて、{}に送った！".format(what, who)
##print(sentence)
##
##
###section6-3
##sentence = "albous Huxley was born in 1894.".capitalize()
##print(sentence)
##
##
###section6-4
##sentence = "どこで？ 誰が？ いつ？"
##sentence = sentence.split(" ")
##sentence_list = [sentence[0], sentence[1], sentence[2]]
##
##print(sentence)
##print(sentence_list)
##
##
###section6-5
##words = ["The", "fox", "jumped", "over", "the", "fence", "."]
##sentence = " ".join(words)
##print(sentence)
##s = sentence.replace(" .", ".")
##print(s)
##
##
###section6-6
##sentence = "A screaming comes across the sky."
##sentence = sentence.replace("s", "$")
##print(sentence)
##
###section6-7
##"Hemingway".index("m")
##
##
###section6-8
##"吉田松陰は\"事を為すは誠にあり\"と遺した。"
##
##
###section6-9
##triple_three = "three"+"three"+"three"
##triple_three = triple_three.replace("et", "e t")
##print(triple_three)
##
##triple_three2 = "three"* 3
##triple_three2 = triple_three2.replace("et", "e t")
##print(triple_three2)
##
##
###section6-10
##sent = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。".split("、")
##print(sent)
