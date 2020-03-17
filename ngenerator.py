
import random

def main():
    i = 0
    namelist = []
    while(i < 12):
        start_syllabels = start_get_syllabels()
        r_ss = random.sample(start_syllabels, 1)
        end_syllabels = end_get_syllabels()
        r_es = random.sample(end_syllabels, 1)
        r_name = r_ss[0] + r_es[0]
        if check_name(r_name):
            i += 1
            namelist.append(r_name)
    return namelist
            

def check_name(name):
    for index, c in enumerate(name):
        if c == name[index + 1] and c == name[index + 2]:
            return False
        elif c == name[-3]:
            return True
            
def count_syllables(word):
    v = "aeiouy"
    v_set = set(v)
    count = 0
    l_word = word.lower()
    for c in l_word:
        if c in v_set:
            count += 1
        if l_word[-1] == "e":
            count -= 1
        return count

def start_get_syllabels():
    names = ["Ahkur","Ahtalg","Aliskeeh","Anash","Argar","Aseepa","Asheeus","Ashgar","Azeenus","Azinar","Azri","Bahrei","Bahtei","Balahkath","Banka","Barnaxi","Batuus","Beeheisei","Beenalz","Benas","Beshnus","Bewlus","Bezeer","Bijot","Bosekus","Bunishyeeth","Buujhan","Buxutheeus","Chakuk","Chalish","Chanka","Chatapnaza","Chilwir","Chitakus","Cholzei","Chosumeel","Choxusha","Chuxu","Chuzu","Claurth","Darasken","Dashnu","Debameel","Deegeeta","Deeheesotl","Deejeeta","Deekonus","Deekum","Deerlus","Demeepa","Derkeehez","Dezanu","Dowoseez","Dozaeek","Dramukkath","Drakaws","Dramukkath","Dreevureesh","Dritan","Drumarz","Druseesh","Druxith","Dunaxith","Eoki","Esqoo","Etsabeeh","Gatulm","Ghelos","Ghesee","Gilustulm","Grish","Guleesh","Halish","Hareeya","Haxal","Heetzasi","Hikathus","Hjorn","Hleezeireeus","Honan","Iggistill","Ilus","Iokkas","Iskenaaz","Jaraleet","Jeela","Jeelus","Jilux","Juut","Kalanu","Kamatpa","Kankeeus","Kaxutl","Keeko","Keemeen","Keenem","Keesekeeth","Keesu","Kepanuu","Kiameed","Klankaatu","Klor","Kloxu","Kluleesh","Klutsaan","Krona","Kudleez","Lohupeel","Losum","Lotaeel","Lotash","Luteema","Maahi","Maheelius","Makadel","Maneeshik","Markka","Mathei","Meejapa","Meenjee","Meenosh","Meensuda","Meewulm","Miharil","Mikeesh","Mobareed","Mohimeem","Mopakuz","Motuu","Mujeen","Muranatepa","Napetui","Naska","Naxaltan","Nazuux","Nebutil","Neelo","Neeluka","Neetzara","Neexi","Neposh","Netapatuu","Nexith","Nodeeus","Nomu","Nosaleeth","Notei","Nowajan","Nowajeem","Nuduxith","Nuleez","Nurhei","Obaxith","Ojei","Okalg","Okeeh","Onuja","Opatieel","Pacheeva","Pacheevutar","Parash","Paduxi","Paraxeeh","Paxalt","Peesha","Peexalt","Pejureel","Petaxai","Pideelus","Pimsy","Pojeel","Powaj","Powostulm","Radeelan","Radithax","Rareel","Rarez","Ratulmdutsei","Redieeus","Reeesh","Reekeesh","Reekisk","Resari","Rezei","Rultkath","Rupah","Rushmeek","Ruxol","Sakeeus","Seemarz","Sejaijilax","Shadutsei","Shuvu","Shakiis","Sinanis","Skalasha","Skasei","Skeehei","Skeewul","Sureeus","Tanaka","Teeka","Teelawei","Teineeja","Terezeeus","Tikaasi","Tikkus","Tlixilja","Tlosee","Topeth","Tsatheitepa","Tsilmtulm","Tsixotl","Tsoglaez","Tsoxolza","Tsurei","Tulalurash","Tuxo","Uaxal","Ukaspa","Ukatsei","Ulawa","Uralgnaza","Uraz","Ushmeek","Utadeek","Utamukeeus","Utatul","Uzeialus","Vaeshna","Veekas","Veelisheeh","Veenaza","Veexalt","Vintheel","Visskar","Voneesh","Vornan","Vozei","Vudeelal","Vukus","Vushtulm","Vuskayeeth","Wayiteh","Wixil","Wixulbeeh","Wunalz","Xazar","Xode","Xozuka","Xukas","Xuzu","Yelus","Yexil"]
    syl_start_all = set()
    for name in names:
        syl_start = name[:2]
        syl_start_all.add(syl_start)
    return syl_start_all

def end_get_syllabels():
    names = ["Ahkur","Ahtalg","Aliskeeh","Anash","Argar","Aseepa","Asheeus","Ashgar","Azeenus","Azinar","Azri","Bahrei","Bahtei","Balahkath","Banka","Barnaxi","Batuus","Beeheisei","Beenalz","Benas","Beshnus","Bewlus","Bezeer","Bijot","Bosekus","Bunishyeeth","Buujhan","Buxutheeus","Chakuk","Chalish","Chanka","Chatapnaza","Chilwir","Chitakus","Cholzei","Chosumeel","Choxusha","Chuxu","Chuzu","Claurth","Darasken","Dashnu","Debameel","Deegeeta","Deeheesotl","Deejeeta","Deekonus","Deekum","Deerlus","Demeepa","Derkeehez","Dezanu","Dowoseez","Dozaeek","Dramukkath","Drakaws","Dramukkath","Dreevureesh","Dritan","Drumarz","Druseesh","Druxith","Dunaxith","Eoki","Esqoo","Etsabeeh","Gatulm","Ghelos","Ghesee","Gilustulm","Grish","Guleesh","Halish","Hareeya","Haxal","Heetzasi","Hikathus","Hjorn","Hleezeireeus","Honan","Iggistill","Ilus","Iokkas","Iskenaaz","Jaraleet","Jeela","Jeelus","Jilux","Juut","Kalanu","Kamatpa","Kankeeus","Kaxutl","Keeko","Keemeen","Keenem","Keesekeeth","Keesu","Kepanuu","Kiameed","Klankaatu","Klor","Kloxu","Kluleesh","Klutsaan","Krona","Kudleez","Lohupeel","Losum","Lotaeel","Lotash","Luteema","Maahi","Maheelius","Makadel","Maneeshik","Markka","Mathei","Meejapa","Meenjee","Meenosh","Meensuda","Meewulm","Miharil","Mikeesh","Mobareed","Mohimeem","Mopakuz","Motuu","Mujeen","Muranatepa","Napetui","Naska","Naxaltan","Nazuux","Nebutil","Neelo","Neeluka","Neetzara","Neexi","Neposh","Netapatuu","Nexith","Nodeeus","Nomu","Nosaleeth","Notei","Nowajan","Nowajeem","Nuduxith","Nuleez","Nurhei","Obaxith","Ojei","Okalg","Okeeh","Onuja","Opatieel","Pacheeva","Pacheevutar","Parash","Paduxi","Paraxeeh","Paxalt","Peesha","Peexalt","Pejureel","Petaxai","Pideelus","Pimsy","Pojeel","Powaj","Powostulm","Radeelan","Radithax","Rareel","Rarez","Ratulmdutsei","Redieeus","Reeesh","Reekeesh","Reekisk","Resari","Rezei","Rultkath","Rupah","Rushmeek","Ruxol","Sakeeus","Seemarz","Sejaijilax","Shadutsei","Shuvu","Shakiis","Sinanis","Skalasha","Skasei","Skeehei","Skeewul","Sureeus","Tanaka","Teeka","Teelawei","Teineeja","Terezeeus","Tikaasi","Tikkus","Tlixilja","Tlosee","Topeth","Tsatheitepa","Tsilmtulm","Tsixotl","Tsoglaez","Tsoxolza","Tsurei","Tulalurash","Tuxo","Uaxal","Ukaspa","Ukatsei","Ulawa","Uralgnaza","Uraz","Ushmeek","Utadeek","Utamukeeus","Utatul","Uzeialus","Vaeshna","Veekas","Veelisheeh","Veenaza","Veexalt","Vintheel","Visskar","Voneesh","Vornan","Vozei","Vudeelal","Vukus","Vushtulm","Vuskayeeth","Wayiteh","Wixil","Wixulbeeh","Wunalz","Xazar","Xode","Xozuka","Xukas","Xuzu","Yelus","Yexil"]
    syl_end_all = set()
    for name in names:
        syl_end = name[3:]
        syl_end_all.add(syl_end)
    return syl_end_all

if __name__ == "__main__":
    main()