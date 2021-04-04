# Bigtable:A DistributedStorageSystemforStructuredData
## Abstract
    Big tableは、googleの多くのサービスで利用されている
    - Google Earth
    - Google Finance
    データサイズ、レイテンシ要求にこたえるのに必要
    データレイアウトやフォーマットを動的にコントロールするBigTableのシンプルデータモデルを解説する
## Introduction
    数千台のサーバーと、数テラバイトのデータに対応する
    
## Data model
    (row:string, column:string, time:int63) -> string
### Rows
    任意文字列(現在は最大64KBまでだが、10~100バイトが一般的なサイズ)
    1つのRow keyのもとのデータへのR/Wはアトミック
    Bigtableは、Row keyを辞書順で保持している
    各rowの範囲は、tabletと呼ばれ、分散とロードバランシングの単位になっている
    webtableでは、URLを反転させることで同じドメインのURLを連続して配置するようになっている
    - ex
      - maps.google.com/index.html
      - com.google.maps/index.html
### Column Families
    column keyのグループであり、アクセスコントロールの基本単位
### Timestamps
    Bigtableの各セルは、同一データの複数バージョンを保持しており、timestampによりインデックスされている
## API
## Building Blocks
    Bigtableは、他のいくつかのGoogleインフラ上に構築されている
    Bigtableは、ログやデータの保存のために、Google Fire System(GFS)を利用している
    Bigtableは、ジョブスケジューリングやリソースマネジメントなどをクラスターマネン地面とシステムに任せている
    Google SSTable file formatは、Bigtableデータを保持するために内部的に利用されている
    SSTbaleは、永続的なオーダーされたイミュータブルマップ(from keys to values)を与える
    Bigtableは、Chubbyと呼ばれる高可用で、持続的な分散ロックサービスを利用している
    Chubbyは、5つのアクティブレプリカで構成されており、1つがマスターに選ばれ、リクエストを分配する
    Chubbyは、障害が発生してもPaxosアルゴリズムを利用してリプ理科の一貫性を保つ
    Bigtableは、Chubbyを様々タスクで利用している
    マスターが1つであることを確認したり、
    Bigtableデータのbootstrapロケーションを保持したり(Section 5.1)、
    tabletサーバーを見つけて、tabletサーバーの死を終わらせたり(Section 5.2)、
    Bigtableスキーマ情報を保持したり、
    アクセス・コントロール・リストを保持したり。
    Chubbyが利用できなくなると、Bigtableも利用できなくなる
## Inmplementation
    Bigtableの実装は、主に3つの要素からなる
    - 各クラインアントにリンクしたライブラリ
    - 1つのマスターサーバー
    - 多くのタブレットサーバー
    
    
