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
    "dizi": """The Wire|suç|sınıf,adalet,güç|karanlık,düşündürücü|Baltimore'da polis, sokak örgütleri ve kamu kurumları arasındaki ilişkiler, bir soruşturmanın farklı cephelerinden izlenir.
The Sopranos|suç|aile,kimlik,güç|karanlık,gerilimli|Mafya lideri Tony Soprano, aile yaşamı ve suç örgütü baskısı arasında terapiye başlar.
Mad Men|dram|kimlik,iş hayatı,aile|melankolik,düşündürücü|Reklamcı Don Draper, 1960'ların değişen Amerika'sında kurduğu kimliği ve yakın ilişkilerini sürdürmeye çalışır.
Succession|dram|aile,güç,siyasi entrika|karanlık,neşeli|Medya patronu Logan Roy'un çocukları, şirketin geleceği ve babalarının onayı için birbirleriyle mücadele eder.
The Americans|gerilim|kimlik,aile,sadakat|karanlık,gerilimli|Soğuk Savaş döneminde Amerikalı aile gibi yaşayan iki Sovyet ajanı, görevleriyle çocukları arasında kalır.
Homeland|gerilim|siyasi entrika,güven,kimlik|gerilimli,karanlık|CIA görevlisi Carrie Mathison, savaş esaretinden dönen bir askerin olası tehdidini araştırırken kendi yargılarına güvenmek zorundadır.
24|aksiyon|terör,hayatta kalma,zaman|gerilimli,heyecanlı|Ajan Jack Bauer, tek bir güne sığan krizlerde zamanla yarışarak saldırıları önlemeye çalışır.
Lost|gizem|hayatta kalma,dostluk,gerçeklik|gizemli,gerilimli|Uçak kazasından sağ çıkanlar, ıssız görünen adada yaşarken geçmişleri ve adanın tuhaflıklarıyla yüzleşir.
The Leftovers|dram|yas,aile,inanç|melankolik,tekinsiz|Dünya nüfusunun bir bölümü açıklanamadan kaybolunca geride kalanlar hayatlarını yeniden anlamlandırmaya çalışır.
Station Eleven|distopya|hayatta kalma,sanat,dostluk|melankolik,umutlu|Küresel salgından yıllar sonra gezici bir tiyatro topluluğu, geçmişle bağını koruyarak yerleşimler arasında dolaşır.
Silo|distopya|gizem,özgürlük,hayatta kalma|karanlık,gerilimli|Yeraltındaki dev siloda yaşayan Juliette, dış dünya hakkındaki kesin kurallara meydan okuyan kanıtlar bulur.
The 100|bilimkurgu|hayatta kalma,gençlik,güç|gerilimli,destansı|Uzay istasyonundan Dünya'ya gönderilen gençler, gezegenin yeniden yaşanabilir olup olmadığını öğrenirken kendi düzenlerini kurar.
Battlestar Galactica|bilimkurgu|hayatta kalma,siyasi entrika,kimlik|karanlık,destansı|Cylon saldırısından kurtulan insan filosu, yeni bir yuva ararken aralarındaki gizli düşmanlardan şüphelenir.
Firefly|bilimkurgu|dostluk,özgürlük,uzay|neşeli,gerilimli|Kaptan Malcolm Reynolds ve Serenity mürettebatı, sınır gezegenlerinde iş alarak merkezi otoriteden uzak yaşamaya çalışır.
Star Trek: The Next Generation|bilimkurgu|keşif,diplomasi,teknoloji|umutlu,destansı|Kaptan Picard'ın Enterprise ekibi, yeni dünyaları araştırırken etik kararlar ve yabancı uygarlıklarla karşılaşır.
Star Trek: Deep Space Nine|bilimkurgu|siyasi entrika,savaş,kimlik|destansı,düşündürücü|Komutan Sisko, stratejik uzay istasyonunda farklı halkların gerilimini yönetirken yaklaşan savaşla uğraşır.
Doctor Who|bilimkurgu|zaman,keşif,dostluk|neşeli,büyülü|Doktor, TARDIS ile farklı zamanlara ve gezegenlere giderek yol arkadaşlarıyla birlikte tehlikeleri çözer.
The X-Files|bilimkurgu|gizem,komplo,güven|karanlık,tekinsiz|FBI ajanları Mulder ile Scully, açıklanamayan olayları araştırırken büyük bir komploya yaklaşır.
Fringe|bilimkurgu|gizem,teknoloji,aile|gerilimli,gizemli|Olivia Dunham'ın ekibi sıra dışı bilimsel olayları araştırırken paralel evrenlerle bağlantı kurar.
Orphan Black|bilimkurgu|kimlik,teknoloji,aile|gerilimli,karanlık|Sarah Manning, kendisine tıpatıp benzeyen bir kadının ölümüne tanık olunca klonların ardındaki kuruluşu araştırır.
Counterpart|bilimkurgu|kimlik,siyasi entrika,gerçeklik|sakin,gerilimli|Sıradan memur Howard Silk, çalıştığı kurumun paralel dünyaya açılan kapısını ve kendi diğer hâlini öğrenir.
12 Monkeys|bilimkurgu|zaman,hayatta kalma,gizem|gerilimli,karanlık|Gelecekten gelen James Cole, yıkıcı salgını önlemek için geçmişteki olayları değiştirmeye çalışır.
Travelers|bilimkurgu|zaman,kimlik,görev|gerilimli,düşündürücü|Gelecekten gelen bilinçler, felaketi önlemek için günümüzde yaşayan insanların bedenlerine yerleşir.
Devs|bilimkurgu|teknoloji,gerçeklik,gizem|sakin,tekinsiz|Yazılım mühendisi Lily, erkek arkadaşının ölümünden sonra çalıştığı şirketin gizli Devs birimini araştırır.
Sense8|bilimkurgu|kimlik,dostluk,özgürlük|duygusal,destansı|Dünyanın farklı şehirlerindeki sekiz kişi, zihinsel bağ kurduklarını keşfederek birbirlerine yardım eder.
Altered Carbon|bilimkurgu|kimlik,teknoloji,sınıf|karanlık,gerilimli|Bilinçlerin bedenler arasında taşınabildiği gelecekte Takeshi Kovacs, zengin bir adamın ölümünü araştırır.
For All Mankind|bilimkurgu|uzay,siyasi entrika,aile|destansı,düşündürücü|Uzay yarışının farklı ilerlediği bir tarihte astronotlar ve aileleri, yeni hedeflerin bedellerini yaşar.
The Last Man on Earth|komedi|yalnızlık,hayatta kalma,toplum|neşeli,tekinsiz|Salgından sonra tek başına kaldığını sanan Phil, başka hayatta kalanlarla karşılaşınca birlikte yaşamanın zorluklarını öğrenir.
The Walking Dead|korku|hayatta kalma,güç,aile|karanlık,gerilimli|Rick Grimes, ölülerin dolaştığı bir dünyada bir grubu korumaya çalışırken insan topluluklarının tehlikeleriyle karşılaşır.
Kingdom|korku|hayatta kalma,siyasi entrika,savaş|karanlık,destansı|Joseon döneminde veliaht prens, saraydaki entrikalarla yayılan ölümcül salgının bağlantısını araştırır.
Sweet Home|korku|hayatta kalma,kimlik,dayanışma|karanlık,gerilimli|Apartman sakinleri insanlar canavara dönüşürken binada birlikte kalmanın ve güvenmenin yolunu arar.
All of Us Are Dead|korku|hayatta kalma,gençlik,dostluk|gerilimli,karanlık|Lisede başlayan zombi salgınında öğrenciler sınıfları geçip yardım gelene kadar direnmeye çalışır.
The Haunting of Hill House|korku|aile,yas,geçmiş|karanlık,duygusal|Crain kardeşler, çocukluklarında yaşadıkları perili eve ve yıllar sonra süren travmalarına geri döner.
Midnight Mass|korku|inanç,toplum,suçluluk|karanlık,tekinsiz|Küçük adaya gelen rahibin ardından yaşanan mucize sanılan olaylar, sakinlerin inançlarını ve korkularını açığa çıkarır.
The Fall of the House of Usher|korku|aile,güç,suç|karanlık,tekinsiz|İlaç şirketi sahibi Roderick Usher, ailesindeki ölümleri anlatırken geçmişteki kararlarının sonuçlarıyla yüzleşir.
Yellowjackets|gerilim|hayatta kalma,geçmiş,kimlik|karanlık,tekinsiz|Uçak kazasından sağ çıkan genç futbolcuların vahşi doğadaki deneyimi, yetişkinlikte yeniden gün yüzüne çıkar.
From|korku|gizem,hayatta kalma,toplum|karanlık,gerilimli|Yolunu kaybedenlerin çıkamadığı kasabada sakinler, geceleri ortaya çıkan varlıklardan korunmak için kurallar oluşturur.
Twin Peaks|gizem|suç,kimlik,gerçeklik|tekinsiz,gizemli|Laura Palmer'ın ölümü, küçük kasabanın sakin görünen yüzünün ardındaki sırları dedektif Dale Cooper'a açar.
True Detective|polisiye|adalet,takıntı,suç|karanlık,gerilimli|Farklı sezonlardaki dedektifler, cinayetleri araştırırken geçmişlerinin ve yaşadıkları yerlerin etkisiyle yüzleşir.
Mindhunter|polisiye|suç,psikoloji,adalet|sakin,tekinsiz|FBI görevlileri Holden Ford ile Bill Tench, seri katillerle görüşerek yeni bir suç analizi yöntemi geliştirmeye çalışır.
Broadchurch|polisiye|suç,aile,toplum|karanlık,duygusal|Bir çocuğun ölümü üzerine yapılan soruşturma, küçük sahil kasabasındaki aileleri ve sırları sarsar.
The Killing|polisiye|suç,siyasi entrika,aile|karanlık,gerilimli|Genç bir kızın cinayeti, dedektiflerin uzun soruşturmasında aile ve yerel siyaseti birbirine bağlar.
Mare of Easttown|polisiye|aile,suç,geçmiş|karanlık,duygusal|Dedektif Mare Sheehan, küçük kasabasındaki cinayeti araştırırken kendi ailesindeki kayıplarla uğraşır.
Happy Valley|polisiye|adalet,aile,geçmiş|karanlık,gerilimli|Polis memuru Catherine Cawood, torununu büyütürken geçmişte ailesine zarar veren kişinin yeniden ortaya çıkmasıyla karşılaşır.
Luther|polisiye|suç,vicdan,takıntı|karanlık,gerilimli|Dedektif John Luther, zor davalarda üstün sezgisini kullanırken işinin kişisel hayatına verdiği zarar büyür.
The Night Of|polisiye|adalet,kimlik,sınıf|karanlık,düşündürücü|Bir cinayetle suçlanan Naz, dava boyunca ceza adaleti sisteminin ve hapishanenin dönüştürücü etkisini yaşar.
The Undoing|gerilim|aile,gerçeklik,suç|gerilimli,karanlık|Terapist Grace Fraser'ın düzenli yaşamı, çevresindeki bir cinayet ve eşine dair şüphelerle çözülür.
Sharp Objects|gerilim|aile,geçmiş,kimlik|karanlık,tekinsiz|Gazeteci Camille, genç kız cinayetlerini araştırmak için döndüğü kasabada annesi ve çocukluğuyla yüzleşir.
Big Little Lies|dram|aile,suç,sınıf|duygusal,gerilimli|Monterey'deki annelerin görünüşte kusursuz yaşamları, okul çevresindeki çatışma ve bir ölümle sarsılır.
The White Lotus|dram|sınıf,güç,kimlik|neşeli,tekinsiz|Lüks tatil köyündeki konuklar ve çalışanlar, dinlenme beklentilerinin ardında sınıfsal gerilimleri açığa çıkarır.
The Handmaid's Tale|distopya|özgürlük,güç,kimlik|karanlık,gerilimli|June, kadınların haklarının ellerinden alındığı Gilead'da kızını bulmak ve sistemden kurtulmak için direnç gösterir.
The Man in the High Castle|alternatif tarih|güç,özgürlük,gerçeklik|karanlık,gerilimli|Mihver devletlerinin kazandığı bir dünyada bulunan filmler, farklı bir tarihin var olabileceğini düşündürür.
Years and Years|dram|aile,teknoloji,siyasi entrika|gerilimli,düşündürücü|Lyons ailesinin yıllara yayılan yaşamı, teknolojik ve siyasi değişimlerin gündelik etkilerini gösterir.
Mr. Inbetween|suç|aile,sadakat,kimlik|karanlık,neşeli|Kirli işlerden para kazanan Ray, kızına iyi bir baba olmaya çalışırken iki yaşamını dengeleyemez.
Barry|suç|kimlik,suç,sanat|karanlık,neşeli|Tetikçi Barry, Los Angeles'ta oyunculuk dersine katılınca geçmişinden çıkıp başka biri olmayı hayal eder.
Ozark|suç|aile,güç,hayatta kalma|karanlık,gerilimli|Marty Byrde, tehlikeli müşterilerine borcunu ödemek için ailesiyle Ozark'a taşınıp para aklamaya başlar.
Narcos|suç|güç,adalet,siyasi entrika|gerilimli,karanlık|Kolombiya'daki uyuşturucu ticaretinin yükselişi, kartellerin ve onları izleyen görevlilerin gözünden anlatılır.
Peaky Blinders|suç|aile,güç,savaş sonrası|karanlık,gerilimli|Tommy Shelby, Birmingham'daki ailesinin işlerini büyütürken savaşın izleriyle ve rakipleriyle uğraşır.
Boardwalk Empire|suç|siyasi entrika,güç,sadakat|karanlık,destansı|İçki yasağı döneminde Atlantic City'yi yöneten Nucky Thompson, siyaset ve suç arasındaki konumunu korumaya çalışır.
The Shield|suç|adalet,güç,vicdan|karanlık,gerilimli|Los Angeles'ta özel polis birimini yöneten Vic Mackey'nin yöntemleri, suçla mücadele ile yolsuzluğu birbirine karıştırır.
Line of Duty|polisiye|adalet,güç,gizem|gerilimli,karanlık|Yolsuzluk karşıtı polis birimi AC-12, teşkilat içindeki şüpheli kararları ve gizli ilişkileri araştırır.
Slow Horses|gerilim|siyasi entrika,sadakat,mizah|karanlık,neşeli|Görevden düşmüş istihbaratçılar, Jackson Lamb yönetiminde beklenmedik biçimde büyük tehditlerin ortasına düşer.
The Night Manager|gerilim|kimlik,siyasi entrika,güven|gerilimli,ışıltılı|Otel yöneticisi Jonathan Pine, silah tüccarı Roper'ın çevresine sızmak için tehlikeli bir rol üstlenir.
Bodyguard|gerilim|siyasi entrika,güven,travma|gerilimli,karanlık|Savaş gazisi koruma David Budd, görüşlerine karşı çıktığı içişleri bakanını korurken komplonun içine çekilir.
Killing Eve|gerilim|takıntı,kimlik,suç|gerilimli,neşeli|İstihbarat görevlisi Eve ile suikastçı Villanelle'in karşılıklı ilgisi, görevlerinin sınırlarını aşar.
The Diplomat|dram|siyasi entrika,evlilik,güç|gerilimli,neşeli|ABD büyükelçisi Kate Wyler, uluslararası krizi yönetirken eşiyle karmaşık ortaklığını sürdürmeye çalışır.
House of Cards|dram|siyasi entrika,güç,intikam|karanlık,gerilimli|Washington'da istediği görevi alamayan Frank Underwood, iktidar basamaklarını kendi yöntemleriyle tırmanır.
The West Wing|dram|siyasi entrika,adalet,dayanışma|umutlu,gerilimli|Başkan Bartlet'in ekibi, Beyaz Saray'da günlük krizlerle ve uzun vadeli siyasi kararlarla uğraşır.
Veep|komedi|siyasi entrika,güç,mizah|neşeli,gerilimli|Başkan yardımcısı Selina Meyer ile ekibi, Washington'daki küçük zaferleri büyük krizlere dönüştürür.
Parks and Recreation|komedi|dostluk,toplum,kişisel yolculuk|neşeli,umutlu|Pawnee belediyesinde çalışan Leslie Knope, kamusal projeleri yürütürken arkadaşlarıyla engelleri aşar.
The Office|komedi|iş hayatı,dostluk,mizah|neşeli,sıcak|Dunder Mifflin'in Scranton ofisindeki çalışanlar, yöneticileri Michael Scott'ın tuhaf kararlarıyla günlük işlerini sürdürür.
Brooklyn Nine-Nine|komedi|dostluk,adalet,mizah|neşeli,sıcak|Jake Peralta ve ekibi, New York'taki polis merkezinde davaları çözerken birbirleriyle güçlü bir bağ kurar.
Community|komedi|dostluk,kimlik,eğitim|neşeli,deneysel|Greendale'de kurulan çalışma grubu, birbirinden farklı üyelerin tuhaf dersler ve kampüs krizleri içindeki arkadaşlığına dönüşür.
Abbott Elementary|komedi|eğitim,dayanışma,mizah|neşeli,umutlu|Philadelphia'daki devlet okulunun öğretmenleri, kısıtlı imkânlara rağmen öğrencileri için yaratıcı yollar bulur.
Schitt's Creek|komedi|aile,sınıf,kişisel yolculuk|neşeli,sıcak|Servetini kaybeden Rose ailesi, sahip oldukları küçük kasabada yaşayarak birbirlerini yeniden tanır.
Modern Family|komedi|aile,kuşak çatışması,mizah|neşeli,sıcak|Birbirine bağlı üç aile, ebeveynlik ve gündelik ilişkilerindeki değişimleri farklı bakış açılarından yaşar.
The Marvelous Mrs. Maisel|komedi|kimlik,aile,kişisel yolculuk|neşeli,ışıltılı|Midge Maisel, evliliği değişince sahne komedyenliğinde kendi sesini bulmaya çalışır.
BoJack Horseman|animasyon|kimlik,şöhret,yas|neşeli,melankolik|Eski televizyon yıldızı BoJack, kariyerindeki boşluk ve arkadaşlarına verdiği zararlarla yüzleşmeye çalışır.
Rick and Morty|animasyon|bilimkurgu,aile,mizah|neşeli,tekinsiz|Bilim insanı Rick ile torunu Morty, boyutlar arasında dolaşırken aile içindeki çatışmaları da yanlarında taşır.
Adventure Time|animasyon|dostluk,keşif,kimlik|büyülü,neşeli|Finn ile Jake, Ooo Diyarı'nda maceralara atılırken çevrelerindeki dünyanın geçmişini keşfeder.
Over the Garden Wall|animasyon|dostluk,hayatta kalma,gizem|büyülü,melankolik|Wirt ve Greg, Bilinmeyen adlı ormanda evlerine dönüş yolunu ararken tuhaf karakterlerle karşılaşır.
Gravity Falls|animasyon|gizem,aile,keşif|neşeli,gizemli|İkizler Dipper ile Mabel, yazı geçirdikleri kasabada garip olayların ve gizli bir günlüğün izini sürer.
Hilda|animasyon|keşif,dostluk,doğa|büyülü,sakin|Hilda, doğadaki yaratıklarla kurduğu bağları yeni taşındığı şehirde sürdürmenin yolunu bulur.
Blue Eye Samurai|animasyon|intikam,kimlik,adalet|karanlık,destansı|Edo dönemi Japonya'sında Mizu, geçmişinden sorumlu insanları bulmak için kimliğini gizleyerek yol alır.
Castlevania|animasyon|intikam,aile,hayatta kalma|karanlık,destansı|Trevor Belmont, Alucard ve Sypha, Drakula'nın insanlığa karşı başlattığı yıkımı durdurmaya çalışır.
Invincible|animasyon|aile,güç,kimlik|karanlık,destansı|Mark Grayson süper güçlerini keşfederken kahraman babası Omni-Man hakkında beklenmedik gerçekler öğrenir.
One Piece|macera|dostluk,keşif,özgürlük|neşeli,destansı|Luffy, efsanevi hazineyi aramak için farklı yeteneklere sahip arkadaşlardan bir korsan ekibi kurar.
Fullmetal Alchemist: Brotherhood|animasyon|aile,adalet,bedel|destansı,duygusal|Edward ile Alphonse, başarısız bir simya girişiminde kaybettiklerini geri almak için Felsefe Taşı'nı arar.
Attack on Titan|animasyon|hayatta kalma,özgürlük,siyasi entrika|karanlık,destansı|Duvarların ardında yaşayan Eren ve arkadaşları, devlerin tehdidini araştırırken kendi dünyalarının geçmişini öğrenir.
Death Note|animasyon|adalet,güç,strateji|karanlık,gerilimli|Light Yagami, isim yazdığı kişiyi öldüren defteri bulur; gizemli dedektif L onu durdurmaya çalışır.
Monster|animasyon|vicdan,suç,kimlik|karanlık,gerilimli|Cerrah Tenma, yıllar önce kurtardığı çocuğun cinayetlerle bağlantısını öğrenince Avrupa boyunca onu arar.
Vinland Saga|animasyon|intikam,savaş,kişisel yolculuk|karanlık,destansı|Thorfinn, babasının ölümünün ardından Viking savaşlarına katılırken intikamının anlamını sorgular.
Cowboy Bebop|animasyon|geçmiş,dostluk,uzay|melankolik,neşeli|Spike ve Bebop ekibi, ödül avcılığı yaparken kaçamadıkları geçmişleriyle farklı gezegenlerde karşılaşır.
Neon Genesis Evangelion|animasyon|kimlik,aile,hayatta kalma|karanlık,tekinsiz|Shinji, insanlığı koruyan dev makineyi kullanmaya çağrılırken babasıyla ve kendi korkularıyla yüzleşir.
The Sandman|fantastik|güç,mitoloji,kimlik|karanlık,büyülü|Yıllarca tutsak kalan Rüya, kaçtıktan sonra kaybettiği eşyaları toplayıp krallığındaki düzeni onarmaya çalışır.
Good Omens|fantastik|dostluk,kader,mizah|neşeli,büyülü|Melek Aziraphale ile iblis Crowley, dünyanın sonunu engellemek için beklenmedik bir ortaklık kurar.
His Dark Materials|fantastik|özgürlük,keşif,aile|büyülü,destansı|Lyra, kaçırılan çocukları ararken paralel dünyaların ve güçlü kurumların sakladığı sırları açar.
The Wheel of Time|fantastik|kehanet,güç,dostluk|destansı,büyülü|Moiraine, karanlık gücü durdurabilecek kişiyi bulmak için beş genci köylerinden uzak bir yolculuğa çıkarır.
House of the Dragon|fantastik|aile,siyasi entrika,güç|karanlık,destansı|Targaryen ailesindeki veraset tartışması, krallığın geleceğini belirleyecek iç savaşa doğru büyür.
The Boys|aksiyon|güç,adalet,şöhret|karanlık,neşeli|Süper kahramanların şirketlerce yönetildiği dünyada Billy Butcher ve ekibi, dokunulmaz sanılan figürlerin suçlarını ortaya çıkarmaya çalışır.""",
}
