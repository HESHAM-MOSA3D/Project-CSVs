import csv

data = {
    "Gebna Beda ma Zeitoun": {
        "English": ["Gebna Beda ma Zeitoun", "Gebna Beda ma Zeitoon"],
        "Arabic": ["جبنة بيضا بالزيتون"],
        "Franco": ["Gebna beda bel zaytoon", "Gebna beida bel zaytoon"]
    },
    "Zabady bel Asal wal Mekasarat": {
        "English": ["Zabady bel Asal wal Mekasarat", "Zabadi bel Asal"],
        "Arabic": ["زبادي بالعسل والمكسرات"],
        "Franco": ["Zabady bel 3asal wal mekasarat"]
    },
    "Ful Nabet bel Salata": {
        "English": ["Ful Nabet bel Salata", "Foul Nabet", "Ful Nabet"],
        "Arabic": ["فول نابت بالسلطة"],
        "Franco": ["Foul nabet bel salata"]
    },
    "Basterma Mashwia": {
        "English": ["Basterma Mashwia", "Grilled Basturma", "Basterma Mashweya"],
        "Arabic": ["بسطرمة مشوية"],
        "Franco": ["Basterma mashweya"]
    },
    "Homos Sham Mohammas": {
        "English": ["Homos Sham Mohammas", "Roasted Chickpeas", "Hommos Sham"],
        "Arabic": ["حمص شام محمص"],
        "Franco": ["7ommos sham me7ammas"]
    },
    "Aish Baladi Homemade": {
        "English": ["Aish Baladi Homemade", "Homemade Aish Baladi", "Aish Baladi"],
        "Arabic": ["عيش بلدي بيتي", "عيش بلدي"],
        "Franco": ["3esh balady"]
    },
    "Semit Masri": {
        "English": ["Semit Masri", "Egyptian Simit", "Semiet"],
        "Arabic": ["سميط مصري", "سميط"],
        "Franco": ["Semeet masry", "Semeet"]
    },
    "Fiteer bel Gebna wal Basterma": {
        "English": ["Fiteer bel Gebna wal Basterma", "Fiteer Basterma"],
        "Arabic": ["فطير بالجبنة والبسطرمة"],
        "Franco": ["Feteer bel gebna wal basterma"]
    },
    "Shorbet Kishk": {
        "English": ["Shorbet Kishk", "Kishk Soup"],
        "Arabic": ["شوربة كشك"],
        "Franco": ["Shorbet keshk"]
    },
    "Kishk bel Samna": {
        "English": ["Kishk bel Samna"],
        "Arabic": ["كشك بالسمنة"],
        "Franco": ["Keshk bel samna"]
    },
    "Shorbet Sha'ria": {
        "English": ["Shorbet Sha'ria", "Orzo Soup", "Lesan Asfour Soup"],
        "Arabic": ["شوربة شعرية"],
        "Franco": ["Shorbet sha3reya"]
    },
    "Shorbet Samak": {
        "English": ["Shorbet Samak", "Seafood Soup"],
        "Arabic": ["شوربة سمك", "شوربة سي فود"],
        "Franco": ["Shorbet samak", "Shorbet seafood"]
    },
    "Shorbet Hamam": {
        "English": ["Shorbet Hamam", "Pigeon Soup"],
        "Arabic": ["شوربة حمام"],
        "Franco": ["Shorbet 7amam"]
    },
    "Salatet Tahina Sada": {
        "English": ["Salatet Tahina Sada", "Tahini Salad", "Tahina"],
        "Arabic": ["سلطة طحينة سادة", "سلطة طحينة"],
        "Franco": ["Salatet te7ina"]
    },
    "Salsa Toum": {
        "English": ["Salsa Toum", "Salsa Toom", "Garlic Sauce", "Tomia"],
        "Arabic": ["صلصة ثوم", "تومية"],
        "Franco": ["Salset tom", "Tomeya"]
    },
    "Salatet Zabadi bel Toum": {
        "English": ["Salatet Zabadi bel Toum", "Yogurt Salad with Garlic", "Salatet Zabadi"],
        "Arabic": ["سلطة زبادي بالثوم", "سلطة زبادي"],
        "Franco": ["Salatet zabady bel tom"]
    },
    "Dukkah Masri": {
        "English": ["Dukkah Masri", "Egyptian Dukkah", "Duqqa"],
        "Arabic": ["دقة مصرية", "دقة"],
        "Franco": ["Do22a masreya", "Do22a"]
    },
    "Ful Akhdar bel Lahma": {
        "English": ["Ful Akhdar bel Lahma", "Foul Akhdar", "Green Fava Beans with Meat"],
        "Arabic": ["فول أخضر باللحمة"],
        "Franco": ["Foul a5dar bel la7ma"]
    },
    "Loubia Khadra bel Lahma": {
        "English": ["Loubia Khadra bel Lahma", "Loobia Khadra bel Lahma", "Green Beans with Meat"],
        "Arabic": ["لوبيا خضرا باللحمة", "لوبيا باللحمة"],
        "Franco": ["Loubya 5adra bel la7ma"]
    },
    "Qolqas bel Lahma": {
        "English": ["Qolqas bel Lahma", "Colocasia with Meat", "Taro with Meat", "Qolqas"],
        "Arabic": ["قلقاس باللحمة", "قلقاس"],
        "Franco": ["2ol2as bel la7ma"]
    },
    "Habb Al-Aziz Muhamas": {
        "English": ["Habb Al-Aziz Muhamas", "Roasted Tiger Nuts"],
        "Arabic": ["حب العزيز محمص", "حب العزيز"],
        "Franco": ["7abb el 3azeez me7ammas"]
    },
    "Fasolia Khadra bel Lahma": {
        "English": ["Fasolia Khadra bel Lahma", "Fasolia Khadra"],
        "Arabic": ["فاصوليا خضرا باللحمة", "فاصوليا باللحمة"],
        "Franco": ["Fasoulya 5adra bel la7ma"]
    },
    "Bazella bel Lahma": {
        "English": ["Bazella bel Lahma", "Besella bel Lahma", "Peas and Carrots with Meat"],
        "Arabic": ["بسلة باللحمة"],
        "Franco": ["Besella bel la7ma"]
    },
    "Sabanekh bel Lahma": {
        "English": ["Sabanekh bel Lahma", "Spinach with Meat", "Sabanekh"],
        "Arabic": ["سبانخ باللحمة"],
        "Franco": ["Sabanek5 bel la7ma"]
    },
    "Salatet Sabanekh": {
        "English": ["Salatet Sabanekh", "Spinach Salad"],
        "Arabic": ["سلطة سبانخ"],
        "Franco": ["Salatet sabane5"]
    },
    "Silq bel Lahma": {
        "English": ["Silq bel Lahma", "Swiss Chard with Meat"],
        "Arabic": ["سلق باللحمة"],
        "Franco": ["Sel2 bel la7ma"]
    },
    "Kousa bel Lahma": {
        "English": ["Kousa bel Lahma", "Koosa bel Lahma", "Zucchini with Meat"],
        "Arabic": ["كوسة باللحمة"],
        "Franco": ["Kousa bel la7ma"]
    },
    "Batates bel Lahma": {
        "English": ["Batates bel Lahma", "Potato with Meat", "Saniyet Batates"],
        "Arabic": ["بطاطس باللحمة", "صينية بطاطس باللحمة"],
        "Franco": ["Batates bel la7ma", "Saneyet batates"]
    },
    "Torshi Betengan": {
        "English": ["Torshi Betengan", "Pickled Eggplant"],
        "Arabic": ["طرشي بتنجان", "بتنجان مخلل"],
        "Franco": ["Torshy betengan", "Betengan me5allel"]
    },
    "Torshi Malfouf": {
        "English": ["Torshi Malfouf", "Pickled Cabbage", "Torshi Koromb"],
        "Arabic": ["طرشي ملفوف", "كرنب مخلل"],
        "Franco": ["Torshy malfouf", "Koromb me5allel"]
    },
    "Torshi Left": {
        "English": ["Torshi Left", "Pickled Turnip"],
        "Arabic": ["طرشي لفت", "لفت مخلل"],
        "Franco": ["Torshy left", "Left me5allel"]
    },
    "Torshi Gazar": {
        "English": ["Torshi Gazar", "Pickled Carrots"],
        "Arabic": ["طرشي جزر", "جزر مخلل"],
        "Franco": ["Torshy gazar", "Gazar me5allel"]
    },
    "Torshi Khiar": {
        "English": ["Torshi Khiar", "Pickled Cucumber"],
        "Arabic": ["طرشي خيار", "خيار مخلل"],
        "Franco": ["Torshy 5yar", "5yar me5allel"]
    },
    "Torshi Basal": {
        "English": ["Torshi Basal", "Pickled Onions"],
        "Arabic": ["طرشي بصل", "بصل مخلل"],
        "Franco": ["Torshy basal", "Basal me5allel"]
    },
    "Torshi Filfil": {
        "English": ["Torshi Filfil", "Pickled Peppers"],
        "Arabic": ["طرشي فلفل", "فلفل مخلل"],
        "Franco": ["Torshy felfel", "Felfel me5allel"]
    },
    "Salatet Betengan Mashwi": {
        "English": ["Salatet Betengan Mashwi", "Baba Ghanoush", "Grilled Eggplant Salad"],
        "Arabic": ["سلطة بتنجان مشوي", "بابا غنوج"],
        "Franco": ["Salatet betengan mashwy", "Baba ghanoug"]
    },
    "Salatet Loubia": {
        "English": ["Salatet Loubia", "Black Eyed Peas Salad", "Salatet Loobia"],
        "Arabic": ["سلطة لوبيا"],
        "Franco": ["Salatet loubya"]
    },
    "Salatet Fasolia Beida": {
        "English": ["Salatet Fasolia Beida", "White Bean Salad", "Fasolia Salad"],
        "Arabic": ["سلطة فاصوليا بيضا"],
        "Franco": ["Salatet fasoulya beida"]
    },
    "Salatet Batates": {
        "English": ["Salatet Batates", "Potato Salad"],
        "Arabic": ["سلطة بطاطس"],
        "Franco": ["Salatet batates"]
    },
    "Salatet Bengar": {
        "English": ["Salatet Bengar", "Beetroot Salad"],
        "Arabic": ["سلطة بنجر"],
        "Franco": ["Salatet bangar"]
    },
    "Salatet Filfil Mashwi": {
        "English": ["Salatet Filfil Mashwi", "Grilled Pepper Salad"],
        "Arabic": ["سلطة فلفل مشوي"],
        "Franco": ["Salatet felfel mashwy"]
    },
    "Salatet Karnabeet": {
        "English": ["Salatet Karnabeet", "Cauliflower Salad"],
        "Arabic": ["سلطة قرنبيط"],
        "Franco": ["Salatet arnabyt"]
    },
    "Karnabeet Meqli bel Tahina": {
        "English": ["Karnabeet Meqli bel Tahina", "Fried Cauliflower with Tahini"],
        "Arabic": ["قرنبيط مقلي بالطحينة", "قرنبيط مقلي"],
        "Franco": ["Arnabyt me2ly", "Arnabyt ma2ly"]
    },
    "Mahshi Koussa bi Roz": {
        "English": ["Mahshi Koussa bi Roz", "Mahshi Koossa bi Roz", "Stuffed Zucchini"],
        "Arabic": ["محشي كوسة بالرز", "محشي كوسة"],
        "Franco": ["Ma7shy kousa"]
    },
    "Mahshi Betengan bi Roz": {
        "English": ["Mahshi Betengan bi Roz", "Stuffed Eggplant"],
        "Arabic": ["محشي بتنجان بالرز", "محشي بتنجان"],
        "Franco": ["Ma7shy betengan"]
    },
    "Mahshi Filfil bi Roz": {
        "English": ["Mahshi Filfil bi Roz", "Stuffed Peppers"],
        "Arabic": ["محشي فلفل بالرز", "محشي فلفل"],
        "Franco": ["Ma7shy felfel"]
    },
    "Mahshi Tamatem": {
        "English": ["Mahshi Tamatem", "Stuffed Tomatoes"],
        "Arabic": ["محشي طماطم"],
        "Franco": ["Ma7shy tamatem"]
    },
    "Mahshi Basal": {
        "English": ["Mahshi Basal", "Stuffed Onions"],
        "Arabic": ["محشي بصل"],
        "Franco": ["Ma7shy basal"]
    },
    "Mahshi Silq bi Roz": {
        "English": ["Mahshi Silq bi Roz", "Stuffed Swiss Chard"],
        "Arabic": ["محشي سلق بالرز"],
        "Franco": ["Ma7shy sel2"]
    },
    "Filfil Mahshi bel Freekeh": {
        "English": ["Filfil Mahshi bel Freekeh", "Peppers Stuffed with Freekeh"],
        "Arabic": ["فلفل محشي بالفريك"],
        "Franco": ["Felfel ma7shy bel feryk"]
    },
    "Ardi Shawki Mahshi bel Lahma": {
        "English": ["Ardi Shawki Mahshi bel Lahma", "Stuffed Artichokes with Meat"],
        "Arabic": ["خرشوف محشي باللحمة", "أرضي شوكي محشي"],
        "Franco": ["5arshouf ma7shy bel la7ma"]
    },
    "Ardi Shawki bel Zeit wal Limon": {
        "English": ["Ardi Shawki bel Zeit wal Limon", "Artichokes with Oil and Lemon"],
        "Arabic": ["خرشوف بالزيت والليمون"],
        "Franco": ["5arshouf bel zeit wal lamoun"]
    },
    "Dawood Basha": {
        "English": ["Dawood Basha", "Dawoud Basha", "Meatballs in Tomato Sauce"],
        "Arabic": ["داوود باشا"],
        "Franco": ["Dawood basha"]
    },
    "Kofta bel Batates": {
        "English": ["Kofta bel Batates", "Kofta with Potatoes", "Saniyet Kofta"],
        "Arabic": ["كفتة بالبطاطس", "صينية كفتة بالبطاطس"],
        "Franco": ["Kofta bel batates", "Saneyet kofta"]
    },
    "Kofta Halla": {
        "English": ["Kofta Halla"],
        "Arabic": ["كفتة حلة"],
        "Franco": ["Kofta 7alla"]
    },
    "Kammounia bel Lahma": {
        "English": ["Kammounia bel Lahma", "Kammoonia bel Lahma"],
        "Arabic": ["كمونية باللحمة"],
        "Franco": ["Kammouneya bel la7ma"]
    },
    "Kubeba Maqliya": {
        "English": ["Kubeba Maqliya", "Kobeiba", "Fried Kibbeh"],
        "Arabic": ["كبيبة مقلية", "كبيبة"],
        "Franco": ["Kobeiba ma2leya", "Kobeiba"]
    },
    "Fatta bel Aranib": {
        "English": ["Fatta bel Aranib", "Rabbit Fatteh"],
        "Arabic": ["فتة بالأرانب", "فتة أرانب"],
        "Franco": ["Fatta bel araneb"]
    },
    "Firakh bel Furn": {
        "English": ["Firakh bel Furn", "Roasted Chicken", "Baked Chicken"],
        "Arabic": ["فراخ في الفرن", "فراخ مشوية"],
        "Franco": ["Fera5 bel forn"]
    },
    "Fattet Firakh": {
        "English": ["Fattet Firakh", "Chicken Fatteh"],
        "Arabic": ["فتة فراخ"],
        "Franco": ["Fattet fera5"]
    },
    "Fattet Gambari": {
        "English": ["Fattet Gambari", "Shrimp Fatteh"],
        "Arabic": ["فتة جمبري"],
        "Franco": ["Fattet gambary"]
    },
    "Kalawi Mashwiya": {
        "English": ["Kalawi Mashwiya", "Grilled Kidneys"],
        "Arabic": ["كلاوي مشوية", "كلاوي"],
        "Franco": ["Kalawy mashweya"]
    },
    "Kibda Mashwia": {
        "English": ["Kibda Mashwia", "Grilled Liver", "Kibda Mashweya"],
        "Arabic": ["كبدة مشوية", "كبدة ردة"],
        "Franco": ["Kebda mashweya", "Kebda bel radda"]
    },
    "Lisan Mashwi": {
        "English": ["Lisan Mashwi", "Grilled Tongue"],
        "Arabic": ["لسان مشوي"],
        "Franco": ["Lesan mashwy"]
    },
    "Lisan Salata": {
        "English": ["Lisan Salata", "Tongue Salad"],
        "Arabic": ["سلطة لسان"],
        "Franco": ["Salatet lesan"]
    },
    "Tehal Eskandarani": {
        "English": ["Tehal Eskandarani", "Alexandrian Spleen"],
        "Arabic": ["طحال إسكندراني", "طحال"],
        "Franco": ["To7al eskandarany"]
    },
    "Deek Rumi bel Furn": {
        "English": ["Deek Rumi bel Furn", "Roasted Turkey"],
        "Arabic": ["ديك رومي في الفرن", "ديك رومي"],
        "Franco": ["Deek roumy bel forn"]
    },
    "Hamam Mahshi Freekeh": {
        "English": ["Hamam Mahshi Freekeh", "Stuffed Pigeons with Freekeh"],
        "Arabic": ["حمام محشي فريك"],
        "Franco": ["7amam ma7shy feryk"]
    },
    "Molokhia bel Gambari": {
        "English": ["Molokhia bel Gambari", "Molokhia with Shrimp"],
        "Arabic": ["ملوخية بالجمبري"],
        "Franco": ["Molou5eya bel gambary"]
    },
    "Molokhia Yabsa bel Thoum": {
        "English": ["Molokhia Yabsa bel Thoum", "Molokhia Yabsa bel Thoom", "Dried Molokhia"],
        "Arabic": ["ملوخية ناشفة بالثوم", "ملوخية ناشفة"],
        "Franco": ["Molou5eya nashfa"]
    },
    "Sayadeya Gambari": {
        "English": ["Sayadeya Gambari", "Shrimp Sayadeya"],
        "Arabic": ["صيادية جمبري"],
        "Franco": ["Sayadeyet gambary"]
    },
    "Samak Eskandarani": {
        "English": ["Samak Eskandarani", "Alexandrian Fish", "Saniyet Samak"],
        "Arabic": ["سمك إسكندراني", "صينية سمك"],
        "Franco": ["Samak eskandarany", "Saneyet samak"]
    },
    "Ankaleesh Mashwi": {
        "English": ["Ankaleesh Mashwi", "Grilled Eel", "Tho'ban Samak"],
        "Arabic": ["حنشان مشوي", "ثعبان سمك مشوي"],
        "Franco": ["7enshan mashwy"]
    },
    "Renga Salad": {
        "English": ["Renga Salad", "Smoked Herring Salad"],
        "Arabic": ["سلطة رنجة"],
        "Franco": ["Salatet renga"]
    },
    "Renga Mashwia": {
        "English": ["Renga Mashwia", "Grilled Smoked Herring"],
        "Arabic": ["رنجة مشوية"],
        "Franco": ["Renga mashweya"]
    },
    "Sardin Mekhalel": {
        "English": ["Sardin Mekhalel", "Pickled Sardines", "Fesikh Sardines"],
        "Arabic": ["سردين مخلل"],
        "Franco": ["Sardeen me5allel"]
    },
    "Bream Mashwi": {
        "English": ["Bream Mashwi", "Bolti Mashwi", "Grilled Tilapia"],
        "Arabic": ["بلطي مشوي", "سمك مشوي"],
        "Franco": ["Bolty mashwy"]
    },
    "Kaboria bel Salsa": {
        "English": ["Kaboria bel Salsa", "Crabs in Sauce"],
        "Arabic": ["كابوريا بالصلصة", "كابوريا"],
        "Franco": ["Kaborya bel salsa"]
    },
    "Gambari bel Thoum": {
        "English": ["Gambari bel Thoum", "Gambari bel Thoom", "Garlic Shrimp"],
        "Arabic": ["جمبري بالثوم"],
        "Franco": ["Gambary bel tom"]
    },
    "Roz Muammar": {
        "English": ["Roz Muammar", "Baked Rice", "Roz Meammar"],
        "Arabic": ["رز معمر", "أرز معمر"],
        "Franco": ["Roz me3ammar"]
    },
    "Roz bel Foul Akhdar": {
        "English": ["Roz bel Foul Akhdar", "Roz bel Fool Akhdar", "Rice with Green Fava Beans"],
        "Arabic": ["رز بالفول الأخضر"],
        "Franco": ["Roz bel foul el a5dar"]
    },
    "Roz bel Lahma": {
        "English": ["Roz bel Lahma", "Rice with Meat"],
        "Arabic": ["رز باللحمة"],
        "Franco": ["Roz bel la7ma"]
    },
    "Ruz bel Loubia": {
        "English": ["Ruz bel Loubia", "Ruz bel Loobia", "Rice with Black Eyed Peas"],
        "Arabic": ["رز باللوبيا"],
        "Franco": ["Roz bel loubya"]
    },
    "Macarona bel Zeit": {
        "English": ["Macarona bel Zeit", "Pasta with Oil"],
        "Arabic": ["مكرونة بالزيت"],
        "Franco": ["Macarona bel zeit"]
    },
    "Macarona bel Gambari": {
        "English": ["Macarona bel Gambari", "Shrimp Pasta"],
        "Arabic": ["مكرونة بالجمبري"],
        "Franco": ["Macarona bel gambary"]
    },
    "Sabanekh bel Gambari": {
        "English": ["Sabanekh bel Gambari", "Spinach with Shrimp"],
        "Arabic": ["سبانخ بالجمبري"],
        "Franco": ["Sabane5 bel gambary"]
    },
    "Amar El Din": {
        "English": ["Amar El Din", "Qamar al-Din", "Apricot Juice"],
        "Arabic": ["قمر الدين", "عصير قمر الدين"],
        "Franco": ["Amar el dyn"]
    },
    "Tamarhindi": {
        "English": ["Tamarhindi", "Tamarind Drink", "Tamr Hindi"],
        "Arabic": ["تمرهندي", "تمر هندي"],
        "Franco": ["Tamr hendy"]
    },
    "Sobia": {
        "English": ["Sobia", "Coconut Milk Drink"],
        "Arabic": ["سوبيا", "عصير سوبيا"],
        "Franco": ["Sobya"]
    },
    "Ganzabil": {
        "English": ["Ganzabil", "Ginger Drink"],
        "Arabic": ["جنزبيل", "زنجبيل"],
        "Franco": ["Ganzabeel"]
    },
    "Asir Asab bel Limon": {
        "English": ["Asir Asab bel Limon", "Sugarcane Juice with Lemon"],
        "Arabic": ["عصير قصب بالليمون", "عصير قصب"],
        "Franco": ["3aseer asab bel lamoun", "3aseer asab"]
    },
    "Khoshaf Ramadan": {
        "English": ["Khoshaf Ramadan", "Dried Fruit Compote", "Khoshaf"],
        "Arabic": ["خشاف رمضان", "خشاف"],
        "Franco": ["5oshaf"]
    },
    "Basbousa bel Gozz Hindi": {
        "English": ["Basbousa bel Gozz Hindi", "Basboosa bel Gozz Hindi", "Coconut Basbousa"],
        "Arabic": ["بسبوسة بجوز الهند", "بسبوسة"],
        "Franco": ["Basbousa bel goz hend", "Basbousa"]
    },
    "Qatayef Asafiri": {
        "English": ["Qatayef Asafiri", "Mini Qatayef", "Atayef Asafiri"],
        "Arabic": ["قطايف عصافيري", "قطايف"],
        "Franco": ["2atayef 3asafyry", "Atayef"]
    },
    "Kahk bel Gozz": {
        "English": ["Kahk bel Gozz", "Kahk with Walnuts"],
        "Arabic": ["كحك بالجوز", "كحك العيد"],
        "Franco": ["Ka7k bel goz", "Ka7k"]
    },
    "Mishmoshiya": {
        "English": ["Mishmoshiya", "Apricot Pudding"],
        "Arabic": ["مشمشية"],
        "Franco": ["Meshmesheya"]
    },
    "Loz Msakar": {
        "English": ["Loz Msakar", "Sugared Almonds"],
        "Arabic": ["لوز مسكر"],
        "Franco": ["Loz mesakkar"]
    },
    "Fool Sudani Muhammas": {
        "English": ["Fool Sudani Muhammas", "Roasted Peanuts"],
        "Arabic": ["فول سوداني محمص", "سوداني محمص"],
        "Franco": ["Foul soudany me7ammas", "Soudany me7ammas"]
    },
    "Mekasarat Muhamasa": {
        "English": ["Mekasarat Muhamasa", "Roasted Nuts", "Mixed Nuts"],
        "Arabic": ["مكسرات محمصة", "مكسرات"],
        "Franco": ["Mekassarat me7ammasa"]
    },
    "Balah Mahshi bel Mekasarat": {
        "English": ["Balah Mahshi bel Mekasarat", "Stuffed Dates with Nuts"],
        "Arabic": ["بلح محشي بالمكسرات", "تمر محشي"],
        "Franco": ["Bala7 ma7shy bel mekassarat"]
    },
    "Koshari": {
        "English": ["Koshari", "Koshary", "Kosheri"],
        "Arabic": ["كشري"],
        "Franco": ["Koshary"]
    },
    "Molokhia": {
        "English": ["Molokhia", "Molokheya", "Mulukhiyah"],
        "Arabic": ["ملوخية"],
        "Franco": ["Molou5eya"]
    },
    "Mahshi Waraq Enab": {
        "English": ["Mahshi Waraq Enab", "Mahshi Warak Enab", "Stuffed Grape Leaves"],
        "Arabic": ["محشي ورق عنب"],
        "Franco": ["Mahshi wara2 enab", "Mahshi war2 enab"]
    },
    "Ful Medames": {
        "English": ["Ful Medames", "Foul Medammes", "Foul Medames"],
        "Arabic": ["فول مدمس"],
        "Franco": ["Foul", "Ful Medames"]
    },
    "Taameya": {
        "English": ["Taameya", "Taamia", "Falafel Egyptian"],
        "Arabic": ["طعمية"],
        "Franco": ["Ta3meya", "Ta3ameya"]
    },
    "Macarona Bechamel": {
        "English": ["Macarona Bechamel", "Macarona Béchamel", "Baked Pasta with Bechamel"],
        "Arabic": ["مكرونة بشاميل", "مكرونة بالبشاميل"],
        "Franco": ["Macarona beshamel"]
    },
    "Om Ali": {
        "English": ["Om Ali", "Umm Ali", "Omm Ali"],
        "Arabic": ["أم علي"],
        "Franco": ["Om 3aly"]
    },
    "Moussaka Masreya": {
        "English": ["Moussaka Masreya", "Moossaka Masreya", "Egyptian Moussaka", "Mesa'a'ah"],
        "Arabic": ["مسقعة مصرية", "مسقعة"],
        "Franco": ["Mesa2a3a masreya", "Mesa2a3a"]
    },
    "Roz Bel Laban": {
        "English": ["Roz Bel Laban", "Rice Pudding", "Roz be Laban"],
        "Arabic": ["أرز باللبن", "رز باللبن"],
        "Franco": ["Roz bel laban"]
    },
    "Sayadeya": {
        "English": ["Sayadeya", "Sayadiya", "Egyptian Fishermans Rice"],
        "Arabic": ["صيادية", "رز صيادية"],
        "Franco": ["Sayadeya", "Roz sayadeya"]
    },
    "Kofta Mashweya": {
        "English": ["Kofta Mashweya", "Grilled Kofta"],
        "Arabic": ["كفتة مشوية", "كفتة الحاتي"],
        "Franco": ["Kofta mashweya", "Koftat el 7aty"]
    },
    "Fatteh Masreya": {
        "English": ["Fatteh Masreya", "Egyptian Fatteh", "Fatta"],
        "Arabic": ["فتة مصرية", "فتة بالخل والثوم"],
        "Franco": ["Fatta masreya"]
    },
    "Shorbet Adss": {
        "English": ["Shorbet Adss", "Lentil Soup", "Shorbet Ads"],
        "Arabic": ["شوربة عدس"],
        "Franco": ["Shorbet 3ads"]
    },
    "Shakshouka Masreya": {
        "English": ["Shakshouka Masreya", "Shakshooka Masreya", "Egyptian Shakshouka"],
        "Arabic": ["شكشوكة مصرية", "شكشوكة"],
        "Franco": ["Shakshouka masreya", "Shakshouka"]
    },
    "Kabab Halla": {
        "English": ["Kabab Halla", "Kebab Halla", "Egyptian Beef Stew"],
        "Arabic": ["كباب حلة"],
        "Franco": ["Kabab 7alla"]
    },
    "Tagen Bamia Bel Lahma": {
        "English": ["Tagen Bamia Bel Lahma", "Okra Tagine with Meat", "Bamia bel Lahma"],
        "Arabic": ["طاجن بامية باللحمة", "بامية باللحمة"],
        "Franco": ["Tagen bamya bel la7ma", "Bamya bel la7ma"]
    },
    "Salatat Baladi": {
        "English": ["Salatat Baladi", "Salata Baladi", "Egyptian Salad"],
        "Arabic": ["سلطة بلدي", "سلطة خضراء"],
        "Franco": ["Salata balady"]
    },
    "Baid Bel Basterma": {
        "English": ["Baid Bel Basterma", "Eggs with Basturma", "Eggs and Basterma"],
        "Arabic": ["بيض بالبسطرمة"],
        "Franco": ["Beed bel basterma"]
    },
    "Hawawshi": {
        "English": ["Hawawshi", "Egyptian Meat Pie", "Hawawshy"],
        "Arabic": ["حواوشي"],
        "Franco": ["7awawshy"]
    },
    "Kebda Iskandarani": {
        "English": ["Kebda Iskandarani", "Alexandrian Liver", "Kebda Eskandarani"],
        "Arabic": ["كبدة إسكندراني"],
        "Franco": ["Kebda eskandarany"]
    }
}

with open(r"f:\projects\iti projects\Project-CSVs\RecipeAliases.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["RecipeName", "Alias", "Language"])
    for recipe, langs in data.items():
        for lang, aliases in langs.items():
            for alias in aliases:
                writer.writerow([recipe, alias, lang])
