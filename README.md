# Softversko rešenje za pomoć pri praćenju nastave kod dece sa hiperaktivnim poremećajem

#

Đorđe Antić, Petar Ranđelović, Milan Danilović, Aleksa Krstić, Anđela Kostić

#

#

_Sadržaj_ – U ovom radu predstavljen je softver baziran na veštačkoj inteligenciji i računarskom vidu, koji ima namenu da pomogne pri onlajn (_online_) radu sa decom koja pate od ADHD-a. Softver je kreiran pomoću programskog jezika Python.

#

### I. Uvod

#

ADHD (_Attention Deficit Hyperactivity Disorder_), odnosno poremećaj pažnje, je prvi psihijatrijski poremećaj koji je dijagnostifikovan kod dece. Širom sveta čak 8 do 12% dece uglavnom uzrasta od 5 do 18 godina pati od ovog poremećaja. Od ukupnog broja dijagnoza koje deca dobijaju čak 70% se odnosi na ovaj poremećaj. ADHD karakteriše dosta različitih simptoma, a oni najvažniji su nedostatak pažnje, hiperaktivnost i impulsivnost [1].

Deca koja pate od poremećaja pažnje imaju dosta poteškoća u praćenju nastave pa zbog toga zahtevaju poseban tretman od strane predavača. Trenutno, kada se masovno prelazi na onlajn nastavu zbog zatvaranja škola izazvanog pandemijom corona virusa, veliki problem javlja se kod dece sa ADHD-om kod kojih je neophodan poseban pristup pri radu.

Veštačka inteligencija (eng. _Artificial Intelligence - AI_) je grana računarstva koja se bavi razvojem softvera koji bi u određenim situacijama imao ponašanje koje se može okarakterisati kao inteligentno. Veštačka inteligencija je jedan od glavnih predstavnika Industrije 4.0. Programski jezik Python omogućava da lako i efikasno implementiramo različite tehnologije veštačke inteligencije. Prednost ovog programskog jezika je to što se lako može povezati sa ostalim programskim jezicima koji su pogodni za razvoj programa na različitim uređajima.

Računarski vid (eng_. Computer Vision – CV_) je oblast veštačke inteligencije koja uči računar kako da „vidi&quot; i razume sadržaj digitalne slike. Računarski vid uz pomoć modela dubokog učenja može da uoči i klasifikuje određene objekte [2].

Ovaj softver baziran na veštačkoj inteligenciji prati pažnju učenika u toku časa i detektuje trenutke kada učeniku opadne pažnja.

Đorđe Antić, Petar Ranđelović, Milan Danilović, Aleksa Krstić i Anđela Kostić su studenti na modulu Računarstvo i informatika na Elektronskom Fakultetu Univerziteta u Nišu, Aleksandra Medvedeva 14, 18000 Niš, Srbija.

Email: djordje.antic@elfak.rs, petarran@elfak.rs, danilovic.m@elfak.rs, krlekrle@elfak.rs, endziko@elfak.rs

### II. Princip rada

Tehnologije implementirane u softveru prate promenu pravca lica učenika tako da svaki put kada učenik ne gleda u ekran vremenski period duži od 3 sekunde, reaguje glasovnom porukom kojom ga poziva da vrati pažnju na čas. Predavaču stiže informacija o tome da je učeniku opala pažnja kako bi mogao da adekvatno odreaguje. Kada program uoči da lice učenika nije u vidnom polju beleži vreme početka nepažnje, kao i vreme trajanja te nepažnje.

Softver unosi takozvane vremenske pečate u tekstualni fajl i generiše histogram na osnovu koga se može zaključiti u kojim vremenskim intervalima je učeniku značajno opala pažnja. Po završetku predavanja softver računa procenat nepažnje u toku časa.

### III. Implementacija softvera

| ** _A. Python interpretator_ ** |

Za izvršavanje programa pisanog u Python-u, neophodno je instalirati Python interpretator (slika 1.) sa čijom instalacijom se dobija integrisano okruženje za razvoj i učenje (_IDLE_) koje sadrži školjku u kojoj se mogu izvršavati Python programi [3].

# ![](RackMultipart20210326-4-1k6i6gw_html_5c87faad0ef82c5c.png)

Slika 1. Python shell

| **_B. Detekcija lica i orijentiri na licu_** |

#

Detekcija lica je tehnologija bazirana na veštačkoj inteligenciji čija je namena da uoči, locira i identifikuje ljudsko lice [4]. Ova tehnologija koristi različite algoritme kao što su duboko i mašinsko učenje. Projektovan softver koristi biblioteke _dlib_ i _OpenCV_ koje nam pronalaze orijentire na licu.

Orijentiri na licu (eng. _Face Landmarks_) se postavljaju na istaknutim delovima lica kao što su oči, nos, usta, vilica i obrve. Biblioteka _Dlib_ omogućava prepoznavanje 68 tačaka koje će nam biti orijentiri za ključne strukture na licu. Ovi orijentiri lako i uspešno prate poziciju i pokrete lica. Detekcija orijentira na licu se sastoji iz 2 koraka:

1. Lociranje lica na slici
2. Detekcija ključnih struktura na licu

Za lociranje lica i detekciju ključnih struktura na licu neophodno je uvesti biblioteke _OpenCV_, _DLIB_ i _Numpy_.

![](RackMultipart20210326-4-1k6i6gw_html_e143b1ec42940f4a.png)

Osim ovih biblioteka neophodno je uvesti i biblioteke _Winsound_, _Random_, _Datetime_, _Pandas_ i _Plotly.express_ koje omogućavaju reprodukciju zvuka, nasumičan odabir zvučnog zapisa koji će se reprodukovati, prikaz vremena, manipulaciju podacima i analizu i izradu histograma, respektivno.

TABELA I

Opseg tačaka na ključnim strukturama lica

| **Istaknuta crta lica** | **Opseg tačaka** |
| --- | --- |
| **Leva linija vilice** | 0-7 |
| **Brada** | 8 |
| **Desna linija vilice** | 9-16 |
| **Leva obrva** | 17-21 |
| **Desna obrva** | 22-26 |
| **Gornji deo nosa** | 27-30 |
| **Donji deo nosa** | 31-35 |
| **Levo oko** | 36-41 |
| **Desno oko** | 42-47 |
| **Spoljnja ivica usni** | 48-59 |
| **Unutrašnja ivica usni** | 60-67 |

Orijentiri na licu su predodređeni, tako da kada je neophodno uočiti vrh nečije brade, uočavaju se tačke orijentira na licu i obraća se posebna pažnja na tačku broj 8, koja prati vrh brade na licu. Takođe ako je neophodno pratiti obrve, uočavaju se tačke iz opsega 17-21 i 22-26. Ove tačke će omogućiti praćenje položaja lica na osnovu posmatranja kako se one pomeraju u toku vremena [5].

Na slici 2. prikazan je raspored ovih orijentira. Ovakav raspored je univerzalan za svako ljudsko lice tako da će ga program bez problema detektovati na bilo kojoj slici ili video zapisu.

![](RackMultipart20210326-4-1k6i6gw_html_b79e6196611d4992.png)

Slika 2. Orijentiri na licu (_Face landmarks_).

Za detekciju lica sa snimka neophodno je pozvati sledeću funkciju iz dlib biblioteke.

![](RackMultipart20210326-4-1k6i6gw_html_4328035ad65a544e.png)Slika 3. Pozivanje funkcije iz _dlib_ biblioteke.

Za prepoznavanje lica korišćena već istreniranu mašinu ,,_shape\_predictor\_68\_face\_landmarks.dat_&quot; koja se nalazi na opensource github-u [6].

Kao izlazni podatak dobijaju se koordinate uočenog lica sa snimka. Tačke koje se dobiju predstavljaju pravougaonik koji predstavlja naše lice. Prva tačka se odnosi na gornji levi ugao, a druga na donji desni ugao.

![](RackMultipart20210326-4-1k6i6gw_html_334e7f533808d1d6.png)

Slika 4. Izlazni podatak prethodno pozvane funkcije

Sledeći deo koda ima namenu da prati _FaceMap_ vrednosti radi određivanja položaja lica.

![](RackMultipart20210326-4-1k6i6gw_html_41a14210be3deaa9.png)

# Nakon što je položaj lica utvrđen, pratimo _FaceMap_ vrednosti za preklapanja tačaka na očima, a zatim se proveravaju vrednosti i poklapanje kritičnih tačaka lica.

# ![](RackMultipart20210326-4-1k6i6gw_html_56028e0ec0fe6c74.png) ![](RackMultipart20210326-4-1k6i6gw_html_10d359387c83f0e2.png)

# Ukoliko je vreme koje je lice provelo van vidnog polja veće od definisanog, softver će reagovati reprodukovanjem zvučnog zapisa i dodavanjem vremenskog pečata u fajl.

# ![](RackMultipart20210326-4-1k6i6gw_html_18fd89683ec867e5.png)

#

# _C. Histogram_

#

# Po završetku predavanja program generiše histogram na osnovu _.cvs_ fajla u kome se nalaze vremenski intervali u kojima je osobi skrenuta pažnja. Svaki od stubića na histogramu predstavlja interval od 3 minuta u predavanju koje traje 45 minuta. Na y-osi nalazi se broj opomena u tom vremenskom intervalu, a x-osa služi kao vremenska osa.

# ![](RackMultipart20210326-4-1k6i6gw_html_4bc3b91fc72944aa.png)

# Histogram daje uvid u rast i opadanje pažnje u toku predavanja i olakšava predavaču da po potrebi promeni pristup rada u tom vremenskom intervalu.

# Za generisanje histograma korišćena je _matplotlib_ biblioteka na koji je primenjen osmišljen algoritam za inkrementiranje i dekrementiranje određenih vrednosti. Na slici 5. prikazan je histogram generisan testiranjem programa.

# ![](RackMultipart20210326-4-1k6i6gw_html_4426b6fdf013f905.png)

Slika 5. Histogram generisan testiranjem programa.

#

### IV. Zaključak

#

Razvoj ove tehnologije omogućuje predavaču lakši rad sa učenicima koji pate od hiperaktivnog poremećaja. Predavač će znati u kojim vremenskim intervalima treba da napravi pauzu ili obrati posebnu pažnju na učenika. Softver i AI daju informacije predavaču koje učenik možda ne bi umeo da objasni. Takođe daje statistički podatak koji se može iskoristiti u naučne svrhe.

### Zahvalnica

#

Autori rada se zahvaljuju prof. dr Aleksandru Milosavljeviću, sa Elektronskog fakulteta u Nišu na pruženoj pomoći tokom izrade ovog rada.

# Literatura

[1] J. Kudek Mirošević, S. Opić &quot;PONAŠANJA KARAKTERISTIČNA ZA ADHD&quot;, u _Odgojne znanosti_ Zagreb, 2010, vol. 12 br. 1 str. 167-183.

[2] H. Lawaniya, &quot;Computer Vision&quot;, _IET Computer Vision_, 2020, Suresh Gyan Vihar University, Jaipur

[3] Python interpretator https://www.python.org/downloads/

[4] Facial landmarks with dlib, OpenCV, and Python https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ (posećen 29.10.2020.)

[5] Detect Facial Landmark Points With C# And Dlib https://medium.com/machinelearningadvantage/detect-facial-landmark-points-with-c-and-dlib-in-only-50-lines-of-code-71ab59f8873f (posećen 29.10.2020.)

[6] Shape predictor 68 face landmarks https://github.com/topics/shape-predictor-68-face-landmarks
