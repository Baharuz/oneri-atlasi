"""Katalog genişletme taslağı.

Biçim: ad | tür | temalar | atmosfer | esere özgü Türkçe açıklama.
Bu kayıtlar görsel kaynağı ve lisansı tamamlanana kadar seed'e dahil edilmez.
"""

DATA = {
    "kitap": """Karanlığın Sol Eli|bilimkurgu|kimlik,siyasi entrika,keşif|sakin,düşündürücü|Elçi Genly Ai, Gethen gezegeninde ittifak ararken yerel kültürün cinsiyet ve sadakat anlayışını öğrenir.
Mülksüzler|bilimkurgu|özgürlük,sınıf,siyasi entrika|düşündürücü,umutlu|Fizikçi Shevek, iki komşu dünyanın farklı toplumsal düzenleri arasında bilimsel fikrini ve özgürlük arayışını taşır.
Solaris|bilimkurgu|kimlik,gizem,gerçeklik|sakin,karanlık|Psikolog Kris Kelvin, okyanusla kaplı gezegendeki istasyona vardığında mürettebatın geçmişinden gelen canlı anılarla karşılaşır.
Çocukluğun Sonu|bilimkurgu|güç,kimlik,gerçeklik|düşündürücü,tekinsiz|Dünya'ya gelen Üstün Akıllar barışı sağlar; insanlık ise bu müdahalenin geleceği için ne anlama geldiğini öğrenmeye çalışır.
Mars Yıllıkları|bilimkurgu|keşif,sömürgecilik,yalnızlık|melankolik,düşündürücü|Mars'a yerleşen insanların birbirine bağlı öyküleri, yeni bir dünyaya taşınan eski alışkanlıkları ve kayıpları gösterir.
Androidler Elektrikli Koyun Düşler mi?|bilimkurgu|kimlik,teknoloji,vicdan|karanlık,düşündürücü|Rick Deckard kaçak androidlerin peşine düşerken canlı olmanın ve empati kurmanın sınırlarını sorgular.
2001: Bir Uzay Destanı|bilimkurgu|keşif,teknoloji,gerçeklik|gizemli,destansı|Ay'da bulunan esrarengiz bir nesne, insanlığı Jüpiter yönünde bir göreve ve bilinmeyen bir evrimsel eşiğe götürür.
Rama ile Buluşma|bilimkurgu|keşif,gizem,teknoloji|gizemli,destansı|Güneş sistemine giren dev silindirik araç, bir uzay ekibini yabancı bir uygarlığın izlerini incelemeye çağırır.
Leviathan Uyanıyor|bilimkurgu|siyasi entrika,gizem,hayatta kalma|gerilimli,destansı|Kayıp bir genç kadının izi, dedektif Miller ile Holden'ın mürettebatını gezegenler arası bir krizin merkezine çeker.
Üç Cisim Problemi|bilimkurgu|teknoloji,gizem,güç|gerilimli,düşündürücü|Çin'in yakın geçmişindeki bir bilimsel çalışma, Dünya'nın geleceğini etkileyecek yabancı bir uygarlıkla temasın kapısını aralar.
Hyperion|bilimkurgu|inanç,kişisel yolculuk,ayrıntılı evren|destansı,gizemli|Yedi yolcu, Hyperion gezegenindeki ölümcül varlığa yaklaşırken kendilerini oraya getiren hikâyeleri anlatır.
Çöl Gezegeni Mesihi|bilimkurgu|güç,siyasi entrika,kimlik|karanlık,düşündürücü|İmparator olan Paul Atreides, kendi adına yürütülen savaşın ve geleceği görme yeteneğinin bedeliyle yüzleşir.
Kızıl İsyan|bilimkurgu|sınıf,özgürlük,güç|gerilimli,destansı|Mars'ın yeraltında çalışan Darrow, toplumun gerçek düzenini öğrenince üst sınıfın içine sızmak için kimliğini değiştirir.
Silo|distopya|gizem,özgürlük,hayatta kalma|karanlık,gerilimli|İnsanların yeraltı silosunda yaşadığı bir gelecekte Juliette, dış dünya hakkındaki kuralları ve geçmişi araştırır.
İstasyon On Bir|distopya|hayatta kalma,sanat,dostluk|melankolik,umutlu|Salgın öncesi ve sonrasını izleyen karakterler, gezici bir tiyatro topluluğuyla kültürü yaşatmanın anlamını arar.
Damızlık Kızın Öyküsü|distopya|özgürlük,güç,kimlik|karanlık,gerilimli|Offred, kadınların bedenleri üzerinde söz hakkını yitirdiği Gilead'da geçmişini ve kaçış olasılığını düşünür.
Otomatik Portakal|distopya|özgürlük,şiddet,vicdan|karanlık,tekinsiz|Alex'in suç dolu yaşamı, devletin onu zorla yeniden biçimlendirme girişimiyle irade ve ahlak tartışmasına dönüşür.
Biz|distopya|özgürlük,kimlik,güç|karanlık,düşündürücü|Matematikçi D-503, bütün yaşamın hesaplandığı Tek Devlet'te kişisel duyguların düzeni nasıl sarsabileceğini keşfeder.
Yol|distopya|aile,hayatta kalma,umut|karanlık,duygusal|Bir baba ve oğlu, küle dönmüş bir dünyada güneye yürürken insan kalabilmek için birbirlerine tutunur.
Asla Bırakma Beni|bilimkurgu|kimlik,dostluk,vicdan|melankolik,duygusal|Kathy, Ruth ve Tommy'nin yatılı okuldaki arkadaşlığı, yetişkinlikte öğrendikleri sarsıcı gerçek tarafından yeniden anlam kazanır.
Bulut Atlası|bilimkurgu|özgürlük,güç,bağlantı|destansı,düşündürücü|Farklı çağlarda geçen altı hikâye, insanların birbirinin yaşamına bıraktığı izleri beklenmedik biçimde birleştirir.
Algernon'a Çiçekler|bilimkurgu|kimlik,zekâ,vicdan|duygusal,düşündürücü|Charlie Gordon'ın zekâsını artıran deney, ona yeni imkânlar sunarken ilişkilerini ve kendine bakışını değiştirir.
Kör Baykuş|klasik|kimlik,yalnızlık,gerçeklik|karanlık,tekinsiz|İsimsiz anlatıcı, tekrar eden imgeler ve parçalı anılar içinde sevgiyle ölüm arasındaki saplantısını aktarır.
Dönüşüm|klasik|aile,kimlik,yalnızlık|karanlık,duygusal|Gregor Samsa bir sabah dönüşmüş hâlde uyanır; ailesinin ona bakışı giderek evdeki yerini belirler.
Dava|klasik|adalet,güç,kimlik|tekinsiz,karanlık|Josef K. nedenini öğrenemediği bir suçlamayla karşılaşır ve erişemediği bir yargı düzeninde yol arar.
Şato|klasik|güç,kimlik,yalnızlık|tekinsiz,sakin|Kadastrocu K., çağrıldığı köyde Şato'nun yetkililerine ulaşmaya çalışırken bürokrasinin kapalı kapılarıyla karşılaşır.
Yabancı|klasik|kimlik,vicdan,adalet|sakin,karanlık|Meursault'nun ilgisiz görünen tavrı, işlediği cinayetin yargılanmasında davranışlarının suçtan önce değerlendirilmesine yol açar.
Veba|klasik|dayanışma,hayatta kalma,vicdan|karanlık,umutlu|Oran'da salgın başlayınca Dr. Rieux ve çevresindekiler, belirsizliğe rağmen insanlara yardım etmenin yolunu arar.
Usta ile Margarita|fantastik|güç,aşk,gerçeklik|büyülü,tekinsiz|Şeytan ve maiyetinin Moskova'ya gelişi, bir yazarın kaderini ve Margarita'nın sevgisi için aldığı kararı değiştirir.
Yüzyıllık Yalnızlık|büyülü gerçekçilik|aile,yalnızlık,tarih|büyülü,melankolik|Buendía ailesinin Macondo'daki kuşakları, kasabanın kuruluşundan değişimine uzanan döngüsel bir geçmiş yaşar.
Kolera Günlerinde Aşk|romantik|aşk,zaman,aile|duygusal,melankolik|Florentino Ariza, Fermina Daza'ya duyduğu sevgiyi yıllar boyunca taşırken ikisinin yaşamı farklı yollardan ilerler.
Rüzgârın Gölgesi|gizem|kitaplar,aile,geçmiş|gizemli,duygusal|Daniel, Unutulmuş Kitaplar Mezarlığı'nda bulduğu romanın yazarını araştırırken Barselona'nın saklı hikâyelerine ulaşır.
Gülün Adı|polisiye|gizem,inanç,bilgi|karanlık,düşündürücü|William ile Adso, bir manastırdaki ölümleri araştırırken yasaklı kitapların ve fikir çatışmalarının izini sürer.
Doğu Ekspresinde Cinayet|polisiye|gizem,adalet,strateji|gerilimli,gizemli|Hercule Poirot, karda mahsur kalan trende işlenen cinayeti yolcuların çelişen ifadelerini çözerek araştırır.
Ve Sonra Hiçbiri Kalmadı|polisiye|gizem,suç,vicdan|karanlık,gerilimli|Bir adaya çağrılan on yabancı, geçmişlerindeki suçlamalar ortaya çıktıkça aralarındaki katili bulmaya çalışır.
Ejderha Dövmeli Kız|polisiye|gizem,adalet,aile|karanlık,gerilimli|Gazeteci Mikael Blomkvist ile hacker Lisbeth Salander, yıllar önce kaybolan bir kadının izini sürer.
Kayıp Kız|gerilim|evlilik,kimlik,gerçeklik|karanlık,gerilimli|Amy'nin kaybolmasıyla kocası Nick kamuoyunun şüphe odağı olur; çiftin anlatıları birbirini sarsar.
Sineklerin Tanrısı|klasik|güç,hayatta kalma,toplum|karanlık,gerilimli|Issız adada kalan çocuklar kendi düzenlerini kurmaya çalışırken korku ve iktidar arayışı grubu böler.
Bülbülü Öldürmek|klasik|adalet,aile,önyargı|duygusal,düşündürücü|Scout, babası Atticus'un savunduğu davayı izlerken kasabasındaki önyargıları çocuk gözünden görür.
Gazap Üzümleri|klasik|aile,sınıf,hayatta kalma|destansı,duygusal|Joad ailesi kuraklık ve yoksulluk yüzünden Oklahoma'dan Kaliforniya'ya göç ederken yeni bir yaşam arar.
Fareler ve İnsanlar|klasik|dostluk,yalnızlık,hayal|duygusal,karanlık|Gezici işçiler George ve Lennie, küçük bir çiftlik kurma düşüne tutunurken sert koşullarla karşılaşır.
Muhteşem Gatsby|klasik|aşk,sınıf,hayal|melankolik,ışıltılı|Nick Carraway, gizemli komşusu Gatsby'nin gösterişli partileri ardındaki eski aşka ve Amerikan rüyasına tanık olur.
Çavdar Tarlasında Çocuklar|klasik|kimlik,gençlik,yalnızlık|melankolik,duygusal|Okuldan ayrılan Holden Caulfield, New York'ta dolaşırken yetişkinlerin dünyasıyla arasındaki mesafeyi anlatır.
Küçük Kadınlar|klasik|aile,dostluk,kişisel yolculuk|sıcak,umutlu|March kardeşler savaş yıllarında büyürken farklı hayalleri, kayıpları ve birbirlerine bağlılıklarıyla yol bulur.
Uğultulu Tepeler|romantik|aşk,intikam,aile|karanlık,duygusal|Heathcliff ile Catherine'in kopamayan ilişkisi, iki ailenin sonraki kuşaklarını da etkileyen bir çatışmaya dönüşür.
Anna Karenina|klasik|aşk,aile,toplum|duygusal,melankolik|Anna'nın ilişkisi ve Levin'in yaşam arayışı, Rus toplumunda evlilikle kişisel mutluluk arasındaki gerilimi gösterir.
Karamazov Kardeşler|klasik|aile,inanç,vicdan|karanlık,düşündürücü|Üç kardeşin babalarıyla çatışması, işlenen bir cinayetin ardından suç ve ahlak sorularını büyütür.
Yeraltından Notlar|klasik|kimlik,özgürlük,yalnızlık|karanlık,düşündürücü|Kendini toplumdan çekmiş anlatıcı, çelişkili düşüncelerini ve insanlarla yaşadığı kırıcı karşılaşmaları aktarır.
Monte Cristo Kontu|macera|intikam,adalet,kimlik|destansı,gerilimli|Haksız yere hapsedilen Edmond Dantès, yıllar sonra yeni kimliğiyle özgürlüğüne kavuşur ve geçmişin hesabını sorar.
Üç Silahşörler|macera|dostluk,siyasi entrika,onur|neşeli,destansı|D'Artagnan, kralın muhafızlarına katılma hayaliyle Paris'e gelir ve üç silahşörle tehlikeli entrikalara karışır.
Denizler Altında Yirmi Bin Fersah|macera|keşif,teknoloji,özgürlük|gizemli,destansı|Profesör Aronnax, Kaptan Nemo'nun Nautilus denizaltısında okyanusların bilinmeyen bölgelerini görür.
Seksen Günde Devrialem|macera|keşif,strateji,dostluk|neşeli,heyecanlı|Phileas Fogg, bir iddia üzerine uşağı Passepartout ile dünyayı seksen günde dolaşmak için yola çıkar.
Define Adası|macera|keşif,hazine,güven|heyecanlı,gerilimli|Jim Hawkins, bulduğu haritayla korsanların sakladığı hazineyi arayan gemiye katılır.
Robinson Crusoe|macera|hayatta kalma,keşif,yalnızlık|sakin,gerilimli|Issız bir adaya düşen Robinson, barınak kurup kaynak bulurken yıllar boyunca çevresine uyum sağlar.
Moby Dick|klasik|intikam,doğa,takıntı|karanlık,destansı|Kaptan Ahab, kendisini sakatlayan beyaz balinanın peşinde Pequod'u ve mürettebatını tehlikeli bir yolculuğa sürükler.
İki Şehrin Hikâyesi|klasik|adalet,aşk,fedakârlık|destansı,duygusal|Fransız Devrimi sırasında Londra ile Paris arasında yaşayan karakterlerin kaderi, bir mahkûmun kurtuluşunda birleşir.
Büyük Umutlar|klasik|sınıf,kimlik,aile|duygusal,melankolik|Pip'e gelen gizemli servet, onun Londra'da beyefendi olma isteğini ve geçmişindeki bağları sınar.
David Copperfield|klasik|aile,kimlik,kişisel yolculuk|duygusal,umutlu|David, çocukluğundaki kayıplardan yetişkinlikteki yazarlık yaşamına kadar kendisini biçimlendiren insanları anlatır.
Oliver Twist|klasik|adalet,çocukluk,sınıf|karanlık,umutlu|Yetim Oliver, Londra'nın yoksul mahallelerinde suç çetelerinden uzaklaşıp güvenli bir yuva arar.
Don Kişot|klasik|hayal,dostluk,gerçeklik|neşeli,melankolik|Şövalye romanlarından etkilenen Don Kişot, Sancho Panza'yla dünyayı kendi ideallerine göre düzeltmeye çalışır.
Savaş ve Barış|klasik|aile,savaş,tarih|destansı,düşündürücü|Napolyon savaşları sırasında Rus ailelerinin aşkları, kayıpları ve siyasi kararları büyük tarihsel değişimle kesişir.
Budala|klasik|vicdan,aşk,toplum|duygusal,karanlık|Prens Mışkin'in açık sözlü iyiliği, Petersburg çevresindeki kıskançlık ve çıkar ilişkileriyle çatışır.
Babalar ve Oğullar|klasik|aile,kuşak çatışması,kimlik|sakin,düşündürücü|Bazarov'un nihilist görüşleri, bir aile ziyaretinde geleneksel değerlerle ve kendi duygularıyla karşılaşır.
Madame Bovary|klasik|aşk,hayal,toplum|melankolik,duygusal|Emma Bovary, evlilik yaşamından beklediklerini bulamayınca romantik düşlerinin peşinden giderek borç ve hayal kırıklığıyla yüzleşir.
Siyah Lale|tarihi|aşk,siyasi entrika,umut|duygusal,gerilimli|Cornelius van Baerle, Hollanda'daki siyasi karışıklık sırasında nadir bir siyah lale yetiştirme hayalini ve Rosa'ya sevgisini korur.
İnce Memed|klasik|adalet,özgürlük,sınıf|destansı,umutlu|Memed, Çukurova'daki ağalık düzenine karşı dağa çıkar; kişisel isyanı köylüler için bir umuda dönüşür.
Tutunamayanlar|klasik|kimlik,dostluk,yalnızlık|melankolik,düşündürücü|Turgut Özben, arkadaşı Selim'in ölümünden sonra onun bıraktığı izleri takip ederek kendi hayatını sorgular.
Saatleri Ayarlama Enstitüsü|klasik|modernleşme,kimlik,mizah|neşeli,düşündürücü|Hayri İrdal'ın bir enstitüdeki işi, toplumun yenilik tutkusu ile gündelik alışkanlıkları arasındaki çelişkileri açığa çıkarır.
Kürk Mantolu Madonna|romantik|aşk,yalnızlık,kimlik|duygusal,melankolik|Raif Efendi'nin yıllarca sakladığı defter, Berlin'de Maria Puder ile yaşadığı ilişkinin izlerini anlatır.
Kuyucaklı Yusuf|klasik|adalet,aşk,toplum|karanlık,duygusal|Yusuf'un Muazzez'e bağlılığı, kasabadaki güç ve çıkar ilişkileri içinde giderek zor bir sınava dönüşür.
Bereketli Topraklar Üzerinde|klasik|sınıf,dayanışma,hayatta kalma|karanlık,düşündürücü|Çukurova'ya iş aramaya gelen üç arkadaş, tarla ve fabrikalardaki sert çalışma koşullarıyla karşılaşır.
Kara Kitap|gizem|kimlik,şehir,gerçeklik|gizemli,melankolik|Galip, kaybolan eşini İstanbul'da ararken gazete köşeleri ve eski hikâyeler aracılığıyla kendi kimliğini de izler.
Benim Adım Kırmızı|gizem|sanat,kimlik,aşk|gizemli,düşündürücü|Osmanlı nakkaşları arasındaki bir cinayet, resim geleneği ile değişen bakış açıları üzerine bir soruşturmaya dönüşür.
Masumiyet Müzesi|romantik|aşk,hatıra,sınıf|melankolik,duygusal|Kemal, Füsun'a duyduğu sevgiyi yıllar boyunca eşyalarla ve anılarla biriktirerek İstanbul'daki yaşamını yeniden kurar.
Puslu Kıtalar Atlası|fantastik|gizem,kimlik,keşif|büyülü,tekinsiz|İhsan Oktay Anar'ın eski İstanbul'unda düşler, haritalar ve maceralar birbirine karışır.
Serenad|tarihi|aşk,geçmiş,adalet|duygusal,melankolik|Maya, yaşlı bir profesörün İstanbul ziyaretinde geçmişe uzanan bir aşk hikâyesi ve savaşın izlerini öğrenir.
Çalıkuşu|klasik|aşk,bağımsızlık,kişisel yolculuk|duygusal,umutlu|Feride, öğretmenlik yaparak Anadolu'yu dolaşırken geçmişteki kırgınlığından ve toplumun beklentilerinden uzaklaşmaya çalışır.
Yaprak Dökümü|klasik|aile,modernleşme,toplum|melankolik,duygusal|Ali Rıza Bey'in ailesi, değişen şehir yaşamında değerleri ve geçim sıkıntıları yüzünden çözülme yaşar.
Kiralık Konak|klasik|aile,kuşak çatışması,modernleşme|melankolik,düşündürücü|Bir konağın üç kuşağı, Batılılaşma karşısında farklı hayatlar kurdukça aynı evdeki bağlarını kaybeder.
Tehlikeli Oyunlar|klasik|kimlik,yalnızlık,gerçeklik|tekinsiz,düşündürücü|Hikmet Benol, apartman dairesinde kurduğu oyunlar aracılığıyla ilişkilerini ve kendi sesini anlamaya çalışır.
Atuan Mezarları|fantastik|özgürlük,kimlik,büyü|karanlık,büyülü|Tenar, yeraltı tapınağındaki görevleriyle büyürken Ged'in gelişi ona başka bir yaşam ihtimalini gösterir.
Silmarillion|fantastik|mitoloji,güç,kayıp|destansı,melankolik|Orta Dünya'nın yaratılışından ilk çağlarına uzanan anlatılar, elflerin ve insanların eski savaşlarını bir araya getirir.
Kralların Yolu|fantastik|ayrıntılı evren,onur,güç|destansı,gerilimli|Roshar'da savaş sürerken Kaladin, Shallan ve Dalinar farklı yollardan kadim bir tehdidin izlerini bulur.
Sissoylu: Son İmparatorluk|fantastik|özgürlük,strateji,güç|karanlık,destansı|Vin, metal büyüsünü öğrenen bir hırsız ekibine katılarak bin yıllık imparatorluğu devirmeyi hedefler.
Rüzgârın Adı|fantastik|büyü,kimlik,kişisel yolculuk|büyülü,melankolik|Kvothe, ailesini kaybettiği çocukluktan üniversitedeki yıllarına kadar uzanan yaşam öyküsünü kendi ağzından anlatır.
Altın Pusula|fantastik|keşif,özgürlük,aile|büyülü,gerilimli|Lyra, kaybolan çocukların peşinden kuzeye giderken ruh hayvanları ve paralel dünyalarla ilgili bir sırrı çözmeye yaklaşır.
Narnia Günlükleri: Aslan, Cadı ve Dolap|fantastik|dostluk,cesaret,ayrıntılı evren|büyülü,umutlu|Dört kardeş bir dolaptan Narnia'ya geçer ve Beyaz Cadı'nın kışına karşı Aslan'ın yanında yer alır.
Taht Oyunları|fantastik|siyasi entrika,aile,güç|karanlık,destansı|Westeros'un büyük aileleri taht için mücadele ederken kuzeyde büyüyen eski bir tehlike fark edilmeyi bekler.
Ejderha Mızrağı: Güz Alacakaranlığının Ejderhaları|fantastik|dostluk,ayrıntılı evren,savaş|destansı,büyülü|Eski dostlar Krynn'de yeniden buluşur ve ejderhaların dönüşüyle başlayan savaşa sürüklenir.
Drizzt Efsanesi: Anayurt|fantastik|kimlik,özgürlük,aile|karanlık,destansı|Drizzt, yeraltındaki Menzoberranzan toplumunun kurallarına karşı kendi ahlaki yolunu seçmeye başlar.
Harry Potter ve Azkaban Tutsağı|fantastik|dostluk,gizem,aile|büyülü,gerilimli|Harry'nin üçüncü Hogwarts yılında kaçak mahkûm Sirius Black'in geçmişi, ailesine dair bildiklerini değiştirir.
Açlık Oyunları: Ateşi Yakalamak|distopya|özgürlük,hayatta kalma,güç|gerilimli,karanlık|Katniss'in ilk oyunlardan sonra dönmesi, bölgelerdeki huzursuzluğu artırır ve onu yeni bir arenaya geri götürür.
Uçurtma Avcısı|dram|dostluk,suçluluk,aile|duygusal,melankolik|Amir, çocukluk arkadaşı Hasan'a ilişkin pişmanlığıyla yıllar sonra Afganistan'a dönerek yüzleşir.
Bin Muhteşem Güneş|dram|aile,dayanışma,hayatta kalma|duygusal,karanlık|Meryem ile Leyla'nın yaşamları savaş içindeki Kabil'de birleşir; iki kadın birbirlerine dayanarak güç bulur.
Kitap Hırsızı|tarihi|kitaplar,dostluk,savaş|duygusal,umutlu|Liesel, Nazi Almanyası'nda yeni ailesine uyum sağlarken çaldığı kitaplar ve dostlukları sayesinde dünyasını genişletir.
Pi'nin Yaşamı|macera|hayatta kalma,inanç,gerçeklik|gizemli,umutlu|Pi Patel, bir gemi kazasından sonra Bengal kaplanıyla aynı filikada okyanusu geçmeye çalışır.
Kefaret|dram|aşk,suçluluk,savaş|duygusal,melankolik|Briony'nin çocukken yaptığı yanlış yorum, ablası Cecilia ile Robbie'nin hayatını yıllar boyunca etkiler.
Gece Yarısı Kütüphanesi|fantastik|pişmanlık,kimlik,hayat seçimleri|sakin,umutlu|Nora Seed, olası yaşamlarını barındıran bir kütüphanede verdiği kararların başka sonuçlarını görür.
Bir Kış Gecesi Eğer Bir Yolcu|deneysel|kitaplar,kimlik,gerçeklik|gizemli,neşeli|Bir okur, başladığı romanın devamını ararken peş peşe açılan farklı hikâyelerin içine çekilir.
Ulysses|klasik|şehir,kimlik,gündelik yaşam|düşündürücü,deneysel|Leopold Bloom ile Stephen Dedalus'un Dublin'deki tek günü, farklı anlatım biçimleriyle zihnin ve kentin ayrıntılarını izler.""",
}
