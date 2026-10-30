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
    "film": """2001: A Space Odyssey|bilimkurgu|keşif,teknoloji,gerçeklik|gizemli,destansı|Ay'da bulunan siyah monolitin ardından insanlık Jüpiter'e bir görev gönderir; HAL 9000 yolculuğun dengesini değiştirir.
Blade Runner|bilimkurgu|kimlik,teknoloji,vicdan|karanlık,sakin|Rick Deckard, Los Angeles'ta kaçak replikantları ararken insan ile yapay yaşam arasındaki sınırı sorgular.
Alien|bilimkurgu|hayatta kalma,gizem,uzay|karanlık,gerilimli|Nostromo mürettebatı bilinmeyen bir gezegenden gelen sinyali izler ve gemiye taşıdıkları varlıkla ölümcül bir mücadeleye girer.
Aliens|bilimkurgu|hayatta kalma,aile,savaş|gerilimli,destansı|Ripley, iletişimi kesilen koloniye deniz piyadeleriyle döner ve yabancı yaratıklarla yeniden karşılaşır.
Terminator 2: Judgment Day|bilimkurgu|teknoloji,aile,hayatta kalma|gerilimli,umutlu|Sarah Connor ve oğlu John, gelecekten gelen gelişmiş bir makineden korunmak için eski bir düşmanla işbirliği yapar.
Back to the Future|bilimkurgu|aile,zaman,mizah|neşeli,heyecanlı|Marty McFly yanlışlıkla 1955'e gidip anne babasının tanışmasını tehlikeye atınca kendi geleceğini kurtarmaya çalışır.
E.T. the Extra-Terrestrial|bilimkurgu|dostluk,aile,keşif|duygusal,umutlu|Elliott, Dünya'da yalnız kalan bir uzaylıyla arkadaş olur ve onu evine göndermek için kardeşleriyle plan yapar.
Jurassic Park|bilimkurgu|teknoloji,doğa,hayatta kalma|gerilimli,heyecanlı|Genetik yöntemlerle yaratılan dinozorların bulunduğu parkta güvenlik çökünce ziyaretçiler hayatta kalmaya çalışır.
The Fifth Element|bilimkurgu|uzay,kimlik,mizah|neşeli,destansı|Taksi şoförü Korben Dallas, evreni tehdit eden kötülüğü durdurmak için gizemli Leeloo'ya yardım eder.
District 9|bilimkurgu|sınıf,kimlik,önyargı|karanlık,gerilimli|Johannesburg'daki uzaylı yerleşimini yöneten görevli Wikus, bir kazadan sonra dışlananların durumunu bizzat yaşar.
Moon|bilimkurgu|kimlik,teknoloji,yalnızlık|sakin,gizemli|Ay üssündeki görevini bitirmeye hazırlanan Sam Bell, yaşadığı kazadan sonra kendisiyle ilgili ürkütücü bir gerçekle karşılaşır.
Gravity|bilimkurgu|hayatta kalma,uzay,kişisel yolculuk|gerilimli,duygusal|Uzay görevinde yaşanan kaza, Dr. Ryan Stone'u Dünya'ya dönmek için tek başına çözüm aramaya zorlar.
Edge of Tomorrow|bilimkurgu|zaman,hayatta kalma,strateji|gerilimli,heyecanlı|Savaşta ölünce aynı güne dönen William Cage, tekrarlarını kullanarak istilacıların zayıf noktasını bulmaya çalışır.
Looper|bilimkurgu|zaman,kimlik,suç|karanlık,gerilimli|Gelecekten gönderilen hedefleri öldüren Joe, karşısına yaşlı hâli çıkınca kendi kaderini değiştirecek bir seçim yapar.
Minority Report|bilimkurgu|özgürlük,teknoloji,adalet|gerilimli,karanlık|Suçları işlenmeden önce önleyen polis John Anderton, kendisinin bir cinayet işleyeceği öngörülünce sistemden kaçar.
Gattaca|bilimkurgu|kimlik,sınıf,azim|sakin,umutlu|Genetik ölçütlerle fırsatların dağıtıldığı bir dünyada Vincent, uzaya gitme hayali için başka birinin kimliğine bürünür.
Contact|bilimkurgu|iletişim,inanç,keşif|sakin,düşündürücü|Radyo astronomu Ellie Arroway, uzaydan gelen karmaşık bir sinyali çözerek insanlığın ilk temas olasılığıyla yüzleşir.
The Shape of Water|fantastik|aşk,önyargı,özgürlük|büyülü,duygusal|Temizlik görevlisi Elisa, gizli laboratuvarda tutulan amfibi varlıkla yakınlık kurar ve onu kurtarmaya karar verir.
Pan's Labyrinth|fantastik|hayal,savaş,cesaret|karanlık,büyülü|İç savaş sonrası İspanya'da Ofelia, acımasız gerçekliğin yanında sınavlarla dolu bir masal dünyasına girer.
The Fall|fantastik|hayal,dostluk,anlatı|büyülü,duygusal|Hastanedeki bir dublör, küçük Alexandria'ya anlattığı macerayla hem kendi acısını hem çocuğun dünyasını biçimlendirir.
Big Fish|fantastik|aile,anlatı,gerçeklik|büyülü,duygusal|Will Bloom, babasının abartılı görünen hikâyelerinin ardındaki gerçek insanı anlamak için geçmişini araştırır.
The Green Mile|dram|adalet,vicdan,doğaüstü|duygusal,karanlık|İdam koğuşu gardiyanı Paul, olağanüstü yetenekleri olan mahkûm John Coffey'nin suçsuz olabileceğini fark eder.
Forrest Gump|dram|aile,aşk,tarih|duygusal,umutlu|Forrest'in beklenmedik yolculuğu, Amerika'nın değişen dönemlerinden geçerken Jenny'ye bağlılığıyla birleşir.
Good Will Hunting|dram|kimlik,dostluk,kişisel yolculuk|duygusal,umutlu|Üstün matematik yeteneği keşfedilen Will, terapist Sean ile görüşmelerinde geçmişindeki yaraları açar.
Dead Poets Society|dram|özgürlük,eğitim,dostluk|duygusal,umutlu|Öğretmen John Keating, öğrencilerini şiir aracılığıyla kendi seslerini bulmaya çağırırken okulun katı kurallarıyla çatışır.
The Wrestler|dram|kimlik,beden,aile|karanlık,duygusal|Yaşlanan güreşçi Randy, ringdeki yaşamı sona yaklaşırken kızıyla ve çevresindeki insanlarla bağını onarmaya çalışır.
Marriage Story|dram|aile,aşk,ayrılık|duygusal,gerilimli|Oyuncu Nicole ile yönetmen Charlie'nin ayrılığı, oğullarıyla kurdukları yaşamı iki şehir arasında yeniden düzenlemelerini gerektirir.
Before Sunrise|romantik|aşk,iletişim,zaman|sakin,umutlu|Trende tanışan Jesse ile Céline, Viyana'da bir gece boyunca yürüyerek birbirlerinin hayallerini ve korkularını öğrenir.
Before Sunset|romantik|aşk,zaman,hayat seçimleri|sakin,melankolik|Jesse ile Céline, ilk karşılaşmalarından dokuz yıl sonra Paris'te yeniden buluşup kaçırdıkları olasılıkları konuşur.
Before Midnight|romantik|aşk,aile,zaman|duygusal,düşündürücü|Jesse ve Céline, uzun yıllık birlikteliklerinde ebeveynlik ve kişisel beklentiler üzerine zorlu bir konuşma yaşar.
Portrait of a Lady on Fire|romantik|aşk,sanat,özgürlük|sakin,duygusal|Ressam Marianne, evliliğe hazırlanan Héloïse'in portresini gizlice yaparken ikisi arasında yakınlık doğar.
Call Me by Your Name|romantik|aşk,kimlik,yaz|sakin,duygusal|Elio'nun ailesinin yazlık evine gelen Oliver, genç adamın ilk aşk deneyimine ve büyümesine eşlik eder.
The Notebook|romantik|aşk,zaman,sınıf|duygusal,melankolik|Noah ile Allie'nin gençlik aşkı, aile baskısı ve yılların ayırdığı yollar yüzünden farklı biçimlerde sınanır.
Lost in Translation|dram|yalnızlık,iletişim,kimlik|sakin,melankolik|Tokyo'da yabancılık hisseden Bob ile Charlotte, kısa bir dostlukta birbirlerini anlamaya çalışır.
The Secret Life of Walter Mitty|macera|keşif,kişisel yolculuk,hayal|umutlu,neşeli|Walter, kayıp bir fotoğrafın peşinden çıkınca zihnindeki maceralardan gerçek bir yolculuğa geçer.
Little Miss Sunshine|komedi|aile,hayal,dayanışma|neşeli,duygusal|Hoover ailesi, küçük Olive'i güzellik yarışmasına yetiştirmek için arızalı minibüsleriyle uzun bir yolculuğa çıkar.
The Intouchables|komedi|dostluk,sınıf,kişisel yolculuk|neşeli,duygusal|Zengin Philippe ile bakıcısı Driss, farklı yaşam deneyimleri sayesinde birbirlerinin gündelik dünyasını değiştirir.
Jojo Rabbit|komedi|savaş,önyargı,aile|neşeli,duygusal|Nazi Almanyası'nda büyüyen Jojo, annesinin sakladığı Yahudi kızla tanışınca öğrendiği propagandayı sorgular.
The Grandmaster|aksiyon|onur,sanat,tarih|sakin,destansı|Ip Man'in dövüş sanatı yolculuğu, ustalar arası rekabet ve savaş dönemindeki kayıplarla birlikte ilerler.
Crouching Tiger, Hidden Dragon|aksiyon|aşk,onur,özgürlük|büyülü,destansı|Çalınan bir kılıcın peşine düşen savaşçılar, bastırılmış duygular ve toplumsal beklentiler arasında seçim yapar.
Hero|aksiyon|güç,fedakârlık,tarih|destansı,düşündürücü|İsimsiz bir savaşçı, Qin kralına suikastçıları nasıl yendiğini anlatırken aynı olayın farklı yüzleri ortaya çıkar.
Seven Samurai|aksiyon|dayanışma,savaş,onur|destansı,duygusal|Bir köy, haydutların saldırısından korunmak için yedi samuray tutar ve birlikte savunma düzeni kurar.
Ran|dram|aile,güç,savaş|karanlık,destansı|Yaşlı hükümdar Hidetora topraklarını oğulları arasında bölüştürünce aile içindeki iktidar kavgası yıkıcı bir savaşa dönüşür.
The Godfather|suç|aile,güç,sadakat|karanlık,destansı|Michael Corleone, ailesinin suç dünyasından uzak durmak isterken babasına yapılan saldırı sonrası farklı bir yola girer.
The Godfather Part II|suç|aile,güç,geçmiş|karanlık,destansı|Michael'ın aile imparatorluğunu büyütmesi ile genç Vito'nun Amerika'da yükselişi iki ayrı zamanda izlenir.
Goodfellas|suç|güç,sadakat,suç|gerilimli,karanlık|Henry Hill, çocukluktan beri özenerek girdiği mafya çevresinde yükselirken dostlukların ne kadar kırılgan olduğunu görür.
The Departed|suç|kimlik,sadakat,gizem|karanlık,gerilimli|Polis teşkilatındaki köstebek ile mafyanın içine sızan polis, birbirinin kimliğini ortaya çıkarmak için yarışır.
Heat|suç|strateji,onur,takıntı|karanlık,gerilimli|Profesyonel soyguncu Neil ile dedektif Vincent, Los Angeles'ta birbirlerinin hamlelerini izleyerek kaçınılmaz karşılaşmaya yaklaşır.
Pulp Fiction|suç|rastlantı,suç,mizah|karanlık,neşeli|Los Angeles suç dünyasındaki birbirine dolanan hikâyeler, küçük kararların beklenmedik sonuçlarını gösterir.
Reservoir Dogs|suç|sadakat,gizem,suç|karanlık,gerilimli|Başarısız bir soygundan sonra bir depoda buluşan suçlular, aralarındaki muhbirin kim olduğunu anlamaya çalışır.
No Country for Old Men|gerilim|şiddet,kader,adalet|karanlık,gerilimli|Llewelyn Moss çölde bulduğu parayı alınca acımasız Anton Chigurh ve yaşlanan şerif Bell'in peşinden geldiği bir kaçışa girer.
Fargo|suç|sözde planlar,suç,vicdan|karanlık,neşeli|Borçlarını çözmek için kaçırma planı yapan Jerry'nin işi kontrolden çıkar; polis Marge olayların izini sürer.
Zodiac|polisiye|gizem,takıntı,adalet|karanlık,gerilimli|Gazeteciler ve dedektifler, San Francisco'yu korkutan Zodiac katilinin şifreli mektuplarını yıllarca araştırır.
Se7en|polisiye|adalet,suç,vicdan|karanlık,gerilimli|İki dedektif, kurbanlarını ölümcül günahlara göre seçen bir katilin bıraktığı izleri takip eder.
The Silence of the Lambs|gerilim|gizem,kimlik,hayatta kalma|karanlık,gerilimli|FBI öğrencisi Clarice Starling, seri katili bulmak için hapisteki Hannibal Lecter'ın zekâsından yararlanmaya çalışır.
Shutter Island|gerilim|gizem,gerçeklik,suçluluk|karanlık,tekinsiz|Federal polis Teddy Daniels, kayıp bir hastayı aramak için geldiği adadaki akıl hastanesinde kendi anılarına yaklaşır.
Memento|gerilim|hafıza,kimlik,intikam|gizemli,gerilimli|Kısa süreli hafıza kaybı yaşayan Leonard, notları ve dövmeleriyle eşinin katilini bulmaya çalışır.
Gone Girl|gerilim|evlilik,kimlik,gerçeklik|karanlık,gerilimli|Amy'nin kaybolmasının ardından Nick'in anlattıkları ile kamuoyuna sunulan aile hikâyesi birbirini tutmaz.
Prisoners|gerilim|aile,adalet,vicdan|karanlık,gerilimli|İki kız çocuğu kaybolunca bir baba kendi yöntemlerine başvurur; dedektif Loki kanıtların peşinden gider.
The Usual Suspects|suç|gizem,kimlik,strateji|karanlık,gerilimli|Patlama sonrası hayatta kalan Verbal Kint, sorguda beş suçlunun gizemli Keyser Söze ile ilişkisini anlatır.
Fight Club|dram|kimlik,tüketim,gerçeklik|karanlık,tekinsiz|Uykusuz bir anlatıcı ile Tyler Durden'ın kurduğu dövüş kulübü, giderek kontrolden çıkan bir harekete dönüşür.
American Beauty|dram|aile,kimlik,özgürlük|karanlık,düşündürücü|Lester Burnham orta yaş krizinde yaşamını değiştirmeye kalkarken komşularının ve ailesinin saklı çatışmaları açığa çıkar.
Birdman|dram|sanat,kimlik,şöhret|gerilimli,düşündürücü|Eski süper kahraman oyuncusu Riggan, Broadway sahnesinde itibarını yeniden kurmaya çalışırken kendi sesiyle mücadele eder.
The Revenant|macera|hayatta kalma,intikam,doğa|karanlık,destansı|Avcı Hugh Glass, ağır yaralı bırakıldığı vahşi doğada yaşamak ve oğlunun hesabını sormak için ilerler.
Cast Away|macera|hayatta kalma,yalnızlık,umut|sakin,duygusal|Uçak kazasından sonra adada mahsur kalan Chuck, yıllar boyunca gündelik yaşamı yeniden kurmaya çalışır.
Life of Pi|macera|hayatta kalma,inanç,gerçeklik|gizemli,umutlu|Pi Patel, bir Bengal kaplanıyla paylaştığı filikada okyanusu geçerken yaşadıklarını yıllar sonra anlatır.
The Pursuit of Happyness|dram|aile,azim,sınıf|duygusal,umutlu|Chris Gardner, evsizlik ve geçim sıkıntısı içinde oğluna bakarken finans dünyasında bir fırsat yakalamaya çalışır.
12 Years a Slave|tarihi|özgürlük,adalet,hayatta kalma|karanlık,duygusal|Özgür bir müzisyen olan Solomon Northup kaçırılıp köleleştirilir; yıllarca kimliğini ve eve dönme umudunu korur.
Schindler's List|tarihi|savaş,vicdan,hayatta kalma|karanlık,duygusal|Oskar Schindler, fabrikasında çalışan Yahudilerin yaşamını korumak için savaş dönemindeki ilişkilerini kullanır.
The Pianist|tarihi|savaş,hayatta kalma,sanat|karanlık,duygusal|Piyanist Władysław Szpilman, işgal altındaki Varşova'da ailesinden ayrıldıktan sonra saklanarak yaşamaya çalışır.
Dunkirk|savaş|hayatta kalma,dayanışma,zaman|gerilimli,destansı|Dunkirk kıyısında sıkışan askerlerin tahliyesi, kara, deniz ve havadan farklı zaman çizgileriyle izlenir.
1917|savaş|görev,dostluk,hayatta kalma|gerilimli,duygusal|İki İngiliz askeri, bir birliği ölümcül saldırıdan kurtaracak emri ulaştırmak için cepheyi geçer.
Saving Private Ryan|savaş|fedakârlık,dostluk,görev|gerilimli,duygusal|Normandiya çıkarmasının ardından bir birlik, ailesinin diğer oğulları ölen Ryan'ı bulmak için yola çıkar.
Apocalypse Now|savaş|güç,delilik,kimlik|karanlık,tekinsiz|Yüzbaşı Willard, Vietnam Savaşı sırasında ormanın derinlerinde kontrolünü kaybeden Kurtz'u bulma emri alır.
Full Metal Jacket|savaş|şiddet,kimlik,eğitim|karanlık,gerilimli|Askerlerin eğitim kampındaki dönüşümü ile Vietnam'daki savaş deneyimi, insanın şiddet karşısındaki değişimini gösterir.
The Lives of Others|dram|özgürlük,gözetim,vicdan|sakin,gerilimli|Doğu Almanya'da bir yazar ile sevgilisini dinleyen istihbarat görevlisi, izlediği hayatla kendi inançlarını sorgular.
Cinema Paradiso|dram|sinema,dostluk,geçmiş|duygusal,nostaljik|Yönetmen Salvatore, çocukluğundaki sinemacı Alfredo'yu anarak filmlere duyduğu sevgiyi ve kasabasını hatırlar.
The Artist|romantik|sinema,şöhret,aşk|neşeli,melankolik|Sessiz sinema yıldızı George Valentin, sesli film döneminde kariyeri gerilerken genç oyuncu Peppy yükselir.
The Holdovers|dram|yalnızlık,dostluk,geçmiş|sıcak,melankolik|Tatilde yatılı okulda kalan öğretmen Paul, öğrencisi Angus ve aşçı Mary ile beklenmedik bir yakınlık kurar.
The Farewell|dram|aile,göç,gerçeklik|duygusal,sıcak|Billi, büyükannesinin hastalığı aileden saklanırken Çin'e döner ve farklı kuşakların sevgi anlayışını görür.
The Florida Project|dram|çocukluk,sınıf,aile|neşeli,duygusal|Moonee, eğlence parkı yakınındaki motelde yazı oyunlarla geçirirken annesi geçim sıkıntısıyla uğraşır.
The Theory of Everything|dram|bilim,aşk,kişisel yolculuk|duygusal,umutlu|Stephen Hawking'in öğrencilik yıllarında başlayan bilimsel çalışmaları ve Jane ile ilişkisi, hastalığın getirdiği değişimlerle ilerler.
Black Swan|gerilim|sanat,kimlik,takıntı|karanlık,tekinsiz|Balerin Nina, Kuğu Gölü'nün başrolüne hazırlanırken mükemmeliyetçi baskı altında gerçeklik algısını yitirir.
The King of Comedy|komedi|şöhret,takıntı,kimlik|tekinsiz,düşündürücü|Rupert Pupkin, komedyen olma hayalini gerçekleştirmek için televizyon sunucusu Jerry Langford'a saplantılı biçimde yaklaşır.
The Lobster|distopya|aşk,kimlik,toplum|tekinsiz,neşeli|Bekâr insanların eş bulmak zorunda olduğu bir otelde David, ilişki kurallarının acımasızlığıyla karşılaşır.
The Favourite|tarihi|güç,siyasi entrika,rekabet|neşeli,karanlık|Kraliçe Anne'in yakınındaki iki kadın, saraydaki etkilerini korumak için birbirlerine karşı hamleler yapar.
The Banshees of Inisherin|dram|dostluk,yalnızlık,kimlik|melankolik,tekinsiz|Küçük bir adada Colm dostluğu aniden bitirince Pádraic bu kararın nedenini anlamaya çalışır.
Aftersun|dram|aile,hatıra,kimlik|sakin,duygusal|Sophie, babasıyla geçirdiği tatili yıllar sonra anılardan ve kayıtlardan yeniden kurar.
Past Lives|romantik|aşk,kimlik,göç|sakin,melankolik|Çocukluk arkadaşları Nora ile Hae Sung, yıllar sonra New York'ta buluşup seçtikleri hayatların etkisini konuşur.
Minari|dram|aile,göç,umut|sakin,duygusal|Koreli Amerikalı bir aile, Arkansas'ta çiftlik kurmaya çalışırken kuşaklar arası farklı beklentilerle yüzleşir.
Shoplifters|dram|aile,sınıf,adalet|duygusal,karanlık|Geçimini küçük hırsızlıklarla sağlayan bir aile, ihmal edilmiş bir çocuğu yanına alır ve bağlarının sınırlarını gösterir.
Drive My Car|dram|yas,sanat,iletişim|sakin,melankolik|Tiyatro yönetmeni Yūsuke, Hiroşima'daki oyununun hazırlığında genç şoförü Misaki ile uzun yolculuklar paylaşır.
Burning|gizem|sınıf,kıskançlık,gerçeklik|sakin,tekinsiz|Jong-su, çocukluk tanıdığı Hae-mi'nin ortadan kaybolmasından sonra gizemli Ben'in anlattıklarını araştırır.
Memories of Murder|polisiye|adalet,takıntı,gizem|karanlık,gerilimli|Kırsal Kore'de peş peşe işlenen cinayetler, iki dedektifin yöntemlerini ve sabrını sınar.
Oldboy|gerilim|intikam,kimlik,gizem|karanlık,gerilimli|On beş yıl boyunca sebepsiz yere kapatılan Oh Dae-su, serbest bırakılınca kim tarafından ve neden tutulduğunu arar.
Train to Busan|korku|aile,hayatta kalma,dayanışma|gerilimli,duygusal|Baba ve kızı, hızla yayılan salgın sırasında Busan'a giden trende diğer yolcularla birlikte güvenliğe ulaşmaya çalışır.
The Wailing|korku|gizem,inanç,aile|karanlık,tekinsiz|Köyde yaşanan tuhaf ölümler üzerine polis Jong-goo, kızını etkileyen olayların kaynağını anlamaya çalışır.
Get Out|korku|önyargı,kimlik,hayatta kalma|tekinsiz,gerilimli|Chris, sevgilisinin ailesini ziyaret ettiğinde evdeki aşırı nazik tavrın ardında korkunç bir düzen olduğunu fark eder.
Us|korku|aile,kimlik,sınıf|karanlık,tekinsiz|Adelaide'nin ailesi tatilde kendilerine benzeyen yabancılarla karşılaşınca geçmişteki bir olay yeniden açılır.
The Lighthouse|korku|yalnızlık,güç,gerçeklik|karanlık,tekinsiz|Issız bir adadaki iki deniz feneri görevlisi, fırtına ve gerilim altında birbirlerinin güvenini kaybeder.""",
}
