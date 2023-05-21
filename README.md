# ArtadoBot

Artado Search arama motoru için tasarlanmış açık kaynak kodlu crawler botu.

README'de genel olarak projeyi açıkladım. Gerekirse ayrı dosyalarda daha detaylı açıklamalar yapabilirim.
Örneğin TODO List vs. ama onları herkesin yorumu ile yapmanın daha iyi olacağını düşündüm.

## Temel Yapılacaklar

Botun toplaması gereken temel bilgiler:
- Robots.txt okuyabilmeli ve ona uygun olarak sayfaları gezmeli
- Title, description, keywords gibi meta tagleri
- Sitenin faviconu
- Sayfadaki tüm linkler (a etiketleri)
- Sayfaki resimlerin linkleri (img etiketleri)
- Sayfanın mobile uyumluluğu (puanlamayı etkileyecek)
- Sayfanın kullandığı teknolojiler (JavaScript kullanıp kullanmaması vs.)
- Sayfa içeriğinin dili (opsiyonel, olmasa da olur)

Yani temelde bir crawler hangi verileri alıyorsa ArtadoBot'da onları alacak.
Bunların yanında sayfayı [PageRank](https://tr.wikipedia.org/wiki/PageRank)
algoritmasına göre puanlandıracak. Sıfırdan bir PageRank algoritması
yazmana gerek yok. Bir kütüphaneyi kullanabilirsin.

### Botun Kullanımı

Bot konsol/terminal üzerinden çalıştırılabilir olmalı. Yani 
konsol uygulaması olacak. Botun özellikle Linux ve Windows'da çalıştırılabilir 
olması gerek.

Yaklaşık 3 yıldır Artado Search üzerinden insanlar sonuçlara eklenebilmesi için
[bu sayfadan](https://www.artadosearch.com/AddResult) site ekleyebiliyorlar. Buradan
eklenen linkler onay listesi olarak bir database'e kaydediliyor. Bot hem bu listeden
siteleri sırayla ziyaret edecek, hem zaten sonuçlara eklenmiş siteleri yeniden ziyaret edecek,
hem de mesela `artadobot crawl (url)` diyince o URL'i ziyaret edip o siteyi gezmeye başlayacak.
Bu yüzden farklı modlar olması lazım. Mesela `artadobot waitlist` diyince insanlar tarafından eklenen
siteleri gezmeye başlar. Ayrıca bir sayfada bulduğu yeni linkleri de waitlist'e ekleyebilir veya 
direkt onları da ziyaret eder. Bu ikisini ayrı seçenekler olarak da sunabiliriz. Tabi bu komutlar
sadece birer örnek.

## Sonuçların kaydedilmesi

Web sonuçları ve Görsel sonuçları farklı tablolara kaydedilmekte. Veritabanı olarak MSSQL
kullanıyoruz. 

Web sonuçlarının kaydedildiği tablo:
![image](https://user-images.githubusercontent.com/47920304/236550180-05255164-b3fa-424e-9c09-ee83b6c318c1.png)
ID: otomatik atanan ID

Content1: Site Description

Date: Botun siteyi ziyaret ettiği tarih (DD/MM/YY olarak kaydedersin sen)

Lang: `<html lang="tr"/>` etiketi ile sitenin dilini buluyordum, sen farklı şekilde yapabilirsin.


Görsel sonuçlarının kaydedildiği tablo:

![image](https://user-images.githubusercontent.com/47920304/236553241-1514379e-bab4-4769-baff-86c237d23f4a.png)


Waitlist(Kullanıcılar tarafından eklenen linkler vs):

![image](https://user-images.githubusercontent.com/47920304/236553461-89a04dce-f158-4e4c-8c3b-22415ca5bc87.png)


Tablolarda değişikliklere gidebiliriz. Bunlar senin çalışmanda örnek olması için.

## Kaynaklar

Crawler konusunda yardımcı olabilecek projeler/kaynaklar:
### C#
- Crawler Örnekleri
  + https://github.com/TurnerSoftware/InfinityCrawler
  + https://github.com/dotnetcore/DotnetSpider
  + https://github.com/microfisher/Simple-Web-Crawler
  + https://github.com/sjdirect/abot
  + https://github.com/TheM4hd1/PenCrawLer
  + https://github.com/Misterhex/WebCrawler
  + https://github.com/mehmetozkaya/DotnetCrawler
  + https://github.com/meziantou/WebCrawler
  
 - PageRank
   + https://github.com/jeffersonhwang/pagerank
   + https://github.com/devFarzad/PageRanking
   + https://github.com/ptedlapu/PageRank
   + https://github.com/bitlazy/Godaddy-Expired-Domains-Analyser (Farklı bir şey ama yararlı olabilir gibi)
   + https://github.com/bnji/PageRanker

- Robots.txt
  + https://github.com/TurnerSoftware/RobotsExclusionTools
  + https://github.com/stormid/robotify-netcore
  + https://github.com/karl-sjogren/robots-txt-middleware
  
Daha fazla kaynak eklemesi yapacağım zamanla. Şimdilik bunlar yeterli gibi.  
